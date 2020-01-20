#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 07:28:44 2020

@author: ankush
"""
def distance(a, b):
	return ((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)**0.5
def CH_coverage(population, d0, n, head_nos, node_dict):
	count = 0
	for i in range(n):
		min = 99999999
		for j in range(head_nos):
			dist = distance(node_dict[population[j]].loc, node_dict[i].loc)
			if dist < min:
				min = dist
				node_dict[i].admin = int(node_dict[population[j]].id)
		if min < d0:
			count += 1
		node_dict[population[j]].members.append(i)
	return count * 100 / n
