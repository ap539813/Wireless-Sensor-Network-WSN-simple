#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:33:55 2020

@author: ankush
"""
from Distance import *
def Con_CH_Avg_Eres(head_nos, population, node_dict, BS_loc, d0):
    avg = 0
    for i in range(head_nos):
        d = distance(node_dict[population[i]].loc, BS_loc)
        if d <= d0:
            avg += node_dict[population[i]].eng
    return avg/head_nos
