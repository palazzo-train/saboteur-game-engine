import numpy as np
import os 
from enum import Enum
import networkx as nx
from . import route_card
from .game_map import GameMap

card_path = r'D:\my_project\saboteur\assets\route-cards'
N_ROWS = 15
N_COLS = 13

class PlaceResult(Enum):
    Card_exist = 1
    bee = 2
    cat = 3


class GameEnv():
    def init(self):
        self.cards, self.cards_dict = route_card.read_all_route_cards(card_path)
        self.game_graph = nx.Graph()
        self.map = np.zeros( [N_ROWS,N_COLS], dtype=int)


        ###### debug
        r = 4
        c = 5
        c_id = 210
        self.map[r,c] = c_id
        card = self.cards_dict[c_id]
        self.game_graph = self._add_card_to_graph(self.game_graph, card)
        ###### debug

    def test_place_route_card(self,card_id, row, col):
        card = self.cards_dict[card_id]

        if self.map[row,col] != 0 :
            return PlaceResult.Card_exist

        ### place 
        test_g = self.game_graph.copy()
        test_g = self._place_route_card_trial_graph(test_g, card, row, col)

        return test_g

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

        print(f'connecting {center_side_node} <--> {adj_side_node}')

        g.add_edge(center_side_node, adj_side_node)

    def _place_route_card_trial_graph(self,temp_g, card, row, col):
        test_g = nx.algorithms.operators.binary.compose(temp_g, card.g)

        ### connecting 4 sides
        for i in range(0,4):
            rr , cc = self._get_adjacent_coordinate(row, col, i)
            c_id = self.map[rr,cc]

            if c_id != 0 :
                adj_card = self.cards_dict[c_id]
                test_g = self._add_card_to_graph(test_g, adj_card)
                self._connecting_route_cards(test_g, card, adj_card, i)

        return test_g

        




