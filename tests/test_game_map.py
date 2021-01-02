# from unittest.mock import patch 
import pytest 
import networkx as nx
import engine.engine as engine
import engine.route_card as route_card

from matplotlib import pyplot as plt

def test_game_map_init():

    card_path = engine.get_asset_path()

    g = nx.Graph()
    cards_dict = route_card.read_all_route_cards(card_path)

    test_g = g.copy()

    card1 = cards_dict[201]
    card2 = cards_dict[210]
    print(card1.filename)
    print(card2.filename)
    test_g = nx.algorithms.operators.binary.compose(g, card1.g)
    test_g2 = nx.algorithms.operators.binary.compose(test_g, card2.g)

    



    assert(True)