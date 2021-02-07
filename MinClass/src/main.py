#coding:utf-8
import networkx
import os
import shutil
from src.copy_graph import copy_directed_graph
from src import my_deg_cent

from src import write_in_csv, ose


def generate_col_name(target_name):
    return target_name

def generate_un(graph):
    """
    Generating undirected graphs
    Generating undirected weighted graphs from directed weighted graphs
    :return:
    """
    un_graph = networkx.Graph()
    nodes = graph.nodes
    for node in nodes:
        un_graph.add_node(node)
    edges = graph.edges
    for edge in edges:
        _weight = graph.get_edge_data(edge[0], edge[1])['weight']
        if un_graph.has_edge(edge[0],edge[1]):
            _old_weight = un_graph.get_edge_data(edge[0],edge[1])['weight']
            _old_weight = _old_weight + _weight
            un_graph.add_edge(edge[0],edge[1],weight=_old_weight)
        else:
            un_graph.add_edge(edge[0],edge[1],weight=_weight)
    return un_graph

def update_weight(graph):
    """
    将边权规格化
    :param graph:
    :return:
    """
    edges = graph.edges()
    weight_set = set()
    for edge in edges:
        weight = graph.get_edge_data(edge[0],edge[1])['weight']
        weight_set.add(weight)
    max_weight = max(weight_set)

    for edge in edges:
        weight = graph.get_edge_data(edge[0],edge[1])['weight']
        graph.add_edge(edge[0],edge[1],weight=weight/max_weight)
    return graph

def main(net_path,data_path):
    """

    :param net_path:
    :param data_path: Data folder path
    :return:
    """
    graph = networkx.read_pajek(net_path)
    graph = copy_directed_graph(graph)

    graph = update_weight(graph)
    edges = graph.edges()

    remove_edges = []
    for edge in edges:
        if edge[0] == edge[1]:
            remove_edges.append(edge)
    for edge in remove_edges:
        graph.remove_edge(edge[0], edge[0])
    un_graph = generate_un(graph)  # 非有向图

    """
    计算HITS
    """
    try:
        data = networkx.hits(graph,max_iter=1000)  #(hubs,authorities)
        col_name = generate_col_name("HITS-auth")
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data[1])
    except Exception as e:
        print(e)

    """
    计算degree
    """
    try:
        col_name = generate_col_name("InDeg")
        data = my_deg_cent.in_degree_centrality_weight(graph, weight='weight')
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)


    try:
        col_name = generate_col_name("OutDeg")
        networkx.effective_size()
        data = my_deg_cent.out_degree_centrality_weight(graph, weight='weight')
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)

    try:
        col_name = generate_col_name("Deg")
        data = my_deg_cent.degree_centrality_weight(graph, weight='weight')
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)

    """
    计算 betweenness
    """
    try:
        col_name = generate_col_name("Between")
        data = networkx.betweenness_centrality(un_graph)
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)

    try:
        col_name = generate_col_name("CoreNum")
        data = networkx.core_number(un_graph)
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)

    try:
        col_name = generate_col_name("PR")
        data = networkx.pagerank(graph,weight='weight')
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)

    try:
        col_name = generate_col_name("MinClass")
        data = ose.compute_H(graph, weight='weight')
        write_file(csv_file_name="Ant_new_wccn_SoftNet.csv", whole_path=data_path, col_name=col_name, data=data)
    except Exception as e:
        print(e)


def write_file(csv_file_name,whole_path,col_name,data):
    """
        Write data to file
        Use the new file to overlay the old file
    """
    write_in_csv.cvs_file_write(path=whole_path, csv_file_name=csv_file_name, col_name=col_name, data=data)
    shutil.copyfile(whole_path+"data/"+col_name+".csv",whole_path+csv_file_name)

if __name__ == '__main__':
    software_dir_path = "SoftNet/"  #Software network folder
    software_dirs = os.listdir(software_dir_path)
    if ".DS_Store" in software_dirs:
        software_dirs.remove(".DS_Store")
    for software_dir in software_dirs:
        software_path = software_dir_path + software_dir + "/" #data_path
        #Delete useless file names
        file_list = os.listdir(software_path)
        file_list.remove('none_data')
        file_list.remove('.DS_Store')
        file_list.remove('Ant_new_wccn_SoftNet.csv')
        file_list.remove('data')
        net_path = software_path+file_list[0]   #net_path
        print("开始计算：",software_dir)
        # if software_dir == 'jhotdraw':
        main(net_path,software_path)

