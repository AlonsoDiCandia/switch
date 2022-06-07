import os,sys
import json
import subprocess
from yeelight import Bulb
from backend.models import Bulb as myBulb

from django.conf import settings
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

def TurnOffBulb(request, bulb):
    if bulb == "central":
        ip = "192.168.17.251"
    elif bulb == "oficina":
        ip = "192.168.17.241"
    bulb = Bulb(ip)
    bulb.turn_off()
    
    return JsonResponse({
        "ok":"ok"
        })

def change_brightness(request, bulb, brightness):
    if bulb == "central":
        ip = "192.168.17.251"
    elif bulb == "oficina":
        ip = "192.168.17.241"
    bulb = Bulb(ip)
    bulb.set_brightness(brightness)

    return JsonResponse({
        "ok":"ok",
        "brillo": brightness
        })


def DiscoverBulbs(self):
    with open(os.path.join(settings.BASE_DIR, "raspi", "scripts", "arp_scan.txt")) as f:
        lines = f.readlines()
    devices = [dev[:-1] for dev in lines if dev[:3] == "192"]
    for a in devices[0]:
        print(a)
    for dev in devices:
        try:
            bulb = Bulb(dev)
            print(dev, bulb.model)
        except:
            print(f"No bulb in {dev}")
    return JsonResponse({
        "devices": devices
        })