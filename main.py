import Dealer
import Player
import Scorer
# import Tile



dealer = Dealer.Dealer(num_players=4, red_fives=False)


bob = Player.Player("bob", dealer.deal_player())


while dealer.remaining() > 13:
    bob.hand = dealer.deal_player()
    if len(bob.hand) != 13:
        print (f"{len(bob.hand)}?! WHAT THE FUCK")




"""
ASSUMPTIONS:

    4-player game
    Red Fives are optional
    standard tileset (riichi)
    no time limits

"""



"""
ASSUMPTIONS:

    3-player game
    Red Fives are optional
    unique tileset (no non-terminal bamboo)
    no time limits

"""
