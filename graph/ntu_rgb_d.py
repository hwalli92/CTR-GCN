import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools

#num_node = 25
#self_link = [(i, i) for i in range(num_node)]
inward_ori_index_ntu = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
                        (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
                        (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
                        (20, 19), (22, 23), (23, 8), (24, 25), (25, 12)]

inward_ori_index_nt = [(4, 3), (3, 5), (2, 5), (1, 2), (6, 5), (7, 6), (8, 7),
                       (9, 8), (10, 5), (11, 10), (12, 11), (13, 12), (14, 4),
                       (15, 14), (16, 15), (17, 4), (18, 17), (19, 18)]

#inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]
#outward = [(j, i) for (i, j) in inward]
#neighbor = inward + outward

class Graph:
    def __init__(self, num_node=25, graph='ntu', labeling_mode='spatial'):
        self.num_node = num_node
        self.self_link = [(i, i) for i in range(self.num_node)]
        self.inward_ori_index = inward_ori_index_ntu if graph == 'ntu' else inward_ori_index_nt
        self.inward = [(i - 1, j - 1) for (i, j) in self.inward_ori_index]
        self.outward = [(j, i) for (i, j) in self.inward]
        self.neighbor = self.inward + self.outward
        self.A = self.get_adjacency_matrix(labeling_mode)

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(self.num_node, self.self_link, self.inward, self.outward)
        else:
            raise ValueError()
        return A
