#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI

import ConfigParser

class Nrinex:

    # Attributs
    header=dict()
    epochs=dict()

    # Méthodes
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("pionograph.ini")
        filePath=Config.get('input', 'NRINEX_FILE_PATH')
        print filePath
        self.parseNRINEX(filePath)

    def parseNRINEX(self, filePath):
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
                self.process_nrinex_header_line(lines[i])
            else:
                if lines[i][:3]!='   ':
                    if "FILE SPLICE" in lines[i]:
                        next
                    else:
                        #print "INDEX"+str(i)
                        self.process_NRINEX_epoch(i, lines)
                        i+=1
            i+=1
        print self.header
        print self.epochs

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
            self.header['delta_utc_t']=line[42:51]
            self.header['delta_utc_w']=line[51:60]

        elif "LEAP SECONDS" in line:
            self.header['leap_seconds']=line[:6]

    def process_NRINEX_epoch(self, i, lines):
        tmp_epoch={'PRN':lines[i][:2],
                   'time_y':lines[i][2:5],
                   'time_M':lines[i][5:8],
                   'time_d':lines[i][8:11],
                   'time_H':lines[i][11:14],
                   'time_m':lines[i][14:17],
                   'time_s':lines[i][17:22],
                   'sv_clock_bias':lines[i][22:41],
                   'sv_clock_drift':lines[i][41:60],
                   'sv_clock_drift_rate':lines[i][60:79],
                   'iode':lines[i+1][3:22],
                   'crs':lines[i+1][22:41],
                   'delta_n':lines[i+1][41:60],
                   'Mo':lines[i+1][60:79],
                   'cuc':lines[i+2][3:22],
                   'eccentricity':lines[i+2][22:41],
                   'Cus':lines[i+2][41:60],
                   'sqrt_a':lines[i+2][60:79],
                   'toe':lines[i+3][3:22],
                   'cic':lines[i+3][22:41],
                   'OMEGA':lines[i+3][41:60],
                   'cis':lines[i+3][60:79],
                   'loe':lines[i+4][3:22],
                   'crc':lines[i+4][22:41],
                   'omega':lines[i+4][41:60],
                   'OMEGA_dot':lines[i+4][60:79],
                   'i_dot':lines[i+5][3:22],
                   'l2_code_channel':lines[i+5][22:41],
                   'gps_week':lines[i+5][41:60],
                   'l2_p_data_flag':lines[i+5][60:79],
                   'sv_accuracy':lines[i+6][3:22],
                   'sv_health':lines[i+6][22:41],
                   'tgd':lines[i+6][41:60],
                   'iodc':lines[i+6][60:79],
                   'transmission_time':lines[i+6][3:22],
                   'fit_interval':lines[i+6][22:41]
        }
        self.epochs[tmp_epoch['PRN']+'_'+tmp_epoch['time_y']+'_'+tmp_epoch['time_M']+'_'+tmp_epoch['time_d']+'_'+tmp_epoch['time_H']+'_'+tmp_epoch['time_m']+'_'+tmp_epoch['time_s']]=tmp_epoch
nrinex=Nrinex()
