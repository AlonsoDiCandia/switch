import os,sys
import json
from yeelight import Bulb

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