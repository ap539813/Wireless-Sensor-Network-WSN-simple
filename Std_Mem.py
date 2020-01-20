#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:34:32 2020

@author: ankush
"""

def Avg_Mem(n, head_nos):
	return n//head_nos

def Std_Mem(node_dict, population, n, head_nos):
	Std_mem = 0
	avg = Avg_Mem(n, head_nos)
	for i in range(head_nos):
		Std_mem += (len(node_dict[population[i]].members) - avg)**2
	return (Std_mem / head_nos)**0.5