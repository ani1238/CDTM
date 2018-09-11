#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:43:15 2018

@author: rohit
"""
import numpy as np

def angular_second_moment(cdtm1):
    result=0
    (rows,columns)=np.shape(cdtm1)
    for i in range (rows) :
        for j in range (columns):
            result=result+cdtm1[i][j]**2
    return result