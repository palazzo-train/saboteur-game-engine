import os, glob
import networkx as nx
import itertools as it

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
class RouteCard():
    def get_node_name_open(self, i):
        node_name = self.node_prefix + 'open:' + str(i)

        return node_name

    def get_node_name_block(self, i):
        node_name = self.node_prefix + 'block:' + str(i)

        return node_name

    def get_node_name_dead(self, i):
        node_name = self.node_prefix + 'dead:' + str(i)

        return node_name

    def create_nodes(self):
        g = self.g 

        for i in range(0,4):
            node_name = self.get_node_name_open(i)
            g.add_node(node_name)

            node_name = self.get_node_name_block(i)
            g.add_node(node_name)

            node_name = self.get_node_name_dead(i)
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

    def create_dead_end(self):
        for i in range(0,4):
            node_name = self.get_node_name_open(i)
            count = len( list(self.g.neighbors(node_name)))
            if count == 0 :
                node_name1 = self.get_node_name_open(i)
                node_name2 = self.get_node_name_dead(i)
                self.g.add_edge( node_name1, node_name2)


    def create_graph(self):
        self.g = nx.Graph()
        self.create_nodes()
        self.create_edges()
        self.create_dead_end()


    def __init__(self, filepath, filename, card_type, card_id, route_code_list):
        self.filepath = filepath
        self.filename = filename
        self.card_type = card_type
        self.card_id = card_id
        self.route_code_list = route_code_list
        self.node_prefix = f'{self.card_type}-id:{str(self.card_id).zfill(4)}-'

        self.create_graph()

def parse_filename(filename):
    fobj = filename.split('_')
    prefix = fobj[0]
    card_id_str = fobj[1]
    
    card_id = int(card_id_str[2:])
    path_route = fobj[2].split('.')[0]
    route_code_list = (path_route[1:].split('-'))
    
    return prefix , card_id , route_code_list

def read_all_route_cards(card_path):
    path = os.path.join(card_path, '*')

    cards = []
    cards_dict = {}

    for ff in glob.glob(path):
        filename = os.path.basename(ff)
        prefix , card_id , route_code_list = parse_filename(filename)

        c = RouteCard(ff, filename, prefix, card_id, route_code_list)
        cards.append(c)
        cards_dict[card_id] = c

    return cards , cards_dict
