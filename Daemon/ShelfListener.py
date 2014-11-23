from shelf import ShelfEventListener

class ShelfListener(ShelfEventListener):
    def __init__(self, shelf_sate, service):
        self.__shelf_state = state
        self.__service = service
    
    def onItemAdded(self, chipId):
        self.__shelf_state.add_chip(chipId)
        
    def onItemFirstAdded(self, chipId):
        rj = requests.get(service).json()
        if rj == "[OK]":
            self.onItemAdded(chipId)

    def onItemRemoved(self, chipId):
        self.__shelf_state.remove_chip(chipId)
