#! /usr/bin/python
# -*- coding: utf-8 -*-
# Mohamed Amjad LASRI pour KYLIA

def cropIntValue(value): # Éliminer les espaces en plus dans les str qui doivent être exploité comme int ou float
    return str(int(value))

def cropFloatValue(value):
    return str(float(value))
