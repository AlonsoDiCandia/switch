#!/bin bash
while True
    do
        arp -a | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > /home/pi/switch/raspi/scripts/arp_scan.txt && docker cp /home/pi/switch/raspi/scripts/arp_scan.txt web_switch:/code/raspi/scripts/arp_scan.txt
        sleep 5
    done