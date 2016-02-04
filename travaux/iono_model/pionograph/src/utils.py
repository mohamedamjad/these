#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI pour KYLIA
import math
import ConfigParser
import ephemeris
import datetime as dt
def getSatElevation(PRN,h,nav_msg,leap_seconds, xr, yr, zr, t): # cette fonction retourne le triplet lamda phi h
    tmp_nav_msgs=dict()
    rec_sat_vect = ()
    for msg in nav_msg: # Tous les ephemerides du PRN qu'on cherche
        if int(PRN[1:3]) == int(msg[0:2]) and int(h) == int(msg[15:18]):
            eph=ephemeris.Ephemeris()
            #t=getGPSTime(int(msg[3:6]),int(msg[7:10]),int(msg[11:14]),int(msg[15:18]),int(msg[19:22]),int(float(msg[23:29])),leap_seconds) 
            cartesian_sat_coordinate = eph.getSatXYZ(nav_msg[msg], t)
            rec_sat_vect = eph.rec_sat_vector( xr, yr, zr, cartesian_sat_coordinate[0], cartesian_sat_coordinate[1], cartesian_sat_coordinate[2])
            n = math.sqrt(rec_sat_vect[0]*rec_sat_vect[0]+rec_sat_vect[1]*rec_sat_vect[1]+rec_sat_vect[2]*rec_sat_vect[2] )
            rec_sat_vect = (rec_sat_vect[0]/n, rec_sat_vect[1]/n, rec_sat_vect[2]/n)
            return rec_sat_vect
            rec_sat_vect_geo = eph.cart2geo(rec_sat_vect[0],rec_sat_vect[1],rec_sat_vect[2])
            #return rec_sat_vect_geo
    return getSatElevation(PRN,str(int(h)-1),nav_msg,leap_seconds, xr, yr, zr, t)

def cropIntValue(value): # Éliminer les espaces en plus dans les str qui doivent être exploité comme int ou float
    return str(int(value))

def cropFloatValue(value):
    return str(float(value))

def getGPSTime(y, M, d, h, m, s, leap):
    a = dt.datetime(1980,1,6,0,0,0)
    b = dt.datetime(2000+y, M, d, h, m, s)
    return (b-a).total_seconds()+leap

def getDCBs(PRN, h, nrinex,t):
    config = ConfigParser.ConfigParser()
    config.read('pionograph.ini')
    c = float(config.get('constantes','c'))
    for msg in nrinex:
        if int(PRN[1:3]) == int(msg[0:2]) and int(h) == int(msg[15:18]):
            return float(nrinex[msg]['tgd'].replace("D","e"))*float(1.0-math.pow(77.0/60.0,2))*c
    return getDCBs(PRN, str(int(h)-1), nrinex,t)
