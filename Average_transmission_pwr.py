#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:35:53 2020

@author: ankush
"""
def distance(a, b):
	return ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)**0.5
def Avg_transmission_power(node_dict, population, head_nos, base, d0, Eelec, Efs, Eamp):
    avg = 0
    for i in range(head_nos):
        d = distance(node_dict[population[i]].loc, base)
        m = len(node_dict[population[i]].members)
        if d <= d0:
            avg += m * Eelec + m * Efs * d**2
        elif d > d0:
            avg += m * Eelec + m * Eamp * d**4
    return avg
