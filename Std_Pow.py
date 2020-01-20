#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 14:10:38 2020

@author: ankush
"""
from Distance import *
def Std_Pow(head_nos, population, node_dict, BS_loc, Avg_transmission_power, d0, Eelec, Efs, Eamp):
    avg = 0
    for i in range(head_nos):
        d = distance(BS_loc, node_dict[population[i]].loc)
        m = len(node_dict[population[i]].members)
        if d <= d0:
            avg += (m * Eelec + m * Efs * d**2  - Avg_transmission_power)**2
        elif d > d0:
            avg += (m * Eelec + m * Eamp * d**4  - Avg_transmission_power)**2
    return (avg/head_nos)**0.5
