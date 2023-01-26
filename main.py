import TileSet
import Hand


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


NUM_TILE_COPIES = 4


# Testing the creation of a standard tileset
"""
test_set_1 = TileSet.TileSet(NUM_TILE_COPIES, True)
print(str(test_set_1))
print(repr(test_set_1))
"""
