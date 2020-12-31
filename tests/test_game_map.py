# from unittest.mock import patch 
import pytest 
import networkx as nx
import engine.engine as engine
import engine.route_card as route_card
from engine.game_map import GameMap 

from matplotlib import pyplot as plt

def test_game_map_init():

    card_path = r'D:\my_project\saboteur\assets\route-cards'

    g = nx.Graph()
    cards , cards_dict = route_card.read_all_route_cards(card_path)

    map = GameMap()

    test_g = g.copy()

    card1 = cards[0]
    card2 = cards[10]
    print(card1.filename)
    print(card2.filename)
    test_g = nx.algorithms.operators.binary.compose(g, card1.g)
    test_g2 = nx.algorithms.operators.binary.compose(test_g, card2.g)

    



    assert(True)