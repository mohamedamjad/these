#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed-Amjad LASRI
import math
import ConfigParser
class Ephemeris:
    def __init__(self):
        print 'OK'

    def getSatXYZ(self, epoch, t): # Calcul XYZ du satellite en un temps t
        # Récupération des constantes depuis le fichier ini
        config = ConfigParser.ConfigParser()
        config.read('pionograph.ini')
        mu = config.get('constantes','mu')
        ome = config.get('constantes','ome')

        t0 = t-float(epoch['toe'])
        if t0>100000:
            t0-=604800
        if t0<100000:
            t0+=6048000
        # Correction du biais d'horloge
        t0-=float(epoch['sv_clock_bias'])+float(epoch['sv_clock_drift'])*t0+float(epoch['sv_clock_drate'])*t0*t0
        # Calcul du mouvement moyen
        n0=math.sqrt(mu/math.pow(float(epoch['sqrt_a']),6))
        n=n0+float(epoch['delta_n'])
        # Calcul de l'anomalie moyenne en t
        M=float(epoch['M0'])+n*t0
        # résolution de l'équation de kepler par itération
        Em=M
        E=0
        for i in range(0,20):
            E=M+float(epoch['eccentricity'])*math.sin(Em)
            Em=E
        # Calcul de l'anomalie vraie du satellite
        w = 2*math.atan(math.sqrt((1+float(epoch['eccentricity']))/(1-float(epoch['eccentricity'])))*math.tan(E/2))
        # Culcul de l'argument de longitude
        du=float(epoch['cuc'])*math.cos(2*(w+float(epoch['omega'])))+float(epoch['Cus'])*math.sin(2*(w+float(epoch['omega'])))
        u=w+float(epoch['omega'])+du
        # Calcul du rayon terre-satellite
        dr=float(epoch['crc'])*math.cos(2*(w+float(epoch['omega'])))+float(epoch['crs'])*sin(2*(w+float(epoch['omega'])))
        r=float(epoch['sqrt_a'])*float(epoch['sqrt_a'])*(1-float(epoch['eccentricity'])*math.cos(E))+dr
        # Calcul des coordonnées du satellite sur le plan orbital:
        x=r*math.cos(u)
        y=r*math.sin(u)
        # Position du plan orbital sur l'espace
        di=sloat(epoch['cic'])*math.cos(2*(w+float(epoch['omega'])))+float(epoch['cis'])*math.sin(2*(w+float(epoch['omega'])))
        i=float(epoch['I0'])+t0*float(epoch['i_dot'])+di
        om=float(epoch['OMEGA0'])+(float(epoch['OMEGA_dot'])-ome)*t0-ome*float(epoch['toe'])
        # Coordonnées catésiennes en WGS-84
        X=x*math.cos(om)-y*math.sin(om)*math.cos(i)
        Y=x*math.sin(om)+y*math.cos(om)*math.cos(i)
        Z=y*math.sin(i)
        # Retourne le résultat
        return (X,Y,Z)
