import mraa
import threading

class Shelf:
    eventListeners = []
    beepDurationMs = 500

    def __init__(self):
        #TODO
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
    def turnLedOn(self, itemId):
        #TODO
        return

    '''
    Turn off LED of item with specified ID
    '''
    def turnLedOff(self, itemId):
        #TODO
        return

    '''
    Beep
    Length of beep is controlled by beepDurationMs
    '''
    def beep(self):
        # TODO
        return

    '''
    Flash chip on item with specified ID
    '''
    def flashItem(self, position, newItemId):
        #TODO
        return

    def addEventListener(self, eventListener):
        if isinstance(eventListener, ShelfEventListener):
            self.eventListeners.append(eventListener)
    
    def _onItemAdded(self, position, itemId):
        for listener in self.eventListeners:
            listener.onItemAdded(position, itemId)

    def _onItemFirstAdded(self, position):
        for listener in self.eventListeners:
            listener.onItemFirstAdded(position)

    def _onItemRemoved(self, itemId):
        for listener in self.eventListeners:
            listener.onItemRemoved(itemId)

class ShelfGovernor:
    delayS = 1

    def __init__(self, shelf):
        self.shelf = shelf
        self._shutdown_request = False

    def shutdown(self):
        self._shutdown_request = True

    def loop(self):
        self._shutdown_request = False
        while not self._shutdown_request:
            #TODO
            time.sleep(self.delayS)

'''
Interface for event listener
'''
class ShelfEventListener:
    def onItemAdded(self, position, itemId):
        return

    def onItemFirstAdded(self, position):
        return

    def onItemRemoved(self, itemId):
        return
