import engine.engine as engine
import engine.route_card as RC 
import engine.ladder_card as LC 

def test_invalid_move():

    env = engine.GameEnv()

    env.init()


    start_r = 3
    start_c = 6

    card = env.route_cards_dict[203]
    r = env.place_route_card(203, start_r , start_c + 1)
    print(r)
    assert(True)