import os,sys
import json
import subprocess
from yeelight import Bulb

from django.conf import settings
from django.http import JsonResponse


def TurnOnBulb(request, bulb):
    if bulb == "central":
        ip = "192.168.17.251"
    elif bulb == "oficina":
        ip = "192.168.17.241"
    bulb = Bulb(ip)
    bulb.turn_on()

    return JsonResponse({
        "ok":"ok"
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