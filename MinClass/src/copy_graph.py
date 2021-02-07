#coding:utf-8
import networkx

def copy_undirected_graph(graph):
    """
    将无向图复制成新的图
    :param graph:
    :return:
    """
    new_graph = networkx.Graph()
    nodes = graph.nodes
    edges = graph.edges
    for node in nodes:
        new_graph.add_node(node)
    for edge in edges:
        weight = graph.get_edge_data(edge[0],edge[1])[0]['weight']
        new_graph.add_edge(edge[0],edge[1],weight=weight)
    return new_graph

def copy_directed_graph(graph):
    new_graph = networkx.DiGraph()
    nodes = graph.nodes
    edges = graph.edges
    for node in nodes:
        new_graph.add_node(node)
    for edge in edges:
        weight = graph.get_edge_data(edge[0],edge[1])[0]['weight']
        new_graph.add_edge(edge[0],edge[1],weight=weight)
    return new_graph