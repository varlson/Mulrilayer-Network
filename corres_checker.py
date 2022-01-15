# from typing import Sequence   
# import pandas as pd
from igraph import *
# import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr
from exporter import *
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
        sper = coord[2]
        corr = "{:.8f}".format(sper[0])
        pval = "{:.8f}".format(sper[1])
        plt.plot(x, y, label=labels[index]+' sp: '+corr+' pv: '+pval, marker="1")
    
    plt.legend()
    plt.title(name)
    plt.savefig('output/'+name+'.png')



def sort_by_metric(graph, metric, name):
    # import sys
    # try:
    #     peso = graph.es['weight']
    # except:
    #     print(graph)
    #     sys.exit(1)
    peso = graph.es['weight']
    peso = [0.001 if x <= 0 else x for x in peso]
    
    weighted =[]
    if metric == "strength":
        weighted =  graph.strength(weights=peso)
    else:
        # print(peso)
        weighted =  graph.betweenness(weights=peso)


    switcher = {

        "degree": [(x, graph.degree(x), graph.vs['label'][x]) for x in range(graph.vcount())],
        "betweenness": [(x, graph.betweenness(x), graph.vs['label'][x]) for x in range(graph.vcount())],
        "strength": [(index, x, graph.vs['label'][index]) for index, x in enumerate(weighted)],
        "betweenness_w": [(index, x, graph.vs['label'][index]) for index, x in enumerate(weighted)]    
    }
    

    done = switcher.get(metric)
    done = sorted(done, key=lambda data: data[1], reverse=True)
    export_sorted_to_csv(done, metric+'_'+name)
    # print(len(done))
    return done
    

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


def mapper(mobility, sort_by_metr, name):

    mob_list = np.arange(len(mobility))
    lab_list = [-1]*len(mobility)
    lab_list = np.asarray(lab_list)
    label = [x[2] for x in sort_by_metr]

    for index, mob, in enumerate(mobility):
        
        try:
            ind = label.index(mob)
            lab_list[index] = ind
        except:
            pass
    
    export_corres_checker((mob_list.copy(), lab_list.copy()), name)
    return spearmanr(mob_list, lab_list)


mob = load_csv('fluvial_by_death')
fl = load_graph_ml('fluvial')