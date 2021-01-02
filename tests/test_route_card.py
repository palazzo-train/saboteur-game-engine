import engine.engine as engine
import engine.route_card as RC 
import engine.ladder_card as LC 

def test_loading():

    env = engine.GameEnv()

    env.init()
    assert(True)

def test_read_card():
    asset_path = engine.get_asset_path()

    cards , cards_dict = RC.read_all_route_cards(asset_path)

    print(len(cards))

    def print_card(card):
        print('card ' + card.filename)
        print(card.route_code_list)
        print(card.g.edges)
        print(card.g.nodes)
        print()

    for card in cards:
        print_card(card)

    assert(True)

def test_start_card():
    asset_path = engine.get_asset_path()

    print('start ...')
    print(asset_path)

    cards , cards_dict = LC.init_start_card(asset_path)

    print(cards)
