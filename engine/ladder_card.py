import os
import glob
import networkx as nx
import itertools as it

from .base_route_card import BaseRouteCard

class StartCard(BaseRouteCard):
    def __init__(self, filepath, filename, card_type, card_id, route_code_list):
        super(StartCard, self).__init__(filepath, filename, card_type, card_id, route_code_list)

        self.create_graph()

    def create_graph(self):
        self.g = nx.Graph()
        self.create_nodes()
        self.create_edges()
        self.create_invalid_end()

    def get_node_name_ladder(self):
        node_name = self.node_prefix + 'ladder' 

        return node_name

    def create_nodes(self):
        g = self.g 

        for i in range(0,4):
            node_name = self.get_node_name_open(i)
            g.add_node(node_name)

            node_name = self.get_node_name_invalid(i)
            g.add_node(node_name)
        
        node_name = self.get_node_name_ladder()
        g.add_node(node_name)

    def create_edges(self):
        ## create edges
        for e_set in self.route_code_list:
            for e in it.combinations(e_set, 2):
                node1 = e[0]
                node2 = e[1]

                node_name1 = self.get_node_name_open(node1)
                if node2 == 'b' :
                    raise Exception('Incorrect route code for ladder card')
                else:
                    node_name2 = self.get_node_name_open(node2)

                ladder_node = self.get_node_name_ladder()

                self.g.add_edge( node_name1, ladder_node)
                self.g.add_edge( ladder_node, node_name2)

def init_start_card(asset_path):
    card_path = os.path.join(asset_path, 'start-card')
    path = os.path.join(card_path, '*')

    for ff in glob.glob(path):
        filename = os.path.basename(ff)
        prefix , card_id , route_code_list = BaseRouteCard.parse_filename(filename)

        c = StartCard(ff, filename, prefix, card_id, route_code_list)

        return card_id, c 