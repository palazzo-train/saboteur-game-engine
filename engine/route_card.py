import os, glob
import networkx as nx
import itertools as it

from .base_route_card import BaseRouteCard

###
###  0 = N, 1 = E, 2 = S, 3 = W
###
### 12 nodes , ex. in the north, 
###                open0 : outmost inteface
###                block0 : outmost inteface leads to block
###                no0: card with no path in north . i.e. open0 ->no0
###                 
###
###
class RouteCard(BaseRouteCard):

    def create_nodes(self):
        g = self.g 

        for i in range(0,4):
            node_name = self.get_node_name_open(i)
            g.add_node(node_name)

            node_name = self.get_node_name_block(i)
            g.add_node(node_name)

            node_name = self.get_node_name_invalid(i)
            g.add_node(node_name)

    def create_edges(self):
        ## create edges
        for e_set in self.route_code_list:
            for e in it.combinations(e_set, 2):
                node1 = e[0]
                node2 = e[1]

                node_name1 = self.get_node_name_open(node1)
                if node2 == 'b' :
                    node_name2 = self.get_node_name_block(node1)
                else:
                    node_name2 = self.get_node_name_open(node2)

                self.g.add_edge( node_name1, node_name2)

    def create_invalid_end(self):
        for i in range(0,4):
            node_name = self.get_node_name_open(i)
            count = len( list(self.g.neighbors(node_name)))
            if count == 0 :
                node_name1 = self.get_node_name_open(i)
                node_name2 = self.get_node_name_invalid(i)
                self.g.add_edge( node_name1, node_name2)


    def create_graph(self):
        self.g = nx.Graph()
        self.create_nodes()
        self.create_edges()
        self.create_invalid_end()


    def __init__(self, filepath, filename, card_type, card_id, route_code_list):
        super(RouteCard, self).__init__(filepath, filename, card_type, card_id, route_code_list)

        self.create_graph()



def read_all_route_cards(asset_path):
    card_path = os.path.join(asset_path, 'route-cards')
    path = os.path.join(card_path, '*')

    cards = []
    cards_dict = {}

    for ff in glob.glob(path):
        filename = os.path.basename(ff)
        prefix , card_id , route_code_list = BaseRouteCard.parse_filename(filename)

        c = RouteCard(ff, filename, prefix, card_id, route_code_list)
        cards.append(c)
        cards_dict[card_id] = c

    return cards , cards_dict
