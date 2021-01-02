import os
import glob
import networkx as nx

from .base_route_card import BaseRouteCard

class StartCard(BaseRouteCard):
    def __init__(self, filepath, filename, card_type, card_id, route_code_list):
        super(StartCard, self).__init__(filepath, filename, card_type, card_id, route_code_list)

        self.create_graph()

    def create_graph(self):
        self.g = nx.Graph()
        self.create_nodes()

    def create_nodes(self):
        g = self.g 

        for i in range(0,4):
            node_name = self.get_node_name_open(i)
            g.add_node(node_name)

            node_name = self.get_node_name_invalid(i)
            g.add_node(node_name)


def init_start_card(asset_path):
    card_path = os.path.join(asset_path, 'start-card')
    path = os.path.join(card_path, '*')

    for ff in glob.glob(path):
        filename = os.path.basename(ff)
        prefix , card_id , route_code_list = BaseRouteCard.parse_filename(filename)

        c = StartCard(ff, filename, prefix, card_id, route_code_list)

        return card_id, c 