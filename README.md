# Introduction
This is the replication package for our work published by IEEE ACCESS, i.e., Hao Li, Tian Wang, Weifeng Pan, Muchou Wang, Chunlai Chai, Pengyu Chen, Jiale Wang, Jing Wang. Mining Key Classes in Java Projects by Examining a Very Small Number of Classes: A Complex Network based Approach. IEEE Access, 2021, 9: 28076-28088. [[PDF](https://ieeexplore.ieee.org/document/9351963)]

Author Contributions: Hao Li performed the experiments and analyzed the data. Hao Li and Tian Wang wrote the paper. Weifeng Pan conceived of the idea. Other authors proofread the paper. All authors have read and approved the final manuscript.

# CCNs
The CCNs directory contains the CCNs that we built for all the subject systems used in our experiments.
The CCNs have the following format:
source_node1 target_node1 weight1
source_node2 target_node2 weight2
source_node3 target_node3 weight3
source_node4 target_node4 weight4
....

The files with suffix "-kc.txt" contain the key classes in the corresponding system. They have the following format:
"node number in the corresponding CCN" "name of the key class"
....

# MinClass
The MinClass directory contains the Python code which implements our MinClass approach and the approaches in the baseline. It is a small part of our own developped software, SNAP. Of course, the SNAP software can be obtained by emailing us (Email: wfpan@zjgsu.edu.cn).

# Cite our work
If you use our data set or tool, please cite our work.

Hao Li, Tian Wang, Weifeng Pan, Muchou Wang, Chunlai Chai, Pengyu Chen, Jiale Wang, Jing Wang. Mining Key Classes in Java Projects by Examining a Very Small Number of Classes: A Complex Network based Approach. IEEE Access, 2021, 9: 28076-28088. [[PDF](https://ieeexplore.ieee.org/document/9351963)]

Weifeng Pan, Beibei Song, Kangshun Li, Kejun Zhang. Identifying Key Classes in Object-Oriented Software using Generalized k-Core Decomposition. Future Generation Computer Systems, 2018, 81: 188-202. 

Weifeng Pan, Bing Li, Jing Liu, Yutao Ma, Bo Hu. Analyzing the structure of Java software systems by weighted k-core decomposition. Future Generation Computer Systems, 2018, 83: 431-444.

