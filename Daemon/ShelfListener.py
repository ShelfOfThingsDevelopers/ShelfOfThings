from shelf import ShelfEventListener
import requests

class ShelfListener(ShelfEventListener):
    def __init__(self):
	self.__chips = []
    
    def onItemAdded(self, chipId):
	    if chipId not in self.__chips:
		    headers = {"content-type": "application/x-www-form-urlencoded"}
		    answer = requests.post('http://iot.vpolevoy.com/api/product/', data='product_id=%s' % chipId, headers=headers)
        
    def onItemFirstAdded(self, chipId):
        pass
	#rj = requests.get(service).json()
        #if rj == "[OK]":
        #    self.onItemAdded(chipId)

    def onItemRemoved(self, chipId):
        pass
	#self.__shelf_state.remove_chip(chipId)
