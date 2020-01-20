# -*- coding: utf-8 -*-
from Distance import *
def Std_Con_Avg__Eres(head_nos, population, node_dict, BS_loc, Con_CH_Avg_Eres, d0):
    avg = 0
    for i in range(head_nos):
        d = distance(node_dict[population[i]].loc, BS_loc)
        if d <= d0:
            avg += (node_dict[population[i]].eng - Con_CH_Avg_Eres)**2
    return (avg/head_nos)**0.5
