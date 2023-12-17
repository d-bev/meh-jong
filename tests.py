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
    # print("  Expected Text Tests")
    # print("\tred_char_five:\t%s" % str(red_char_five))
    # print("\tchar_five:\t%s" % str(char_five))
    # print("\tcirc_three:\t%s" % str(circ_three))
    # print("\teast_wind:\t%s" % str(east_wind))
    # print("\tred_dragon:\t%s" % str(red_dragon)) 

    # print("  String Matching Tests")
    # print((str(red_char_five) == "5 of characters (red)"))
    # print((str(char_five) == "5 of characters"))
    # print((str(circ_three) == "3 of circles"))
    # print((str(east_wind) == "east wind"))
    # print((str(red_dragon) == "red dragon"))
    
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
    print("*** PLAYER TESTS: DONE ***")

def scorer_tests():
    print("*** SCORER TESTS: START ***")
    print("*** SCORER TESTS: DONE ***")

def dealer_tests():
    print("*** DEALER TESTS: START ***")
    print("*** DEALER TESTS: DONE ***")

# run all test suites

tile_tests()
player_tests()
scorer_tests()
dealer_tests()




# NUM_COPIES = 4
# RED_FIVES = True


# dealer = Dealer.Dealer(NUM_COPIES, RED_FIVES)

# print()

# dealer.remaining()

# bob_tiles = dealer.deal_player()

# print("\nbefore sorting:\n")

# for i in range(len(bob_tiles)):
#     print(bob_tiles[i])

# bob = Player.Player("bob", bob_tiles)

# print("\nafter sorting:\n")
# for i in range(len(bob.hand)):
#     print(bob.hand[i])

# print()

# dealer.remaining()

# print("\nremoving tile at index 3")
# discarded_tile = bob.discard(3)

# print("\nafter discarding:\n")
# for i in range(len(bob.hand)):
#     print(bob.hand[i])