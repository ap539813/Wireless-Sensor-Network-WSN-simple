#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:29:44 2020

@author: ankush
"""
def distance(a, b):
	return ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)**0.5
def BS_connectivity(population, d0, n, head_nos, node_dict):
	count = 0
	for i in range(head_nos):
		for j in range(n):
			dist = distance(node_dict[population[i]].loc, node_dict[j].loc)
			if dist < d0:
				count += 1
	return count / head_nos