#! /usr/bin/python
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
    f1=1575.42
    f2=1227.60
    def __init__(self, prn):
        orinex=ORINEX_parser.Orinex()
        nrinex=NRINEX_parser.Nrinex()
        self.epochsToTEC(orinex.epochs,prn,nrinex.epochs,int(orinex.header['leap_seconds']))
    def column(self,matrix, i):
        return [row[i] for row in matrix]
    def epochsToTEC(self, epochs, prn, nrinex,leap):
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
                                r1=float(epochs[epoch][keys][keys_2][keys_3])
                            if keys_3 == "P2":
                                r2=float(epochs[epoch][keys][keys_2][keys_3])
                        print utils.getSatElevation(prn,epochs[epoch]['time_H'],nrinex, leap)
                        tec = -9.5*math.pow(10,16)*(r1-r2)
                        Matrix.append([int(datetime.datetime(int(epoch.split('_')[0])+2000,int(epoch.split('_')[1]),int(epoch.split('_')[2]),int(epoch.split('_')[3]),int(epoch.split('_')[4]),int(float(epoch.split('_')[0]))).strftime('%s')),tec])
        Matrix2=sorted(Matrix,key=operator.itemgetter(0),reverse=False)
        #for i in range(0,len(Matrix2)):
            #print str(Matrix2[i][0])+' '+str(Matrix2[i][1])+'\n'
        plt.plot(self.column(Matrix2,0),self.column(Matrix2,1), 'ro')
        plt.show()
piono=pionograph('G13')
