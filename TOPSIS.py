#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 10:33:05 2020

@author: ankush
"""

import numpy as np
def TOPSIS(dataset, Weight_mat):
    dataset = np.array(dataset).transpose()

    for i in range(len(dataset)):
        if dataset[i].all() != np.zeros((dataset[i].shape)).all():
            dataset[i] = dataset[i] / (sum(dataset[i]**2))**0.5
        else:
            pass

    for i in range(len(dataset)):
        dataset[i] *= Weight_mat[i]
    benific = np.array([1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0])
    best_worst = []
    for i in range(len(dataset)):
        if benific[i] == 1:
            best_worst.append([max(dataset[i]), min(dataset[i])])
        else:
            best_worst.append([min(dataset[i]), max(dataset[i])])
    
    best_worst = np.array(best_worst)
    db = []
    for i in range(len(dataset)):
        db.append(sum((dataset[i]-best_worst[i][0])**2)**0.5)
    
    dw = []
    for i in range(len(dataset)):
        dw.append(sum((dataset[i]-best_worst[i][0])**2)**0.5)
        
    final = {}
    for i in range(len(dataset)):
        final[dw[i]/(dw[i] + db[i] + 0.00000001)] = i
        
    return final[sorted(final)[0]]
    
    
    
    