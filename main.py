import Dealer
import Player
import Scorer
import Tile

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

NUM_COPIES = 4
RED_FIVES = True


dealer = Dealer.Dealer(NUM_COPIES, RED_FIVES)

print()

dealer.remaining()

bob_tiles = dealer.deal_player()

print("\nbefore sorting:\n")

for i in range(len(bob_tiles)):
    print(bob_tiles[i])

bob = Player.Player("bob", bob_tiles)

print("\nafter sorting:\n")
for i in range(len(bob.hand)):
    print(bob.hand[i])

print()

dealer.remaining()

print("\nremoving tile at index 3")
discarded_tile = bob.discard(3)

print("\nafter discarding:\n")
for i in range(len(bob.hand)):
    print(bob.hand[i])


"""
ASSUMPTIONS:

    3-player game
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


NUM_COPIES = 3
RED_FIVES = True


dealer = Dealer.Dealer(NUM_COPIES, RED_FIVES)


"""



Classes to be implemented:
        Game
        TileSet
            Tile
        Dead Wall
        Player
            Hand

    Possible Class Variables:

        Game
            round wind
            who's dealer
            players' scores
            streak counter
                
        Dead Wall (might want to make DeadWall a TileSet object that Game object oversees)
            Top Row
                dora
            Bottom Row
                ura-dora
    
                
    @classmethod
    def call_chi():
        # take tile discarded by previous player
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player discard

    @classmethod
    def call_pon():
        # take tile discarded by previous player
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player discard

    @classmethod
    def call_open_kan():
        # take tile discarded by previous player
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player discard

    @classmethod
    def call_closed_kan():
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player draw a tile
        # flip next Dora Indicator in Dead Wall
        # make player discard

    @classmethod
    def call_kita():
        # move tile to __table_side
        # player draws a tile
        # make player discard

    @classmethod
    def call_ron():
        # take tile discarded by previous player
        # evaluate point value of player's hand

    @classmethod
    def call_tsumo():
        # evaluate point value of player's hand

"""