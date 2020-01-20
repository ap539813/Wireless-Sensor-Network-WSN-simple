#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:29:42 2020

@author: ankush
"""

def Avg_Eres(node_dict, population, head_nos):
	avg = 0
	for i in range(head_nos):
		avg += node_dict[population[i]].eng
	return avg / head_nos