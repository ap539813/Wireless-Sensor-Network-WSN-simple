#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:03:29 2020

@author: ankush
"""
from Distance import *
def Max_Dist_BS(population, head_nos, node_dict, BS_loc):
    return max([abs(distance(node_dict[population[i]].loc, BS_loc)) for i in range(head_nos)])