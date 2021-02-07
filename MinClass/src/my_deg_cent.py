import networkx
def in_degree_centrality_weight(G,weight=None):
    if len(G) <= 1:
        return {n: 1 for n in G}

    # s = 1.0 / (len(G) - 1.0)
    centrality = {}
    for n in G:
        n_sum_weight = 0
        for in_edge in G.in_edges(n):
            n_sum_weight = n_sum_weight + G.get_edge_data(in_edge[0],in_edge[1])['weight']
        centrality[n] = n_sum_weight
    return centrality

def out_degree_centrality_weight(G,weight=None):
    if len(G) <= 1:
        return {n: 1 for n in G}

    # s = 1.0 / (len(G) - 1.0)
    centrality = {}
    for n in G:
        n_sum_weight = 0
        for out_edge in G.out_edges(n):
            n_sum_weight = n_sum_weight + G.get_edge_data(out_edge[0],out_edge[1])['weight']
        centrality[n] = n_sum_weight
    return centrality

def degree_centrality_weight(G,weight=None):
    if len(G) <= 1:
        return {n: 1 for n in G}

    # s = 1.0 / (len(G) - 1.0)
    centrality = {}
    for n in G:
        n_sum_weight = 0
        for in_edge in G.in_edges(n):
            n_sum_weight = n_sum_weight + G.get_edge_data(in_edge[0],in_edge[1])['weight']
        for out_edge in G.out_edges(n):
            n_sum_weight = n_sum_weight + G.get_edge_data(out_edge[0],out_edge[1])['weight']
        centrality[n] = n_sum_weight
    return centrality

def degree_centrality_undirected_weight(G,weight=None):
    if len(G) <= 1:
        return {n: 1 for n in G}
    # s = 1.0 / (len(G) - 1.0)
    centrality = {}
    for n in G:
        n_sum_weight = 0
        for edge in G.edges(n):
            n_sum_weight = n_sum_weight + G.get_edge_data(edge[0],edge[1])['weight']
        centrality[n] = n_sum_weight
    return centrality
