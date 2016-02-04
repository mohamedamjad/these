#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed-Amjad LASRI
import math
import ConfigParser
class Ephemeris:

    def getSatXYZ(self, epoch, t): # Calcul XYZ du satellite en un temps t
        # Récupération des constantes depuis le fichier ini
        config = ConfigParser.ConfigParser()
        config.read('pionograph.ini')
        mu = config.get('constantes','mu')
        ome = config.get('constantes','ome')

        t0 = t-float(epoch['toe'].replace("D","e"))
        if t0>302400:
            t0-=604800
        if t0<302400:
            t0+=6048000
        # Correction du biais d'horloge
        t0-=float(epoch['sv_clock_bias'].replace("D","e"))+float(epoch['sv_clock_drift'].replace("D","e"))*t0+float(epoch['sv_clock_drift_rate'].replace("D","e"))*t0*t0
        # Calcul du mouvement moyen
        n0=math.sqrt(float(mu)/math.pow(float(epoch['sqrt_a'].replace("D","e")),6))
        n=n0+float(epoch['delta_n'].replace("D","e"))
        # Calcul de l'anomalie moyenne en t
        M=float(epoch['M0'].replace("D","e"))+n*t0
        # résolution de l'équation de kepler par itération
        Em=M
        E=0
        for i in range(0,20):
            E=M+float(epoch['eccentricity'].replace("D","e"))*math.sin(Em)
            Em=E
        # Calcul de l'anomalie vraie du satellite
        w = 2*math.atan(math.sqrt((1+float(epoch['eccentricity'].replace("D","e")))/(1-float(epoch['eccentricity'].replace("D","e"))))*math.tan(E/2))
        # Culcul de l'argument de longitude
        du=float(epoch['cuc'].replace("D","e"))*math.cos(2*(w+float(epoch['omega'].replace("D","e"))))+float(epoch['Cus'].replace("D","e"))*math.sin(2*(w+float(epoch['omega'].replace("D","e"))))
        u=w+float(epoch['omega'].replace("D","e"))+du
        # Calcul du rayon terre-satellite
        dr=float(epoch['crc'].replace("D","e"))*math.cos(2*(w+float(epoch['omega'].replace("D","e"))))+float(epoch['crs'].replace("D","e"))*math.sin(2*(w+float(epoch['omega'].replace("D","e"))))
        r=float(epoch['sqrt_a'].replace("D","e"))*float(epoch['sqrt_a'].replace("D","e"))*(1-float(epoch['eccentricity'].replace("D","e"))*math.cos(E))+dr
        # Calcul des coordonnées du satellite sur le plan orbital:
        x=r*math.cos(u)
        y=r*math.sin(u)
        # Position du plan orbital sur l'espace
        di=float(epoch['cic'].replace("D","e"))*math.cos(2*(w+float(epoch['omega'].replace("D","e"))))+float(epoch['cis'].replace("D","e"))*math.sin(2*(w+float(epoch['omega'].replace("D","e"))))
        i=float(epoch['I0'].replace("D","e"))+t0*float(epoch['i_dot'].replace("D","e"))+di
        om=float(epoch['OMEGA'].replace("D","e"))+(float(epoch['OMEGA_dot'].replace("D","e"))-float(ome))*t0-float(ome)*float(epoch['toe'].replace("D","e"))
        # Coordonnées catésiennes en WGS-84
        X=x*math.cos(om)-y*math.sin(om)*math.cos(i)
        Y=x*math.sin(om)+y*math.cos(om)*math.cos(i)
        Z=y*math.sin(i)
        # Retourne le résultat
        return (X,Y,Z)

    def cart2geo(self, X,Y,Z): # Convertit coordonnées cartésiennes en geographiques
        config = ConfigParser.ConfigParser()
        config.read('pionograph.ini')
        f = config.get('constantes','f')
        f = float(f)
        a = config.get('constantes','a')
        a = float(a)
        R=math.sqrt(X*X+Y*Y+Z*Z)
        # Remarque du chef à ne pas OUBLIER pour atan(Y/X)
        lamda=math.atan(Y/X)
        e=math.sqrt(1-math.pow((1-f),2))
        #phi = math.acos(Z/R)
        mu=math.atan(Z/math.sqrt(X*X+Y*Y)*((1-f)+(e*e*a/R)))
        phi=math.atan((Z*(1-f)+e*e*a*math.pow(math.sin(mu),3))/((1-f)*(math.sqrt(X*X+Y*Y)-e*e*a*math.pow(math.cos(mu),3))))
        if phi<0:
            lamda=lamda+math.pi
            phi*=-1
        h=(math.sqrt(X*X+Y*Y)*math.cos(phi))+(Z*math.sin(phi))-(a*math.sqrt(1-e*e*math.pow(math.sin(phi),2)))
        return (lamda,phi,h)

    def rec_sat_vector(self, xr, yr, zr, xs, ys, zs): # Calculer le vecteur recepteur-satellite dans le repere de la station
        # dans ce qui suit j'utilise la matrice de rotation suivante
        # lamda est la longitude, phi est la latitude
        #
        #     | -sin(lamda)                    cos(lamda)                    0                |
        # R = | -sin(phi)*cos(lamda)          -sin(phi)*sin(lamda)           cos(phi)         |
        #     | cos(phi)*cos(lamda)           cos(phi)*sin(lamda)            sin(phi)         |
        #
        # Xrep_r, Yrep_r, Zrep_r : correspondent aux X, Y et Z du vecteur satellite-recepteur mais dans
        #                          le repere de la station (repere topo-cenitrique)
        (lamda,phi,h) = self.cart2geo(xr, yr, zr)
        Xrep_r = -math.sin(lamda)*(xs-xr)+math.cos(lamda)*(ys-yr)
        Yrep_r = -math.sin(phi)*math.cos(lamda)*(xs-xr)-math.sin(phi)*math.sin(lamda)*(ys-yr)+math.cos(phi)*(zs-zr)
        Zrep_r = math.cos(phi)*math.cos(lamda)*(xs-xr)+math.sin(lamda)*math.cos(phi)*(ys-yr)+math.sin(phi)*(zs-zr)
        # Par moi
        #     | cos(lamda)                   -sin(lamda)                    0                 |
        # R = | cos(phi)*sin(lamda)          -cos(phi)*cos(lamda)           -sin(phi)         |
        #     | sin(phi)*sin(lamda)          cos(lamda)*sin(phi)          cos(phi)          |
        #Xrep_r = math.cos(lamda)*(xs-xr)-math.sin(lamda)*(ys-yr)
        #Yrep_r = math.cos(phi)*math.sin(lamda)*(xs-xr)-math.cos(phi)*math.cos(lamda)*(ys-yr)-math.sin(phi)*(zs-zr)
        #Zrep_r = math.sin(phi)*math.sin(lamda)*(xs-xr)+math.cos(lamda)*math.sin(phi)*(ys-yr)+math.cos(phi)*(zs-zr)

        return (Xrep_r, Yrep_r, Zrep_r)
eph=Ephemeris()
