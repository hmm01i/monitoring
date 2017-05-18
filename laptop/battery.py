#!/usr/bin/env python

#this scipt is intended to query battery stats from a laptop
#it looks for battery information is in /sys/class/power_supply/
import os
import logging
import re

def main():
    logging.basicConfig(level=logging.DEBUG)
    path = '/sys/class/power_supply/'
    bats_re = re.compile('^BAT[0-9]+')
    bats = []
    bat_stats = {}
    power_supplies = os.listdir(path)
    logging.debug("power supplies found {}".format(power_supplies))
    for i in power_supplies:
        m = bats_re.match(i)
        if m:
            bats.append(m.group())
            bat_stats[m.group()] = {}
    logging.debug("Batteries found: {}".format(bats))
    for i in bats:
        for l in open(path+i+'/uevent'):
            print(l)
            bat_stats[i][l.split('=')[0]] = l.split('=')[1].strip()
    print(bat_stats)

if __name__ == "__main__":
    main()
