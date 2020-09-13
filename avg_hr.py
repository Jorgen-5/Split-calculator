import pandas as pd
import numpy as np
from datetime import datetime
import time
import re

print()

workoutData = pd.read_csv("bislettTresh.csv", sep=',')

# print(avgLaptime)

start = 0
laps = 10
hrValid = True

try:
    avgHr = workoutData["Gjennomsnittlig puls"]
except:
    hrValid = False

avgLaptime = workoutData["Tid"]


def calcualteAvgHr(startIndex, numLaps):
    sumAvg = 0
    index = 0
    for i in range(startIndex, startIndex + numLaps):
        sumAvg += int(avgHr[index])
        index += 2
    avg = sumAvg / numLaps
    return avg


def calcualteAvgLaptime(startIndex, numLaps):
    sumAvg = 0
    index = startIndex
    for i in range(startIndex, startIndex + numLaps):
        # Get the time in miliesconds
        x = avgLaptime[index].split(',')[0]
        listTime = re.split(r'[:.]', x)
        listTime = [int(i) for i in listTime]

        time = 0
        try:
            # Under 10 minutes for the lap
            time += listTime[2] / 10  # thent of a second to seconds
            time += 60 * listTime[0]  # Minutes to seconds
            time += listTime[1]  # Seconds

        except:
            # Over 10 minutes for the lap
            time += 60 * listTime[0]  # Minutes to secconds
            time += listTime[1]  # Seconds
        # print(timeMs)
        index += 2
        sumAvg += time

    # Calculates avg
    avg = sumAvg / numLaps

    # Converting back
    min, sec = divmod(avg, 60)
    min = int(min)
    sec = round(sec, 1)

    if(sec < 10):
        sec = "0" + str(sec)
    avgTime = str(min) + ":" + str(sec)

    return avgTime


if(hrValid):
    print("Avrage heart rate while running: ",
          round(calcualteAvgHr(start, laps), 1))
else:
    print("Heart rate not detected")

print("Average lap time: ", calcualteAvgLaptime(start, laps))
