#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI

class Nrinex:

    # Attributs
    header={}
    epochs={}

    # Méthodes
    def __init__(self):

    def parseORINEX(self, filePath):
    file = open(filePath, 'r+')
    lines = file.readlines()
    file.seek(0, 0)
    h=True
    i=0
    while i<len(lines):
        if h:
            if "END OF HEADER" in lines[i]:
                h=False
                #print self.header
                print "-------------END OF HEADER-----------------"
            self.process_orinex_header_line(lines[i])
        else:
            if "G" in lines[i] or "R" in lines[i]:
                if "FILE SPLICE" in lines[i]:
                    next
                else:
                    #print "INDEX"+str(i)
                    self.process_ORINEX_epoch(i, lines)
                    i+=1
        i+=1

    def process_nrinex_header_line(self, line):
        if "RINEX VERSION" in line:
            self.header['RINEX_version']=line[:9]
            self.header['file_type']=line[20:40]
            self.header['satellite_system']=line[40:60]

        elif "RUN BY" in line:
            self.header['PGM']=line[:20]
            self.header['run_by']=line[20:40]
            self.header['creation_date']=line[40:60]

        elif "ION ALPHA" in line:
            self.header['ion_alpha_1']=line[:15]
            self.header['ion_alpha_2']=line[15:30]
            self.header['ion_alpha_3']=line[30:45]
            self.header['ion_alpha_4']=line[45:60]

        elif "ION BETA" in line:
            self.header['ion_beta_1']=line[:15]
            self.header['ion_beta_2']=line[15:30]
            self.header['ion_beta_3']=line[30:45]
            self.header['ion_beta_4']=line[45:60]

        elif "DELTA-UTC" in line:
            self.header['delta_utc_a0']=line[:21]
            self.header['delta_utc_a1']=line[21:42]
            self.header['delta_utc_t']=line[42,51]
            self.header['delta_utc_w']=line[51,60]

        elif "LEAP SECONDS" in line:
            self.header['leap_seconds']=line[:6]

    def 
