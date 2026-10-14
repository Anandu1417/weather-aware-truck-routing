from enum import IntEnum

class Risk(IntEnum):
    LOW=0
    MODERATE=1
    HIGH=2
    SEVERE=3
    NO_TRAVEL=4

def wind_level(mph: float)-> Risk:
    if mph>=55:
        return Risk.NO_TRAVEL
    if mph>=45:
        return Risk.SEVERE
    if mph>=35:
        return Risk.HIGH
    if mph>=25:
        return Risk.MODERATE
    return Risk.LOW  

def rain_level(inches_per_hour: float)->Risk:
    if inches_per_hour>1:
        return Risk.NO_TRAVEL
    if inches_per_hour>=0.5:
        return Risk.SEVERE
    if inches_per_hour>=.25:
        return Risk.HIGH
    if inches_per_hour>=.1:
        return Risk.MODERATE
    return Risk.LOW
    