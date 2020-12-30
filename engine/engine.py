import os 
import networkx as nx
from . import route_card

card_path = r'D:\my_project\saboteur\assets\route-cards'

game_map = nx.Graph()

def init():
    cards = route_card.read_all_route_cards(card_path)