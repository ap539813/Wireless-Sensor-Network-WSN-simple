#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 01:30:05 2020

@author: ankush
"""

import numpy as np
def promethee(dataset, Weight_mat):
    dataset = np.array(dataset).transpose()
    population_data = []
    for i in range(len(dataset)):
        pop = []
        for j in range(len(dataset[0])):
            pop_row = []
            for k in range(len(dataset[0])):
                pop_row.append(int(dataset[i][j] > dataset[i][k]))
            pop.append(pop_row)
        population_data.append(pop)
    population_data = np.array(population_data)
    
    for i in range(len(population_data)):
        population_data[i] = population_data[i] * Weight_mat[i]
    
    population_data = sum(population_data)
    
    final = {}
    for i in range(len(population_data)):
        final[sum(population_data[i]) - sum(population_data[:, i])] = i
    
    return final[sorted(final)[0]]