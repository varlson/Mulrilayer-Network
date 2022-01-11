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


def correspondence_checker(mobolity, sorted_data, graph, name):
    list_of_correspondence = []
    for index, city in enumerate(mobolity):
        n_nodes = first_n_nodes(index+1, graph, sorted_data)

        temp = mobolity
        temp = to_string_list(temp)
        inters = intersec(n_nodes, temp[:index+1])
        list_of_correspondence.append(float(len(inters)/(index+1))) 
    
    x_axis = [x for x in range(graph.vcount())]

    
    df = {"Nos": x_axis}
    df['Correspondecia'] = list_of_correspondence
    
    df = pd.DataFrame(df, index=False)
    df.to_csv('output/'+name+'.csv')
    return list_of_correspondence




to_process = ['terrestrial', 'terrestrial_by_death']


for process in to_process:
    name = process
    mobility = load_csv(process)
    graph = load_graph_ml('terrestrial')

    deg = sort_by_metric(graph, "degree", name)
    bet = sort_by_metric(graph, "betweenness", name)
    stre = sort_by_metric(graph, "strength", name)
    bet_w = sort_by_metric(graph, "betweenness_w", name)

    _tuple = []
    x_axis = [x for x in range(graph.vcount())]

    corresp = correspondence_checker(mobility['city'], deg, graph, name)
    spear = mapper(mobility['city'], deg, name)
    _tuple.append((x_axis, corresp, spear))

    corresp = correspondence_checker(mobility['city'], bet, graph, name)
    spear = mapper(mobility['city'], bet, name)
    _tuple.append((x_axis, corresp, spear))

    corresp = correspondence_checker(mobility['city'], stre, graph, name)
    spear = mapper(mobility['city'], stre, name)
    _tuple.append((x_axis, corresp, spear))


    corresp = correspondence_checker(mobility['city'], bet_w, graph, name)
    spear = mapper(mobility['city'], bet_w, name)
    _tuple.append((x_axis, corresp, spear))
    
    graphPloter(_tuple, ["$k$", "$b$", "$s$", "$b_{w}$"], name)
