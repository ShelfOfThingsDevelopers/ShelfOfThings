#!/usr/bin/env python
import requests
import time

class RESTClient:
    def __init__(self, url, callback):
        self.__url = url
        self.__callback = callback

    def run(self):
        while(True):
            self.__callback(requests.get(self.__url).json())
            time.sleep(1)

