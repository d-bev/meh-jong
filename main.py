import Dealer
import Player
import Scorer
import Tile


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