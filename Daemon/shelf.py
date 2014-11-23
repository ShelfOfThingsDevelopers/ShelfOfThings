import mraa
import pyupm_i2clcd as lcd
import threading
import time

class Shelf:
    eventListeners = []
    beepDurationS = 0.5

    # Range of used LED GPIOs
    gpiosRange = range(2, 12) 
    gpios = []

    # Gpio used for TX and another one that is inverted
    gpioTx = mraa.Gpio(1)
    gpioITx = mraa.Gpio(0)

    aio = mraa.Aio(0)
    
    # Array of chip IDs
    chipIDs=[0b00111001,
            0b11011001,
            0b10010110,
            0b00110110,
            0b00100111,
            0b11100110]

    chipPresence=[False,
            False,
            False,
            False,
            False,
            False]

    chipPositions=range(11)

    posMinVals=range(400, 411)

    def __init__(self):
        self.lcd = lcd.Jhd1313m1(6, 0x3E, 0x62)
        self.lcd.write(" Shelf of Things")
        # Initialising GPIOs
        for gpioN in self.gpiosRange:
            gpio = mraa.Gpio(gpioN)
            gpio.dir(mraa.DIR_OUT)
            self.gpios.append(gpio)
        self.gpioTx.dir(mraa.DIR_OUT)
        self.gpioITx.dir(mraa.DIR_OUT)
        self.gpioTx.write(1)
        self.gpioITx.write(0)
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
        i = chipIDs.index(chipId)
        if self.chipPresence[i]:
            gpios[self.chipPositions[i]].write(1)

    '''
    Turn off LED of item with specified ID
    '''
    def turnLedOff(self, chipId):
        i = chipIDs.index(chipId)
        if self.chipPresence[i]:
            gpios[self.chipPositions[i]].write(0)

    def addEventListener(self, eventListener):
        if isinstance(eventListener, ShelfEventListener):
            self.eventListeners.append(eventListener)
    
    def onItemAdded(self, chipId):
        for listener in self.eventListeners:
            listener.onItemAdded(position, chipId)

    def onItemRemoved(self, chipId):
        for listener in self.eventListeners:
            listener.onItemRemoved(chipId)

class ShelfGovernor:
    delayS = 0.5
    responseDelayS = 0.5
    resposeCheckPeriodS = 0.02

    noiseEpsilon = 200

    def __init__(self, shelf):
        self.shelf = shelf
        self._shutdown_request = False

    def shutdown(self):
        self._shutdown_request = True

    def loop(self):
        aio = mraa.Aio(0)
        gpioTx = self.shelf.gpioTx
        gpioITx = self.shelf.gpioITx
        chipIDs = self.shelf.chipIDs
        sender = Sender(gpioTx, gpioITx)
        posMinVals = self.shelf.posMinVals
        shelf = self.shelf
        self._shutdown_request = False
        while not self._shutdown_request:
            for chipCtr in range(len(chipIDs)):
                chipId = chipIDs[chipCtr]
                analogVal = aio.read()
                sender.sendNumber(chipId)
                t = time.time()
                while time.time() < (t + self.responseDelayS):
                    checkAnalog = aio.read()
                    if checkAnalog > (analogVal + self.noiseEpsilon):
                        if not shelf.chipPresence[chipCtr]:
                            shelf.onItemAdded(chipId)
                            shelf.chipPresence[chipCtr] = True
                            shelf.lcd.clear()
                            shelf.lcd.write("Item was added")
                        pos = 0
                        while posMinVals[pos] < checkAnalog:
                            pos+=1
                        shelf.chipPositions[chipCtr] = pos
                        continue
                    time.sleep(self.resposeCheckPeriodS)
                if shelf.chipPresence[chipCtr]:
                    shelf.onItemRemoved(chipId)
                    shelf.chipPresence[chipCtr] = False
                    shelf.lcd.clear()
                    shelf.lcd.write("Item was removed")
            time.sleep(self.delayS)

class Sender:
        duration1S = 0.21
        duration0S = 0.020

        sleepS = 0.05

        numberSize = 8

        def __init__(self, gpio, gpioI):
                self.gpio = gpio
                self.gpioI = gpioI

        def sendNumber(self, number):
                for i in range(self.numberSize):
                        if (number & (1 << self.numberSize-1)) == 0:
                                self._send0()
                        else:
                                self._send1()
                        number = number << 1
                        time.sleep(self.sleepS)

        def _send1(self):
                self._lowerVoltage(self.duration1S)

        def _send0(self):
                self._lowerVoltage(self.duration0S)

        def _lowerVoltage(self, durationS):
                self.gpio.write(0)
                self.gpioI.write(1)
                time.sleep(durationS)
                self.gpio.write(1)
                self.gpioI.write(0)

'''
Interface for event listener
'''
class ShelfEventListener:
    def onItemAdded(self, chipId):
        return

    def onItemRemoved(self, chipId):
        return
