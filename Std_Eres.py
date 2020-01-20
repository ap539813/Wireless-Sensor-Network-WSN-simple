#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:33:46 2020

@author: ankush
"""

def Std_Eres(node_dict, population, head_nos, Avg_Eres):
	avg = 0
	for i in range(head_nos):
		avg += (node_dict[population[i]].eng - Avg_Eres)**2
	return (avg / head_nos)**0.5