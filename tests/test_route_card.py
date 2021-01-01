import engine.engine as engine
import engine.route_card as route_card

def test_loading():

    env = engine.GameEnv()

    env.init()
    assert(True)

def test_read_card():
    card_path = engine.get_asset_path()
    cards , cards_dict = route_card.read_all_route_cards(card_path)

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