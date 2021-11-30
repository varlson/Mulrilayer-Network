import numpy as np 
from igraph import *
import pandas as pd
from main import load_csv, load_graph_ml, sort_by_metric, graphPloter

def intersec(l1, l2):
    return [x for x in l1 if x in l2]

def first_n_nodes(n, g, sorted_data):
    n_nodes = []

    for node in sorted_data[:n]:
        n_nodes.append(g.vs['label'][node[0]])

    return n_nodes

def to_string_list(data):
    temp=[]

    for d in data:
        temp.append(str(d))
    return temp


def correspondence_checker(mobolity, sorted_data, graph):
    list_of_correspondence = []
    for index, city in enumerate(mobolity):
        n_nodes = first_n_nodes(index+1, graph, sorted_data)

        temp = mobolity
        temp = to_string_list(temp)
        inters = intersec(n_nodes, temp[:index+1])
        list_of_correspondence.append(float(len(inters)/(index+1)))  
    return list_of_correspondence


name = "terrestrial_by_death"
g_fluvial = load_graph_ml('terrestrial')
# fluvial = load_csv('terrestrial_sorted_covid_deaths_by_cities_BR')
fluvial = load_csv('terrestrial_sorted_covid_deaths_by_cities_BR')

deg = sort_by_metric(g_fluvial, "degree")
bet = sort_by_metric(g_fluvial, "betweenness")
stre = sort_by_metric(g_fluvial, "strength")
bet_w = sort_by_metric(g_fluvial, "betweenness_w")

pair = []
x_axis = [x for x in range(g_fluvial.vcount())]

corresp = correspondence_checker(fluvial['city'], deg, g_fluvial)
pair.append((x_axis, corresp))
corresp = correspondence_checker(fluvial['city'], bet, g_fluvial)
pair.append((x_axis, corresp))

corresp = correspondence_checker(fluvial['city'], stre, g_fluvial)
pair.append((x_axis, corresp))


corresp = correspondence_checker(fluvial['city'], bet_w, g_fluvial)
pair.append((x_axis, corresp))

graphPloter(pair, ["$k$", "$b$", "$s$", "$b_{w}$"], name)
