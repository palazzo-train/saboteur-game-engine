import logging
import numpy as np
import os 
from enum import Enum
import networkx as nx
import os
from . import route_card as RC
from . import ladder_card as LC
from .assets import assets as assets

# card_path = r'..\assets\route-cards'
N_ROWS = 15
N_COLS = 13

class PlaceResult(Enum):
    Card_exist = 1
    Invalid = 2
    Success = 3
    Out_of_bound = 4
    No_path_to_ladder = 5

def get_asset_path():
    # card_path = r'..\assets\route-cards'
    asset_path = os.path.abspath(assets.__file__)
    asset_dir = os.path.dirname(asset_path)

    return asset_dir 

class GameEnv():
    def init(self):

        asset_path =  get_asset_path() 
        self.route_cards_dict = RC.read_all_route_cards( asset_path )
        self.game_graph = nx.Graph()
        self.map = np.zeros( [N_ROWS,N_COLS], dtype=int)

        ### start card
        self.start_card_id, self.start_card = LC.init_start_card(asset_path)
        start_r = 3
        start_c = int(N_COLS / 2 )
        self.map[start_r,start_c] = self.start_card_id
        self.game_graph = self._add_card_to_graph(self.game_graph, self.start_card)

        self.route_cards_dict[self.start_card_id] = self.start_card

        ### all ladder cards
        self.ladder_cards_dict = {}
        self.ladder_cards_dict[self.start_card_id] = self.start_card


    def _check_Invalid(self,g, center_card, row, col):
        Invalid = [ False, False, False, False ]
        for i in range(0,4):
            rr , cc = self._get_adjacent_coordinate(row, col, i)
            c_id = self.map[rr,cc]
            adj_index = self._get_opposite_direction(i)

            if c_id != 0 :
                adj_card = self.route_cards_dict[c_id]
                is_connected = nx.algorithms.shortest_paths.generic.has_path( g, 
                                    center_card.get_node_name_invalid(i), 
                                    adj_card.get_node_name_open(adj_index) ) 
                Invalid[i] = is_connected

        return Invalid

    def _check_has_path_to_ladder(self,g,card):
        for ladder_id in self.ladder_cards_dict :
            ladder_card = self.ladder_cards_dict[ladder_id]

            ladder_node = ladder_card.get_node_name_ladder()

            ### check has path from all direction
            for i in range(0,4):
                is_connected = nx.algorithms.shortest_paths.generic.has_path( g, 
                                    ladder_node,
                                    card.get_node_name_open(i) ) 

                if is_connected:
                    return True

        #### no path to any ladder
        return False

    def test_place_route_card(self,card_id, row, col):
        card = self.route_cards_dict[card_id]

        if self.map[row,col] != 0 :
            return PlaceResult.Card_exist, self.game_graph 

        ### place trial
        test_g = self.game_graph.copy()
        test_g = self._place_route_card_trial_graph(test_g, card, row, col)
        Invalid = self._check_Invalid(test_g, card, row, col)
        if any( Invalid ) :
            return PlaceResult.Invalid, test_g

        if not self._check_has_path_to_ladder(test_g,card) :
            return PlaceResult.No_path_to_ladder, test_g

        return PlaceResult.Success, test_g

    def place_route_card(self,card_id, row, col):
        r , test_g = self.test_place_route_card(card_id, row, col)

        if r != PlaceResult.Success:
            return r

        ## no error, commit change
        self.game_graph = test_g
        self.map[row,col] = card_id

        return PlaceResult.Success

    def _add_card_to_graph(self, g, card):
        return nx.algorithms.operators.binary.compose(g, card.g)

    def _get_adjacent_coordinate(self, center_row, center_col, direction_index):
        row = center_row
        col = center_col

        if direction_index == 0 :
            row = row - 1
        elif direction_index == 1:
            col = col + 1
        elif direction_index == 2:
            row = row + 1
        elif direction_index == 3:
            col = col - 1

        return row , col

    def _get_opposite_direction(self, direction_index):
        if direction_index == 0 :
            return 2
        elif direction_index == 1:
            return 3
        elif direction_index == 2:
            return 0
        elif direction_index == 3:
            return 1

    def _connecting_route_cards(self, g, center_card, adj_card, direction_index):
        center_side_node = center_card.get_node_name_open(direction_index)

        adj_index = self._get_opposite_direction(direction_index)
        adj_side_node = adj_card.get_node_name_open(adj_index)

        logging.info(f'connecting {center_side_node} <--> {adj_side_node}')

        g.add_edge(center_side_node, adj_side_node)

    def _place_route_card_trial_graph(self,temp_g, card, row, col):
        test_g = nx.algorithms.operators.binary.compose(temp_g, card.g)

        ### connecting 4 sides
        for i in range(0,4):
            rr , cc = self._get_adjacent_coordinate(row, col, i)
            c_id = self.map[rr,cc]

            if c_id != 0 :
                adj_card = self.route_cards_dict[c_id]
                test_g = self._add_card_to_graph(test_g, adj_card)
                self._connecting_route_cards(test_g, card, adj_card, i)

        return test_g

        




