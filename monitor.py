#!/usr/bin/python
import iostat

PROC = '/proc/meminfo'
INTERVAL = 1


def collect():
    """
    Collector cpu stats
    """

    statFile = open(PROC, "r")
    timeList = statFile.readline()
    iostat.log("debug","The first line is " + str(timeList))
    statFile.close()
    rawValue = timeList.split()[1]
    print rawValue

if __name__ == "__main__":
    iostat.log("info","I've started the main function.")
    collect()