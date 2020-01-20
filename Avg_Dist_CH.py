#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 11:40:24 2020

@author: ankush
"""
from Distance import *
def Avg_Dist_CH(n, node_dict):
    avg = 0
    for i in range(n):
        avg += distance(node_dict[i].loc, node_dict[node_dict[i].admin].loc)
    return avg/n
        