#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os, sys

# This script need to run outside container

from yeelight import discover_bulbs


bulbs = { "bulbs": discover_bulbs()}
print(bulbs)

json_file = open("./sync/bulbs/bulbs.json", "w")
json_file.write(str(bulbs).replace("\'", "\""))
json_file.close()

