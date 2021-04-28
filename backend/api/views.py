import os,sys
import json
from yeelight import Bulb, discover_bulbs


from django.http import JsonResponse


def TurnOnBulb(self, bulb):
    bulb = Bulb("192.168.17.241")
    bulb.turn_on()

    return JsonResponse({
        "ok":"ok"
        })

def TurnOffBulb(self, bulb):
    bulb = Bulb("192.168.17.241")
    bulb.turn_off()
    
    return JsonResponse({
        "ok":"ok"
        })

def DiscoverBulbs(self):
    print(discover_bulbs(timeout=20, interface='192.168.17.0/24'))
    return JsonResponse({
        "ok":"ok"
        })