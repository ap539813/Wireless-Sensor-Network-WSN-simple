#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:58:53 2020

@author: ankush
"""

def Std_Erec(head_nos, population, node_dict, BS_loc, Avg_Eres):
    avg = 0
    for i in range(head_nos):
        avg += (node_dict[population[i]].eng - Avg_Eres)**2
    return (avg/head_nos)**0.5
