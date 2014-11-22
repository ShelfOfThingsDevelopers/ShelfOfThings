import mraa
import threading

class Shelf:
    eventListeners = []
    beepDurationS = 0.5

    # Range of used GPIOs
    gpiosRange = range(2, 12)
    gpios = []
    
    # Used Analog IO port
    aio = mraa.Aio(0)

    # Array of items with corresponding GPIOs
    # Index - chip id
    # Value - Stated GPIO
    itemGPIOs=[]

    def __init__(self):
        # Initialising GPIOs
        for gpioN in self.gpiosRange:
            gpio = mraa.Gpio(gpioN)
            gpio.dir(mraa.DIR_IN)
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
        itemGPIO.dir(mraa.DIR_OUT)
        itemGPIO.write(0)
        return

    '''
    Turn off LED of item with specified ID
    '''
    def turnLedOff(self, chipId):
        #TODO
        return

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
    analogDelayS = 0.1
    impulseTimeS = 0.1

    def __init__(self, shelf):
        self.shelf = shelf
        self._shutdown_request = False

    def shutdown(self):
        self._shutdown_request = True

    def loop(self):
        gpios = shelf.gpios
        aio = shelf.aio
        self._shutdown_request = False
        while not self._shutdown_request:
            for gpio in gpios:
                analogVal = aio.read()
                gpio.dir(mraa.DIR_OUT)
                gpio.write(1)
                t = time.time()
                while aio.read() > analogVal:
                    time.sleep(self.analogDelayS)
                t = time.time() - t
                chipId = t / impulseTimeS
                shelf.itemGPIOs[chipId]=gpio
                gpio.write(0)
                gpio.dir(mraa.DIR_IN)
            time.sleep(self.delayS)

class StatedGPIO:
    gpio=None
    state=None
    STATE_OUT_HIGH=0
    STATE_OUT_LOW=1
    STATE_IN=2
    
    def setStateOutHigh(self):
        return

    def setStateOutLow(self):
        return

    def setStateIn(self):
        return

    def _setState(self, state):
        if self.state != state:
            

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
