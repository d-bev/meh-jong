import Tile
import Player
import Dealer
import Scorer


# Establish various test "suites"


def tile_tests():
    red_char_five = Tile.Tile(4)
    char_five = Tile.Tile(4)
    circ_three = Tile.Tile(11)
    east_wind = Tile.Tile(27)
    red_dragon = Tile.Tile(32)

    print("*** TILE TESTS: START ***")
    
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

    # ensure that a player can discard (need a hand without duplicates; would break "id != id")

    tile_list = [Tile.Tile(1), Tile.Tile(17), Tile.Tile(19), 
                 Tile.Tile(3), Tile.Tile(24), Tile.Tile(30), 
                 Tile.Tile(5), Tile.Tile(18), Tile.Tile(6), 
                 Tile.Tile(22), Tile.Tile(28), Tile.Tile(8),
                 Tile.Tile(10)]
    
    bob = Player.Player("bob", tile_list) 
    before_size = len(bob.hand)
    before_tile : Tile = bob.hand[3]

    bob.discard(3) # removing tile at index 3
    after_size = len(bob.hand)
    after_tile = bob.hand[3]

    if (before_size - 1 == after_size) and (before_tile.id != after_tile.id):
        print("\tdiscard test:\tGOOD")
    else:
        print("\tdiscard test:\tFAIL")


    # TODO: ensure that a player can swap the position of two tiles in their hand



    # ensure that hand-sorting works 

    dealer = Dealer.Dealer(4)
    hand = dealer.deal_player()
    bob = Player.Player("bob", hand) # when a player is instantiated, their hand will be sorted

    test_passed = True
    first_tile : Tile = bob.hand[0]

    for i in range(len(bob.hand)):
        # the first tile in the player's hand should have the smallest id
        if bob.hand[i].id < first_tile.id:
            test_passed = False

    if test_passed:
        print("\tsorting test:\tGOOD")
    else:
        print("\tsorting test:\tFAIL")






    print("*** PLAYER TESTS: DONE ***")

def dealer_tests():
    print("*** DEALER TESTS: START ***")
    # ensure 136 tiles for 4 players
    dealer = Dealer.Dealer(4)

    print(len(dealer.tile_list))

    if len(dealer.tile_list) == 136:
        print("\tTile count:\tGOOD")
    else:
        print("\tTile count:\tFAIL")

    # ensure dealer has correct number pf each kind of tile
    dealer = Dealer.Dealer(4)
    if dealer.validate_tileset():
        print("")
    else:
        print("")

    dealer = Dealer.Dealer(3)
    if dealer.validate_tileset():
        print("")
    else:
        print("")

    dealer = Dealer.Dealer(4)
    if dealer.validate_tileset():
        print("")
    else:
        print("")

    dealer = Dealer.Dealer(3)
    if dealer.validate_tileset():
        print("")
    else:
        print("")
    
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

selection = int(input())

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
