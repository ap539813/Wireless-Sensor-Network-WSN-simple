#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:15:17 2020

@author: ankush
"""

# all the measurements are in meters
import numpy
import random
from Average_Eres import *
from Average_life_CH import *
from Average_transmission_pwr import *
from Avg_Dist_BS import *
from Avg_Dist_CH import *
from BS_connectivity import *
from Con_CH_Avg_Eres import *
from DisCon_CH_Avg_Eres import *
from Distance import *
from Max_Dist_Bs import *
from Percent_Coverage import *
from Std_Eres import *
from Std_Con_CH_Avg__Eres import *
from Std_DisCon_CH_Avg__Eres import *
from Std_Eres import *
from Std_Life_CH import *
from Std_Pow import *
from Std_Mem import *
from Std_Erec import *
from promethee import *
from AHP import *
from TOPSIS import *
# from Distance import *
d0 =87.705
Eelec = 1
Efs = 1
Eamp = 1
class node(object):
	def __init__(self, id, ip, loc):
		self.ip = ip
		self.eng = 3.7
		self.loc = loc
		self.id = id
		self.type = 'head'
		self.admin = id
		self.members = [id]
	def update_eng(self, eng):
		self.eng = eng
	def cluster(self, type):
		self.type = type
n = 100 #int(input("enter the no of nodes"))
size = 200
node_dict = {}
arr1 = numpy.random.rand(1000,) * size
arr2 = numpy.random.rand(1000,) * size
arr3 = numpy.random.rand(1000,) * size

base = (50, 50, 50)
for i in range(n):
    node_dict[i] = node(str(i), "192.168.4." + str(i), (arr1[i], arr2[i], arr3[i]))
head_nos = 10 #int(input("enter the number of clusters"))
# for i in range(n):
# 	node_dict[i] = node(str(i), "192.168.4." + str(i), tuple(map(int, input("enter location of node " + str(i)).split())))


population_count = 20 #int(input("enter the population count"))

populations = {i:random.sample(range(0, n), head_nos) for i in range(population_count)}

def Avg_Mem(n, head_nos):
	return n//head_nos
dataset = []
for i in range(population_count):
    x = []
    x.append(CH_coverage(populations[i], d0, n, head_nos, node_dict))
    x.append(BS_connectivity(populations[i], d0, n, head_nos, node_dict))
    e = Avg_Eres(node_dict, populations[i], head_nos)
    x.append(e)
    x.append(Std_Eres(node_dict, populations[i], head_nos, e))
    x.append(Std_Mem(node_dict, populations[i], n, head_nos))
    a = Avg_transmission_power(node_dict, populations[i], head_nos, base, d0, Eelec, Efs, Eamp)
    b = Avg_Life_CH(node_dict, populations[i], n, head_nos, a)
    x.append(b)
    x.append(Std_Life_CH(node_dict, populations[i], n, head_nos, b, a))
    x.append(Max_Dist_BS(populations[i], head_nos, node_dict, base))
    x.append(Avg_Dist_CH(n, node_dict))
    x.append(Avg_Dist_BS(head_nos, populations[i], node_dict, base))
    c = Con_CH_Avg_Eres(head_nos, populations[i], node_dict, base, d0)
    x.append(c)
    d = DisCon_CH_Avg_Eres(head_nos, populations[i], node_dict, base, d0)
    x.append(d)
    x.append(Std_Con_Avg__Eres(head_nos, populations[i], node_dict, base, c, d0))
    x.append(Std_Con_Avg__Eres(head_nos, populations[i], node_dict, base, d, d0))
    x.append(Std_Erec(head_nos, populations[i], node_dict, base, e))
    x.append(Std_Pow(head_nos, populations[i], node_dict, base, a, d0, Eelec, Efs, Eamp))
    dataset.append(x)
#print(populations)
# print(dataset)
# dataset = np.array(dataset).transpose()

# for i in dataset:
#     i = i / (sum(i**2))**0.5
Weight_mat = list(map(float, "0.115384615384615 0.0897435897435897 0.0769230769230769 0.0769230769230769 0.0128205128205128 0.0128205128205128 0.0641025641025641 0.115384615384615 0.115384615384615 0.0128205128205128 0.0641025641025641 0.0128205128205128 0.0769230769230769 0.115384615384615 0.0128205128205128 0.0256410256410256".split()))
numpy.savetxt("foo.csv", dataset, delimiter=",")

print(TOPSIS(dataset, Weight_mat))
print(promethee(dataset, Weight_mat))
print(AHP(dataset, Weight_mat))




