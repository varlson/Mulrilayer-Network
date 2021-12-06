from corres_checker import *

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




to_process = ['fluvial', 'fluvial_by_death', 'terrestrial', 'terrestrial_by_death']


for process in to_process:
    name = process
    mobility = load_csv(process)
    graph = load_graph_ml('fluvial') if process[0]=='f' else load_csv('terrestrial')

    deg = sort_by_metric(graph, "degree")
    bet = sort_by_metric(graph, "betweenness")
    stre = sort_by_metric(graph, "strength")
    bet_w = sort_by_metric(graph, "betweenness_w")

    _tuple = []
    x_axis = [x for x in range(graph.vcount())]

    corresp = correspondence_checker(mobility['city'], deg, graph)
    spear = mapper(mobility['city'], deg)
    _tuple.append((x_axis, corresp, spear))

    corresp = correspondence_checker(mobility['city'], bet, graph)
    spear = mapper(mobility['city'], bet)
    _tuple.append((x_axis, corresp, spear))

    corresp = correspondence_checker(mobility['city'], stre, graph)
    spear = mapper(mobility['city'], stre)
    _tuple.append((x_axis, corresp, spear))


    corresp = correspondence_checker(mobility['city'], bet_w, graph)
    spear = mapper(mobility['city'], bet_w)
    _tuple.append((x_axis, corresp, spear))

    graphPloter(_tuple, ["$k$", "$b$", "$s$", "$b_{w}$"], name)
