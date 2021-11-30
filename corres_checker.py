# from typing import Sequence   
import pandas as pd
from igraph import *
import numpy as np
import matplotlib.pyplot as plt

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
        
    return seq


def graphPloter(list_of_coord, labels, name="teste"):
    plt.clf()
    for index, coord in enumerate(list_of_coord):
        x = coord[0]
        y = coord[1]

        plt.plot(x, y, label=labels[index], marker="1")
    
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

def mapeador(mobility, graph):

    mob_id = [x  for x in range(len(mobility))]
    mob_id = np.asarray(mob_id)

    g_id =[-1]*len(mobility)
    g_id = np.asarray(g_id)

    g_label = graph.vs['label']

    for index , mob in enumerate(mobility):

        try:
            ind = g_label.index(mob)
            g_id[index] = ind
        except:
            pass
    return[mob_id, g_id]


mob = list(load_csv('fluvial')['city'])
fl = load_graph_ml('fluvial')