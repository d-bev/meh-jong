import Tile
import Player
import Dealer
import Scorer


# Establish various test "suites"


def tile_tests():
    red_char_five = Tile.Tile(4, True)
    char_five = Tile.Tile(4, False)
    circ_three = Tile.Tile(11, False)
    east_wind = Tile.Tile(27, False)
    red_dragon = Tile.Tile(32, False)

    print("*** TILE TESTS: START ***")
    
    print("  String Matching Tests")
    if str(red_char_five) == "5 of characters (red)":
        print("\tred_char_five:\tGOOD")
    else:
        print("\tred_char_five:\tFAIL")

    if str(char_five) == "5 of characters":
        print("\tchar_five:\tGOOD")
    else:
        print("\tchar_five:\tFAIL")

    if str(circ_three) == "3 of circles":
        print("\tcirc_three:\tGOOD")
    else:
        print("\tcirc_three:\tFAIL")

    if str(east_wind) == "east wind":
         print("\teast_wind:\tGOOD")
    else:
         print("\teast_wind:\tFAIL")

    if str(red_dragon) == "red dragon":
        print("\tred_dragon:\tGOOD")
    else:
        print("\tred_dragon:\tFAIL")
    
    print("*** TILE TESTS: DONE ***")

def player_tests():
    print("*** PLAYER TESTS: START ***")

    # ensure that a player can discard

    # purposefully creating a hand that doesn't have a duplicate (breaks testing logic)
    tile_list = [Tile.Tile(1, False), Tile.Tile(17, False), Tile.Tile(19, False), 
                 Tile.Tile(3, False), Tile.Tile(24, False), Tile.Tile(30, False), 
                 Tile.Tile(5, False), Tile.Tile(18, False), Tile.Tile(6, False), 
                 Tile.Tile(22, False), Tile.Tile(28, False), Tile.Tile(8, False),
                 Tile.Tile(10, False)]
    
    bob = Player.Player("bob", tile_list)
    before_size = len(bob.hand)
    before_tile : Tile = bob.hand[3]

    bob.discard(3) # removing tile at index 3
    after_size = len(bob.hand)
    after_tile = bob.hand[3]

    if before_size != after_size and (before_tile.id != after_tile.id):
        print("\tdiscard at index:\tGOOD")
    else:
        print("\tdiscard at index:\tFAIL")

    # ensure that a player can swap the position of two tiles in their hand
        



    print("*** PLAYER TESTS: DONE ***")

def dealer_tests():
    print("*** DEALER TESTS: START ***")
    # ensure 136 tiles for 4 players
    dealer = Dealer.Dealer(4, True)
    if(len(dealer.deal_player()) == 136):
        print("\tTile count:\tGOOD")
    else:
        print("\tTile count:\tFAIL")
    
    # ensure dealer can give a player a hand (and tiles are correctly removed)
        
    # ensure dealer can create a dead wall (and tiles are correctly removed)
        
    # ensure dealer can deal a tile (and tiles are correctly removed)
        
    # dealer = Dealer.Dealer(NUM_COPIES= , RED_FIVES= )
    # if():
    #     print("")
    # else:
    #     print("")
    
    print("*** DEALER TESTS: DONE ***")

def scorer_tests():
    print("*** SCORER TESTS: START ***")
    print("*** SCORER TESTS: DONE ***")



### MAIN ###


# prompt for test suites
print("Select a test suite to run:")
print("1 - Tile Tests")
print("2 - Dealer Tests")
print("3 - Player Tests")
print("4 - Scorer Tests")
# ...
print("9 - Run all tests")

selection : int = input()

match selection:
    case 1:
        tile_tests()
    case 2:
        dealer_tests()
    case 3:
        player_tests()
    case 4:
        scorer_tests()
    case 9:
        tile_tests()
        dealer_tests()
        player_tests()
        scorer_tests()
    case _:
        tile_tests()
        dealer_tests()
        player_tests()
        scorer_tests()
