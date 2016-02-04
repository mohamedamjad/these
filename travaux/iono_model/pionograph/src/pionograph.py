#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI
import ORINEX_parser
import NRINEX_parser
import math
import datetime
import time
import utils
import operator
import matplotlib.pyplot as plt
class pionograph:
    def __init__(self, prn):
        orinex=ORINEX_parser.Orinex()
        nrinex=NRINEX_parser.Nrinex()
        self.epochsToTEC(orinex.epochs,prn,nrinex.epochs,int(orinex.header['leap_seconds']),float(orinex.header['approx_position_x']),float(orinex.header['approx_position_y']),float(orinex.header['approx_position_z']))
    def column(self,matrix, i):
        return [row[i] for row in matrix]
    def epochsToTEC(self, epochs, prn, nrinex,leap,approx_x,approx_y,approx_z):
        Matrix=[]
        Matrix2=[]
        w=1
        phase_i=0
        phase_i_1=0
        r_t_1=0
        for epoch in epochs:
            for keys in epochs[epoch]:
                for keys_2 in epochs[epoch][keys]:
                    #tmp_string+=epoch.replace("_","")+sep+keys_2.replace(" ","")
                    if prn in keys_2:
                        for keys_3 in epochs[epoch][keys][keys_2]:
                            #print keys_3
                            if keys_3 == "P1":
                                if '      ' in epochs[epoch][keys][keys_2][keys_3] or epochs[epoch][keys][keys_2][keys_3]=='':
                                    continue
                                r1=float(epochs[epoch][keys][keys_2][keys_3])
                                #flag+=1
                            if keys_3 == "P2":
                                if '      ' in epochs[epoch][keys][keys_2][keys_3] or epochs[epoch][keys][keys_2][keys_3]=='':
                                    continue
                                #print epochs[epoch][keys][keys_2][keys_3]
                                r2=float(epochs[epoch][keys][keys_2][keys_3])
                                #print r2
                                #flag+=1
                        t=utils.getGPSTime(int(epochs[epoch]['time_y']),int(epochs[epoch]['time_M']),int(epochs[epoch]['time_d']),int(epochs[epoch]['time_H']),int(epochs[epoch]['time_m']),int(float(epochs[epoch]['time_s'])),leap)
                        rec_sat_geo_vect = utils.getSatElevation( prn, epochs[epoch]['time_H'], nrinex, leap,approx_x, approx_y, approx_z, t)
                        # convertion de l'azimuth et l'elevation en degre
                        rec_sat_geo_vect = ((rec_sat_geo_vect[0]), (rec_sat_geo_vect[1]), rec_sat_geo_vect[2])

                        DCBs = utils.getDCBs(prn, epochs[epoch]['time_H'], nrinex,t)
                        print DCBs
                        DCBr = 0.711e-9*3e+8
                        print (r1-r2)*1000.0-DCBr
                        print (r1-r2)*1000.0-DCBr-DCBs
                        print -9.51e+16*((r1-r2)*1000.0-DCBr-DCBs)
                        tec = -9.519643288304653e+16*(r1-r2-DCBs-DCBr)
                        #print tec
                        if tec>1e20 or tec<-1e20:
                            continue
                        # Calcul du VTEC
                        zhPrim = math.asin((6371000.0/(6371000.0+450000.0))*math.sin(1.5708-rec_sat_geo_vect[0]))
                        VTEC = tec*math.cos(zhPrim)
                        print VTEC
                        # Préparation de la matrice des données
                        Matrix.append([int(datetime.datetime(int(epoch.split('_')[0])+2000,int(epoch.split('_')[1]),int(epoch.split('_')[2]),int(epoch.split('_')[3]),int(epoch.split('_')[4]),int(float(epoch.split('_')[0]))).strftime('%s')),tec,rec_sat_geo_vect[0],rec_sat_geo_vect[1],rec_sat_geo_vect[2],epochs[epoch]['time_H'],VTEC])
        Matrix2=sorted(Matrix,key=operator.itemgetter(0),reverse=False)
        #for i in range(0,len(Matrix2)):
            #print str(Matrix2[i][0])+' '+str(Matrix2[i][1])+str(Matrix2[i][2])+' '+str(Matrix2[i][3])+str(Matrix2[i][4])+'\n'
        #plt.plot(self.column(Matrix2,2),self.column(Matrix2,1), 'ro')
        #plt.show()
        plt.plot(self.column(Matrix2,3),self.column(Matrix2,2), 'ro')
        plt.show()
        plt.plot(self.column(Matrix2,0),self.column(Matrix2,3), 'ro')
        plt.show()
        ax = plt.subplot(111, projection='polar')
        ax.plot(self.column(Matrix2,2),self.column(Matrix2,3), 'ro', color='b')
        ax.set_rmax(1)
        ax.grid(True)
        #plt.plot(self.column(Matrix2,1),self.column(Matrix2,2), 'ro', projection='polar')
        plt.show()
piono=pionograph('G 6')
