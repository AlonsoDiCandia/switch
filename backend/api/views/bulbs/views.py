import os,sys
import json
import subprocess
from yeelight import Bulb
from backend.models.models import Bulb as myBulb, House
from backend.synchronizer.sunset.SunsetSynchronizer import SunsetSynchronizer

from django.http import JsonResponse


def TurnOnOffBulb(request, bulb):
    my_bulb = myBulb.objects.get(name=bulb)
    bulb = Bulb(my_bulb.ip)
    properties = bulb.get_properties()
    bulb_status = properties['power']

    if bulb_status == 'on':
        bulb.turn_off()
        bulb_status = 'off'
    elif bulb_status == 'off':
        bulb.turn_on()
        bulb_status = 'on'
    else:
        return JsonResponse({
            "error": "No se pudo determinar el estado de la ampolleta."
        })

    return JsonResponse({
        "status": bulb_status,
        "ok": "ok"
        })

def TurnOnAllBulbs(request):
    house = House.objects.get(name='Los Corregidores')
    sunset = SunsetSynchronizer(house)

    sunset_info = sunset.get_sunset_info()

    if sunset.time_now > sunset_info['sunset']:

        bulbs = myBulb.objects.all()

        response = {}

        for _bulb in bulbs:
            bulb = Bulb(_bulb.ip)
            bulb.turn_on()
            bulb.set_rgb(248, 248, 255)
            bulb.set_brightness(70)
            

            properties = bulb.get_properties()
            bulb_status = properties['power']
            
            response[_bulb.name] = bulb_status
        
        return JsonResponse(response)
