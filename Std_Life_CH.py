#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 14:03:33 2020

@author: ankush
"""

def Std_Life_CH(node_dict, population, n, head_nos, Avg_Life_CH, Avg_transmission_power):
	Std_mem = 0
	for i in range(head_nos):
		Std_mem += (node_dict[population[i]].eng / Avg_transmission_power - Avg_Life_CH)**2
	return (Std_mem / head_nos)**0.5
