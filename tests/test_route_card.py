import engine.engine as engine
import engine.route_card as RC 
import engine.ladder_card as LC 

def test_loading():

    env = engine.GameEnv()

    env.init()
    assert(True)

def test_read_card():
    asset_path = engine.get_asset_path()

    cards_dict = RC.read_all_route_cards(asset_path)

    print(len(cards_dict))

    def print_card(card):
        print('card ' + card.filename)
        print(card.route_code_list)
        print(card.g.edges)
        print(card.g.nodes)
        print()

    for card_id in cards_dict:
        card = cards_dict[card_id]
        print_card(card)

    assert(True)

def test_start_card():
    asset_path = engine.get_asset_path()

    print('start ...')
    print(asset_path)

    card_id , card = LC.init_start_card(asset_path)

    print(card_id)
    print(card.g.nodes)
    print(card.g.edges)
