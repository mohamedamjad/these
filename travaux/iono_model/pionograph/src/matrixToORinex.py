#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI

class MatrixToRinex:
    def __init__():
        print 'OK'

    def matrixToORinexHeader():
        print 'A FAIRE'

    def epochToRinex(self, rinex, epoch):
        # Ajouter une epoch à un RINEX deja prérempli

    def matrixToORinex(self, file, sep, comment):
        for line in file.readlines():
            if comment in line:
                if 'FORMAT' in line:
                    keys=line.split(':')[1].split(sep) # TODO
                next
            else:
                epoch_key=line.split(sep)[0] # Clef de l'epoch
                if len(keys) != len(line.splite(sep)):
                    # CRITIQUE PROBLEM LOG QUAND LE HEADER NE CORRESPOND PAS
                    # AU NOMBRE DE COLONES
                if len(line.splite(sep)) > 12: # C'est un L1+L2
                    epochs[epoch_key]={ 'PRN':line.splite(sep)[1],
                                        'L1':line.splite(sep)[2],
                                        'L1LLI':line.splite(sep)[3],
                                        'L1SSI':line.splite(sep)[4],
                                        'L2':line.splite(sep)[5],
                                        'L2LLI':line.splite(sep)[6],
                                        'L2SSI':line.splite(sep)[7],
                                        'P1':line.splite(sep)[8],
                                        'P1SSI':line.splite(sep)[9],
                                        'P2':line.splite(sep)[10],
                                        'P2SSI':line.splite(sep)[11],
                                        'C1':line.splite(sep)[12],
                                        'C1SSI':line.splite(sep)[13],
                                        'S1':line.splite(sep)[14],
                                        'S2':line.splite(sep)[15]
                    }
                else: # Juste L1
                     epochs[epoch_key]={'PRN':line.splite(sep)[1],
                                        'L1':line.splite(sep)[2],
                                        'L1LLI':line.splite(sep)[3],
                                        'P1':line.splite(sep)[4],
                                        'P1SSI':line.splite(sep)[5],
                                        'C1':line.splite(sep)[6],
                                        'C1SSI':line.splite(sep)[7],
                                        'S1':line.splite(sep)[8]
                     }
