#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 12:23:16 2020

@author: ankush
"""
from Distance import *
def Avg_Dist_BS(head_nos, population, node_dict, BS_loc):
    avg = 0
    for i in range(head_nos):
        avg += distance(node_dict[population[i]].loc, BS_loc)
    return avg/head_nos