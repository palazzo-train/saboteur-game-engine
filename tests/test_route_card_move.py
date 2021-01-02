import engine.game_env.engine as engine
import engine.game_env.route_card as RC 
import engine.game_env.ladder_card as LC 
from engine.game_env.engine import PlaceResult 

def test_invalid_move():

    env = engine.GameEnv()

    env.init()


    start_r = 6
    start_c = 3

    card_id = 203
    r = env.place_route_card(card_id, start_r , start_c + 1)
    assert(r == PlaceResult.Invalid)

    r = env.place_route_card(card_id, start_r - 1, start_c )
    assert(r == PlaceResult.Invalid)

    r = env.place_route_card(card_id, start_r , start_c + 1)
    assert(r == PlaceResult.Invalid)

    r = env.place_route_card(card_id, start_r + 1, start_c )
    assert(r == PlaceResult.Success)

    card_id = 237
    r = env.place_route_card(card_id, start_r + 2, start_c)
    assert(r == PlaceResult.No_path_to_ladder)

    card_id = 226
    r = env.place_route_card(card_id, start_r - 2, start_c - 1)
    assert(r == PlaceResult.No_path_to_ladder)

    card_id = 225
    r = env.place_route_card(card_id, start_r , start_c )
    assert(r == PlaceResult.Card_exist)


    card_id = 224
    r = env.place_route_card(card_id, 1  , 20)
    assert(r == PlaceResult.Out_of_bound)

    r = env.place_route_card(card_id, -1  , 2)
    assert(r == PlaceResult.Out_of_bound)

    r = env.place_route_card(card_id, 1  , -1)
    assert(r == PlaceResult.Out_of_bound)

    r = env.place_route_card(card_id, 20  , 2)
    assert(r == PlaceResult.Out_of_bound)
