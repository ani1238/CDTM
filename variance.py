#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:56:42 2018

@author: rohit
"""
import numpy as np

def varianceX(cdtm1):
    result=0
    (rows,columns)=np.shape(cdtm1)
    for i in range (rows):
        result=result+((i-meanX)**2)*rowSum[i]