#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI pour KYLIA
import ephemeris
import datetime as dt
def getSatElevation(PRN,h,nav_msg,leap_seconds, xr, yr, zr): # cette fonction retourne le triplet lamda phi h
    tmp_nav_msgs=dict()
    for msg in nav_msg: # Tous les ephemerides du PRN qu'on cherche
        if int(PRN[1:3]) == int(msg[0:2]) and int(h) == int(msg[15:18]):
            eph=ephemeris.Ephemeris()
            t=getGPSTime(int(msg[3:6]),int(msg[7:10]),int(msg[11:14]),int(msg[15:18]),int(msg[19:22]),int(float(msg[23:29])),leap_seconds) 
            return eph.getSatXYZ(nav_msg[msg], t)

def cropIntValue(value): # Éliminer les espaces en plus dans les str qui doivent être exploité comme int ou float
    return str(int(value))

def cropFloatValue(value):
    return str(float(value))

def getGPSTime(y, M, d, h, m, s, leap):
    a = dt.datetime(1980,1,6,0,0,0)
    b = dt.datetime(2000+y, M, d, h, m, s)
    return (b-a).total_seconds()+leap
