#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:36:30 2020

@author: ankush
"""

def Avg_Life_CH(node_dict, population, n, head_nos, Avg_transmission_power):
	avg = 0
	for i in range(head_nos):
		avg += node_dict[population[i]].eng / Avg_transmission_power
	return avg/head_nos
