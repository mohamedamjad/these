#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI pour KYLIA

# TODO: ligne FORMAT le séparateur ne doit pas etre ' ' par defaut
# TODO:
import ConfigParser
import ORINEX_parser
import utils
import pionograph
class RinexToMatrix:

    def __init__(self):
        print 'ok'
        orinex=ORINEX_parser.Orinex()
        Config = ConfigParser.ConfigParser()
        Config.read("pionograph.ini")
        filePath=Config.get('output', 'MFILES_DIRECTORY')
        file=open(filePath,'r+') 
        #print orinex.epochs
        #self.rinexToMatrixHeader(file, orinex.header, '#', ' ')
        self.rinexToMatrix(file, orinex.epochs, ' ')

    def rinexToMatrixHeader(self, file, header, comment, sep): # Prend en entré le header du rinex et le transfome en commentaires dans un fichier .m
        file.write(comment+' CONVERTED FROM RINEX BY IGN-KYLIA GPS TOOLBOX\n')
        file.write(comment+' KEEP THE HEADER AS IT IS\n')
        file.write(comment+' YOU CAN ADD YOUR OWN COMMENT BY PRECEDING THE LINE BY:'+comment)
        file.write(comment+' SEPARATOR \''+sep+'\'')
        file.write(comment+' INPUT RINEX VERSION: '+header['RINEX_version']+'\n')
        file.write(comment+' INPUT FILE TYPE:'+header['file_type']+'\n')
        file.write(comment+' SATELLITE SYSTEM USED:'+header['satellite_system']+'\n')
        file.write(comment+' RINEX CREATION DATE:'+header['creation_date']+'\n')
        file.write(comment+' MARKER NAME:'+header['marker_name']+'\n')
        file.write(comment+' MARKER NUMBER:'+header['marker_number']+'\n')
        file.write(comment+' OBSERVER:'+header['observer']+' AGENCY: '+header['agency']+'\n')
        file.write(comment+' RECEIVER NUMBER:'+header['receiver_number']+' RECEIVER TYPE: '+header['receiver_type']+' RECEIVER VERSION: '+header['receiver_version']+'\n')
        file.write(comment+' ANTENNA NUMBER:'+header['antenna_number']+' ANTENNA TYPE: '+header['antenna_type']+'\n')
        file.write(comment+' APPROX. POS. X:'+header['approx_position_x']+' APPROX. POS. Y: '+header['approx_position_y']+' APPROX. POS. Z: '+header['approx_position_z']+'\n')
        file.write(comment+' ANTENNA DELTA H:'+header['antenna_delta_h']+' ANTENNA DELTA E: '+header['antenna_delta_e']+' ANTENNA DELTA N: '+header['antenna_delta_n']+'\n')
        file.write(comment+' WAVELENGTH FACTORY L1'+header['wavelength_factory_L1']+' WAVELENGTH FACTORY L2: '+header['wavelength_factory_L2']+'\n')
        file.write(comment+' OBSERVATION NUMBER:'+header['observation_number']+' EPOCHS INTERVAL: '+header['interval']+'\n')
        file.write(comment+' FIRST OBS. DATE TIME'+header['time_first_obs_d']+'-'+header['time_first_obs_M']+'-'+header['time_first_obs_y']+' '+header['time_first_obs_H']+':'+header['time_first_obs_m']+':'+header['time_first_obs_s']+' FIRST OBS. TIME SYSTEM: '+header['time_first_obs_TS']+'\n')
        file.write(comment+' LAST OBS. DATE TIME'+header['time_last_obs_d']+'-'+header['time_last_obs_M']+'-'+header['time_last_obs_y']+' '+header['time_last_obs_H']+':'+header['time_last_obs_m']+':'+header['time_last_obs_s']+' LAST OBS. TIME SYSTEM: '+header['time_last_obs_TS']+'\n')
        file.write(comment+' IS RECEIVER CLOCK OFFSET ALREADY APPLIED: '+header['receiver_clock_offset_applied']+'\n')
        file.write(comment+' LEAP SECONDS: '+header['leap_seconds']+'\n')
        file.write(comment+' NUMBER OF SAT: '+header['number_of_sat']+'\n')
        file.write(comment+' END OF HEADER\n')
        file.write(comment+' FORMAT:EPOCH PRN L1 L1LLI L1SSI L2 L2LLI L2SSI P1 P1SSI P2 P2SSI C1 C1SSI S1 S2')

    def rinexToMatrix(self, file, epochs, sep):
        tmp_string=''
        print epochs
        for epoch in epochs:
            for keys in epochs[epoch]:
                for keys_2 in epochs[epoch]['epoch_satellites']:
                    tmp_string+=epoch.replace("_","")+sep+keys_2.replace(" ","")
                    for keys_3 in epochs[epoch]['epoch_satellites'][keys_2]:
                        #print keys_3
                        tmp_string+=sep+epochs[epoch]['epoch_satellites'][keys_2][keys_3].replace(" ","")
                    #print tmp_string+'\n$$$$$$$$$$$'
                    print tmp_string+'\n'
                    tmp_string = ''
rTom=RinexToMatrix()
