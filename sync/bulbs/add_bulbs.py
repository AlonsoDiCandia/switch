#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path[:current_path.find(os.path.dirname(__file__))]
sys.path.append(current_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "switch.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import json 
from backend.models.models import Bulb

json_file = open("./sync/bulbs/bulbs.json", "r")

json_data = json.loads(json_file.read())

for bulb in json_data['bulbs']:
    new_bulb, _ = Bulb.objects.get_or_create(
        name = bulb['capabilities']['name'],
        ip = bulb['ip'],
        port = bulb['port'],
        external_id = bulb['capabilities']['id'],
        power = True if bulb['capabilities']['power'].lower() is 'on' else False if bulb['capabilities']['power'].lower() is 'off' else False
    )
    print(new_bulb.ip)

