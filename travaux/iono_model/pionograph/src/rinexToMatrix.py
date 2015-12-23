#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI pour KYLIA

import ConfingParser

class RinexToMatrix:

    def __init__():
        print 'OK'

    def cropIntValue(value): # Éliminer les espaces en plus dans les str qui doivent être exploité comme int ou float
        return str(int(value))

    def cropFloatValue(value):
        return str(float(value))

    def rinexToMatrixHeader(self, file, header): # Prend en entré le header du rinex et le transfome en commentaires dans un fichier .m
        file.write('% CONVERTED FROM RINEX BY KYLIA GPS TOOLBOX\n')
        file.write('% INPUT RINEX VERSION: '+header['RINEX_version']+'\n')
        file.write('% INPUT FILE TYPE: '+header['file_type']+'\n')
        file.write('% SATELLITE SYSTEM USED: '+header['satellite_system']+'\n')
        file.write('% RINEX CREATION DATE: '+header['creation_date']+'\n')
        file.write('% MARKER NAME: '+header['marker_name']+'\n')
        file.write('% MARKER NUMBER: '+header['marker_number']+'\n')
        file.write('% OBSERVER: '+header['observer']+' AGENCY: '+header['header']+'\n')
        file.write('% RECEIVER NUMBER: '+header['receiver_number']+' RECEIVER TYPE: '+header['receiver_type']+' RECEIVER VERSION: '+header['receiver_version']+'\n')
        file.write('% ANTENNA NUMBER: '+header['antenna_number']+' ANTENNA TYPE: '+header['antenna_type']+'\n')
        file.wrtie('% APPROX. POS. X: '+header['approx_position_x']+' APPROX. POS. Y: '+header['approx_position_y']+' APPROX. POS. Z: '+header['approx_position_z']+'\n')
        file.write('% ANTENNA DELTA H: '+header['antenna_delta_h']+' ANTENNA DELTA E: '+header['antenna_delta_e']+' ANTENNA DELTA N: '+header['antenna_delta_n']+'\n')
        file.write('% WAVELENGTH FACTORY L1'+header['wavelength_factory_L1']+' WAVELENGTH FACTORY L2: '+header['wavelength_factory_L2']+'\n')
        file.write('% OBSERVATION NUMBER: '+header['observation_number']+' EPOCHS INTERVAL: '+header['interval']+'\n')
        file.write('% FIRST OBS. DATE TIME'+header['time_first_obs_d']+'-'+header['time_first_obs_M']+'-'+header['time_first_obs_y']+' '+header['time_first_obs_H']+':'+header['time_first_obs_m']+':'+header['time_first_obs_s']+' FIRST OBS. TIME SYSTEM: '+header['time_first_obs_TS']+'\n')
        file.write('% LAST OBS. DATE TIME'+header['time_last_obs_d']+'-'+header['time_last_obs_M']+'-'+header['time_last_obs_y']+' '+header['time_last_obs_H']+':'+header['time_last_obs_m']+':'+header['time_last_obs_s']+' LAST OBS. TIME SYSTEM: '+header['time_last_obs_TS']+'\n')
        file.write('% IS RECEIVER CLOCK OFFSET ALREADY APPLIED: '+header['receiver_clock_offset_applied']+'\n')
        file.write('% LEAP SECONDS: '+header['leap_seconds']+'\n')
        file.write('% NUMBER OF SAT: '+header['number_of_sat']+'\n')

