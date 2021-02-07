#coding:utf-8
import networkx
from networkx.readwrite import read_pajek
from matplotlib import pyplot

def file_reader(path):
    graph = read_pajek(path)
    return graph

def show_graph(graph):
    edge_labels = networkx.get_edge_attributes(graph,'weight')
    print(edge_labels)
    pos = networkx.spring_layout(graph, k=20.0, iterations=2000, weight='weight')
    networkx.draw_networkx_nodes(graph, pos, node_size=8, with_labels=True)
    networkx.draw_networkx_labels(graph, pos,font_size=5,alpha=0.5)
    # 把边权重画出来
    networkx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=4)
    networkx.draw_networkx_edges(graph, pos, width=0.5, alpha=0.2, edge_color='r')
    # networkx.draw(graph)
    pyplot.show()