import Dealer
import Hand
import Player



NUM_COPIES = 4
RED_FIVES = False



bob = Dealer.Dealer(NUM_COPIES, RED_FIVES)

print(bob.tilesLeft())

ethan = Player.Player("ethan", bob.deal())

print(bob.tilesLeft())

print(ethan.hand.tiles)
"""
ASSUMPTIONS:

    4-player game
    Red Fives are optional
    standard tileset (riichi)
    no time limits

LOGIC:

    Game-Mode is selected and/or number of players is chosen
    A Game() object is created WITH:
        A discard pile for each Player() ; is obj or list better?
         A TileSet()
        A Player() object created for each player
            has a Hand()
            a default amount of points (maybe not in Player())
       ???
"""