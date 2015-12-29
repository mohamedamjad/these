#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI

class MatrixToRinex:
    def __init__():
        print 'OK'

    def matrixToORinexHeader():
        print 'A FAIRE'

    def MatrixToORinex(self, file, sep, comment):
        for line in file.readlines():
            if comment in line:
                if 'FORMAT' in line:
                    keys=line.split(':')[1].split(sep)
                next
            else:
                epoch_key=line.split(sep)[0]
                if len(keys) != len(line.splite(sep)):
                    # CRITIQUE PROBLEM LOG
                for i in range(1, len(line.splite(sep))):
                    
