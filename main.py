# from typing import Sequence   
import pandas as pd
from igraph import *
import string
import random
import numpy as np
import matplotlib.pyplot as plt
from util import terminal_clear

def comparator(g, sorted, mobility):
    seq = np.array([0.0]*len(mobility))
    isMatch = notMatch =0.0

    size = len(mobility) if len(mobility) < g.vcount() else g.vcount()
    for index in range(size):
        if(mobility[index])== g.vs['label'][sorted[index][0]]:
            isMatch+=1.0
            print('match')
        else:
            notMatch+=1.0
    
        if(notMatch==0):
            seq[index] = 1
        else:
            temp = ((isMatch/notMatch)*100)/100
            seq[index] = 1.0 if temp > 1.0 else temp
        # print(isMatch, notMatch)
        

    return seq

def graphPloter(list_of_coord, labels, name="teste"):
    plt.clf()
    for index, coord in enumerate(list_of_coord):
        x = coord[0]
        y = coord[1]

        plt.plot(x, y, label=labels[index])
    
    plt.legend()
    plt.title(name)
    plt.savefig('output/'+name+'.png')



def sort_by_metric(graph, metric):

    peso = graph.es['weight']
    peso = [0.001 if x <= 0 else x for x in peso]
    
    weighted =[]
    if metric == "strength":
        weighted =  graph.strength(weights=peso)
    else:
        # print(peso)
        weighted =  graph.betweenness(weights=peso)


    switcher = {

        "degree": [(x, graph.degree(x)) for x in range(graph.vcount())],
        "betweenness": [(x, graph.betweenness(x)) for x in range(graph.vcount())],
        "strength": [(index, x) for index, x in enumerate(weighted)],
        "betweenness_w": [(index, x) for index, x in enumerate(weighted)]    
    }
    

    done = switcher.get(metric)
    return sorted(done, key=lambda data: data[1], reverse=True)
    

def load_graph_ml(full_path):
    g =  Graph.Read_GraphML('datas/'+full_path+'.GraphML')
    return g
    
def load_csv(fileName):
    cols = ['code', 'city', 'state', 'other', 'date', 'other2']
    dataFrame = pd.read_csv('datas/'+fileName+'.csv', sep=";", names=cols)
    return dataFrame

def prepare(g,  metric, mobility):

    return comparator(g, (sort_by_metric(g, metric)), mobility)
# def sort_by_metric(graph):
    # pass
# def main(graph):


# lista_of_coord = []
# # lista_of_coord = []
# labels = ['$k$', '$s$', '$b$']
# metric = ['degree', 'strength', 'betweenness']
# g_fluvial = graph_loader('terrestrial')
# fluvial = loader('terrestrial')['city']
# # peso = g_fluvial.es['weight']

# for met in metric:
#     coord = prepare(g_fluvial, met, fluvial)
#     x_axis = [x for x in range(len(coord))]
#     lista_of_coord.append((x_axis, coord))

# graphPloter(lista_of_coord, labels, "terrestrial_cases")
# print(lista_of_coord)