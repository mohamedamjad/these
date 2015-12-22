#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI

import ConfigParser


class Orinex:
    # Attributs

    # Voir pour plus d'explications sur le header d'un fichier d'observations rinex sur: http://gage14.upc.es/gLAB/HTML/Observation_Rinex_v2.11.html
    header = {'RINEX_version':'',
              'file_type':'',
              'satellite_system':'',
              'PGM':'',
              'run_by':'',
              'creation_date':'',
              'marker_name':'',
              'marker_number':'',
              'observer':'',
              'agency':'',
              'receiver_number':'', 
              'receiver_type':'',
              'receiver_version':'',
              'antenna_number':'',
              'antenna_type':'',
              'approx_position_x':'',
              'approx_position_y':'',
              'approx_position_z':'',
              'antenna_delta_h':'',
              'antenna_delta_e':'',
              'antenna_delta_n':'',
              'wavelength_factory_L1':'',
              'wavelength_factory_L2':'',
              'observation_number':'',
              'interval':'',
              'time_first_obs_y':'',
              'time_first_obs_M':'',
              'time_first_obs_d':'',
              'time_first_obs_H':'',
              'time_first_obs_m':'',
              'time_first_obs_s':'',
              'time_first_obs_TS':'',# TS: Time System: GPS or GLONASS
              'time_last_obs_y':'',
              'time_last_obs_M':'',
              'time_last_obs_d':'',
              'time_last_obs_H':'',
              'time_last_obs_m':'',
              'time_last_obs_s':'',
              'time_last_obs_TS':'',# TS: Time System: GPS or GLONASS
              'receiver_clock_offset_applied':'',
              'leap_seconds':'',
              'number_of_sat':''}

    epochs = {}
     
    
    # Méthodes
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("pionograph.ini")
        filePath=Config.get('input', 'ORINEX_FILE_PATH')
        print filePath
        self.parseORINEX(filePath)

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
            #print self.epochs
        #print self.header

    def process_ORINEX_epoch(self, index_first_line, lines):
        #print lines[index_first_line]
        # Prend l'indice de la première ligne d'une epoch et parse l'epoch
        #self.epochs[lines[index_first_line][:3]+'_'+lines[index_first_line][3:6]+'_'+lines[index_first_line][6:9]+'_'+lines[index_first_line][9:12]+'_'+lines[index_first_line][12:15]+'_'+lines[index_first_line][15:26]]
        tmp_epoch={'time_y':lines[index_first_line][:3],
                   'time_M':lines[index_first_line][3:6],
                   'time_d':lines[index_first_line][6:9],
                   'time_H':lines[index_first_line][9:12],
                   'time_m':lines[index_first_line][12:15],
                   'time_s':lines[index_first_line][15:26],
                   'epoch_flag':lines[index_first_line][26:29],
                   'epoch_sat_number':lines[index_first_line][29:32],
                   'epoch_satellites':{}}
        #print tmp_epoch
        tmp_sat_epoch={}
        Nsat=int(lines[index_first_line][29:32])
        if int(tmp_epoch['epoch_sat_number'])>12:
            for i in range(0, 12): # les PRN des satellites de l'epoch premier ligne
                tmp_sat_epoch['PRN']=lines[index_first_line][32+i*3:35+i*3]
                tmp_sat_epoch['L1']=lines[index_first_line+2+i*2][:14]
                tmp_sat_epoch['L1LLI']=lines[index_first_line+2+i*2][14:15]
                tmp_sat_epoch['L1SSI']=lines[index_first_line+2+i*2][15:16]
                tmp_sat_epoch['L2']=lines[index_first_line+2+i*2][16:30]
                tmp_sat_epoch['L2LLI']=lines[index_first_line+2+i*2][30:31]
                tmp_sat_epoch['L2SSI']=lines[index_first_line+2+i*2][31:32]
                tmp_sat_epoch['P1']=lines[index_first_line+2+2*i][32:46]
                tmp_sat_epoch['P1SSI']=lines[index_first_line+2+2*i][47:48]
                tmp_sat_epoch['P2']=lines[index_first_line+2+2*i][48:62]
                tmp_sat_epoch['P2SSI']=lines[index_first_line+2+2*i][63:64]
                tmp_sat_epoch['C1']=lines[index_first_line+2+2*i][64:78]
                tmp_sat_epoch['C1SSI']=lines[index_first_line+2+2*i][79:80]
                tmp_sat_epoch['S1']=lines[index_first_line+3+2*i][:14]
                tmp_sat_epoch['S2']=lines[index_first_line+3+2*i][16:30]
                tmp_epoch['epoch_satellites'][tmp_sat_epoch['PRN']]=tmp_sat_epoch

            for i in range(13, Nsat):
                tmp_sat_epoch['PRN']=lines[index_first_line+1][32+(i-13)*3:35+(i-13)*3]
                tmp_sat_epoch['L1']=lines[index_first_line+i*2][:14]
                tmp_sat_epoch['L1LLI']=lines[index_first_line+i*2][14:15]
                tmp_sat_epoch['L1SSI']=lines[index_first_line+i*2][15:16]
                tmp_sat_epoch['L2']=lines[index_first_line+i*2][16:30]
                tmp_sat_epoch['L2LLI']=lines[index_first_line+i*2][30:31]
                tmp_sat_epoch['L2SSI']=lines[index_first_line+i*2][31:32]
                tmp_sat_epoch['P1']=lines[index_first_line+2*i][32:46]
                tmp_sat_epoch['P1SSI']=lines[index_first_line+2*i][47:48]
                tmp_sat_epoch['P2']=lines[index_first_line+2*i][48:62]
                tmp_sat_epoch['P2SSI']=lines[index_first_line+2*i][63:64]
                tmp_sat_epoch['C1']=lines[index_first_line+2*i][64:78]
                tmp_sat_epoch['C1SSI']=lines[index_first_line+2*i][79:80]
                tmp_sat_epoch['S1']=lines[index_first_line+1+2*i][:14]
                tmp_sat_epoch['S2']=lines[index_first_line+1+2*i][16:30]
                tmp_epoch['epoch_satellites'][tmp_sat_epoch['PRN']]=tmp_sat_epoch
        else:
            for i in range(0, Nsat): # les PRN des satellites de l'epoch deuxieme ligne
                tmp_sat_epoch['PRN']=lines[index_first_line][32+i*3:35+i*3]
                tmp_sat_epoch['L1']=lines[index_first_line+2+i*2][:14]
                tmp_sat_epoch['L1LLI']=lines[index_first_line+2+i*2][14:15]
                tmp_sat_epoch['L1SSI']=lines[index_first_line+2+i*2][15:16]
                tmp_sat_epoch['L2']=lines[index_first_line+2+i*2][16:30]
                tmp_sat_epoch['L2LLI']=lines[index_first_line+2+i*2][30:31]
                tmp_sat_epoch['L2SSI']=lines[index_first_line+2+i*2][31:32]
                tmp_sat_epoch['P1']=lines[index_first_line+2+2*i][32:46]
                tmp_sat_epoch['P1SSI']=lines[index_first_line+2+2*i][47:48]
                tmp_sat_epoch['P2']=lines[index_first_line+2+2*i][48:62]
                tmp_sat_epoch['P2SSI']=lines[index_first_line+2+2*i][63:64]
                tmp_sat_epoch['C1']=lines[index_first_line+2+2*i][64:78]
                tmp_sat_epoch['C1SSI']=lines[index_first_line+2+2*i][79:80]
                tmp_sat_epoch['S1']=lines[index_first_line+3+2*i][:14]
                tmp_sat_epoch['S2']=lines[index_first_line+3+2*i][16:30]
                tmp_epoch['epoch_satellites'][tmp_sat_epoch['PRN']]=tmp_sat_epoch

        self.epochs[lines[index_first_line][:3]+'_'+lines[index_first_line][3:6]+'_'+lines[index_first_line][6:9]+'_'+lines[index_first_line][9:12]+'_'+lines[index_first_line][12:15]+'_'+lines[index_first_line][15:26]]=tmp_sat_epoch


    def process_orinex_header_line(self, line):
        if "RINEX VERSION" in line:
            self.header['RINEX_version']=line[:9]
            self.header['file_type']=line[20:40]
            self.header['satellite_system']=line[40:60]

        elif "RUN BY" in line:
            self.header['PGM']=line[:20]
            self.header['run_by']=line[20:40]
            self.header['creation_date']=line[40:60]

        elif "MARKER NAME" in line:
            self.header['marker_name']=line[:60]

        elif "MARKER NUMBER" in line:
            self.header['marker_number']=line[:20]

        elif "AGENCY" in line:
            self.header['observer']=line[:20]
            self.header['agency']=line[20:60]

        elif "REC #" in line:
            self.header['receiver_number']=line[:20]
            self.header['receiver_type']=line[20:40]
            self.header['receiver_version']=line[40:60]

        elif "ANT #" in line:
            self.header['antenna_number']=line[:20]
            self.header['antenna_type']=line[20:40]

        elif "APPROX POSITION" in line:
            self.header['approx_position_x']=line[:15]
            self.header['approx_position_y']=line[15:30]
            self.header['approx_position_z']=line[30:45]

        elif "ANTENNA: DELTA" in line:
            self.header['antenna_delta_h']=line[:15]
            self.header['antenna_delta_e']=line[15:30]
            self.header['antenna_delta_n']=line[30:45]

        elif "WAVELENGTH FACT" in line:
            self.header['wavelength_factory_L1']=line[:6]
            self.header['wavelength_factory_L2']=line[6:12]

        elif "# / TYPES OF OBS" in line:
            self.header['observation_number']=line[:6]

        elif "INTERVAL" in line:
            self.header['interval']=line[:10]

        elif "TIME OF FIRST OBS" in line:
            self.header['time_first_obs_y']=line[:6]
            self.header['time_first_obs_M']=line[6:12]
            self.header['time_first_obs_d']=line[12:18]
            self.header['time_first_obs_H']=line[18:24]
            self.header['time_first_obs_m']=line[24:30]
            self.header['time_first_obs_s']=line[30:44]
            self.header['time_first_obs_TS']=line[44:52]

        elif "TIME OF LAST OBS" in line:
            self.header['time_last_obs_y']=line[:6]
            self.header['time_last_obs_M']=line[6:12]
            self.header['time_last_obs_d']=line[12:18]
            self.header['time_last_obs_H']=line[18:24]
            self.header['time_last_obs_m']=line[24:30]
            self.header['time_last_obs_s']=line[30:44]
            self.header['time_last_obs_TS']=line[44:52]

        elif "CLOCK OFFS APPL" in line:
            self.header['receiver_clock_offset_applied']=line[:6]

        elif "LEAP SECONDS" in line:
            self.header['leap_seconds']=line[:6]

        elif "# OF SATELLITES" in line:
            self.header['number_of_sat']=line[:6]

rinex=ORINEX()
