import mraa
import threading
import time

class Shelf:
    eventListeners = []
    beepDurationS = 0.5

    # Range of used GPIOs
    #TODO restore to range(2, 12)
    gpiosRange = [2]
    gpios = []
    
    # Used Analog IO port
    aio = mraa.Aio(0)

    # Array of items with corresponding GPIOs
    # Index - chip id
    # Value - Stated GPIO
    itemGPIOs=range(6)

    def __init__(self):
        # Initialising GPIOs
        for gpioN in self.gpiosRange:
            gpio = StatedGPIO(mraa.Gpio(gpioN))
            gpio.setStateOutHigh()
            self.gpios.append(gpio)
        self.governor = ShelfGovernor(self)

    '''
    Start governor that checks shelf in loop
    '''
    def startGovernor(self):
        governorThread = threading.Thread(target = self.governor.loop)
        governorThread.daemon = True
        governorThread.start()

    '''
    Stop governor
    '''
    def stopGovernor(self):
        self.governor.shutdown()

    '''
    Turn on LED of item with specified ID
    '''
    def turnLedOn(self, chipId):
        itemGPIO = self.itemGPIOs[chipId]
        itemGPIO.setStateIn()

    '''
    Turn off LED of item with specified ID
    '''
    def turnLedOff(self, chipId):
        itemGPIO = self.itemGPIOs[chipId]
        itemGPIO.setStateOutHigh()

    '''
    Beep
    Length of beep is controlled by beepDurationS
    '''
    def beep(self):
        # TODO
        return

    def addEventListener(self, eventListener):
        if isinstance(eventListener, ShelfEventListener):
            self.eventListeners.append(eventListener)
    
    def onItemAdded(self, position, chipId):
        for listener in self.eventListeners:
            listener.onItemAdded(position, chipId)

    def onItemFirstAdded(self, position):
        for listener in self.eventListeners:
            listener.onItemFirstAdded(position)

    def onItemRemoved(self, chipId):
        for listener in self.eventListeners:
            listener.onItemRemoved(chipId)

class ShelfGovernor:
    delayS = 0.5
    analogDelayS = 0.05
    impulseTimeS = 0.1

    def __init__(self, shelf):
        self.shelf = shelf
        self._shutdown_request = False

    def shutdown(self):
        self._shutdown_request = True

    def loop(self):
        gpios = self.shelf.gpios
        aio = self.shelf.aio
        self._shutdown_request = False
        while not self._shutdown_request:
            for gpio in gpios:
                analogVal = aio.read()
                print 'aio1', aio.read()
                if gpio.state == gpio.STATE_IN:
                    gpio.setStateOutLow()
                    time.sleep(0.001)
                    gpio.setStateIn()
                else:
                    gpio.setStateOutLow()
                    time.sleep(0.001)
                    gpio.setStateOutHigh()
                # Wait for capacitor to charge 
                time.sleep(0.01)
                t = time.time()
                while aio.read() > analogVal:
                    time.sleep(self.analogDelayS)
                    print 'aio2', aio.read()
                t = time.time() - t
                print "t:", t
                print 'aio3', aio.read()
                chipId = int(t / self.impulseTimeS)
                #self.shelf.itemGPIOs[chipId]=gpio
            time.sleep(self.delayS)

'''
Wrapper for GPIO because we need to store state
'''
class StatedGPIO:
    gpio=None
    state=None
    STATE_OUT_HIGH=0
    STATE_OUT_LOW=1
    STATE_IN=2

    def __init__(self, gpio):
        self.gpio = gpio
    
    def setStateOutHigh(self):
        if self.state != self.STATE_OUT_HIGH:
            if self.state == self.STATE_IN:
                self.gpio.dir(mraa.DIR_OUT)
            self.gpio.write(1)

    def setStateOutLow(self):
        if self.state != self.STATE_OUT_LOW:
            if self.state == self.STATE_IN:
                self.gpio.dir(mraa.DIR_OUT)
            self.gpio.write(0)

    def setStateIn(self):
        if self.state != self.STATE_IN:
            self.gpio.write(0)
            self.gpio.dir(mraa.DIR_IN)

'''
Interface for event listener
'''
class ShelfEventListener:
    def onItemAdded(self, chipId):
        return

    def onItemFirstAdded(self, chipId):
        return

    def onItemRemoved(self, chipId):
        return
