from RESTClient import RESTClient
from ShelfListener import ShelfListener
from shelf import Shelf

import json
import requests
import threading

class ShelfState:
    def __init__(self, shelf_id):
        self.__state = {}
        self.__shelf_id = shelf_id

    def add_chip(self, chipId):
        self.__state[chipId] = True

    def remove_chip(self, chipId):
        self.__state[chipId] = False

    def find_chip(self, chipId):
        return chipId in self.__state and self.__state[chipId] == True

    def get_shelf_id(self):
        return self.__shelf_id

def service_thread(shelf):
    def callback(json):
	if shelf == None: return
        for obj in json:
            shelf.turnLedOn(obj['product_id'])
            requests.delete('http://iot.vpolevoy.com/api/jobs/%s/' % obj['product_id'])

    rest = RESTClient("http://iot.vpolevoy.com/api/jobs/?format=json", callback)
    rest.run()

def main():
    print 'starting up'
    shelf = Shelf()
    listener = ShelfListener()
    shelf.addEventListener(listener)
    shelf.startGovernor()
    #st = ShelfState()
    shelf_id = requests.get("http://iot.vpolevoy.com/api/register/").json()["board_id"]
    service = threading.Thread(target = service_thread, args = [None])
    service.start()
    service.join()
    

if __name__ == "__main__":
    main()
