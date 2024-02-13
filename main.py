import Dealer
import Player
import Scorer
# import Tile



print("\n4, false\n")
dealer = Dealer.Dealer(num_players=4, red_fives=False)

hand = dealer.deal_player()

bob = Player.Player("bob", hand)

print("player's hand before:\n")

for i in range(len(bob.hand)):
    print(i, ": ", bob.hand[i])

bob.swap_tiles(0, 1)
bob.swap_tiles(3, 8)
bob.swap_tiles(11, 12)


print("\nplayer's hand after:\n")

for i in range(len(bob.hand)):
    print(i, ": ", bob.hand[i])










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


# NUM_COPIES = 3
# RED_FIVES = True


# dealer = Dealer.Dealer(NUM_COPIES, RED_FIVES)


"""



Planned Class/Object Heirarchy:
        Game
            Dealer
                Dead Wall
                Tile
            Player
                Tile
            Scorer
                Tile
            

    Possible Class Variables:

        Game
            round wind
            players' seats 
            streak counter
                
        Dead Wall
            Top Row (to determine dora)
            Bottom Row (to determine ura-dora)
    
"""


"""    
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