#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:20:28 2020

@author: ankush
"""
import numpy as np
def AHP(dataset, Weight_mat):
    weight = np.array(list(map(float, "0.123288 0.095890 0.082192 0.123288 0.013699 0.013699 0.068493 0.123288 0.068493 0.013699 0.068493 0.013699 0.013699 0.041096 0.123288 0.013699".split())))
    
    benific = np.array([1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0])
    dataset = np.array(dataset)
    for i in range(len(dataset[0])):
        if benific[i] == 1:
            dataset[:, i] = dataset[:, i]/(max(dataset[:, i]) + 0.000000001)
        else:
            dataset[:, i] = min(dataset[:, i])/(dataset[:, i] + 0.00000001)
#     np.savetxt("foo.csv", dataset, delimiter=",")
    final = {}
    for i in range(len(dataset)):
        final[sum(dataset[i] * weight)] = i
        
    return final[sorted(final)[0]]
    
    
    
# 14, 19, 4    
    