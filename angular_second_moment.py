#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:43:15 2018

@author: rohit
"""
import numpy as np

def angular_second_moment(cdtm1):
    result=0
    for i in range (np.shape(cdtm1,0)) :
        for j in range (np.shape(cdtm1,1)):
            result=result+cdtm1[i][j]**2
    return result