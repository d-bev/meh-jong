import Tile
import Player
import Dealer
import Scorer


# Establish various test "suites"

# TODO: Encapsulate these tests!


def tile_tests():
    red_char_five = Tile.Tile(34)
    char_five = Tile.Tile(4)
    circ_three = Tile.Tile(11)
    east_wind = Tile.Tile(27)
    red_dragon = Tile.Tile(32)

    print("****\tTILE TESTS:\t\tSTART\t****")
    
    if str(red_char_five) == "5 of characters (red)":
        print("\tred_char_five:\t\tGOOD")
    else:
        print("\tred_char_five:\t\tFAIL")

    if str(char_five) == "5 of characters":
        print("\tchar_five:\t\tGOOD")
    else:
        print("\tchar_five:\t\tFAIL")

    if str(circ_three) == "3 of circles":
        print("\tcirc_three:\t\tGOOD")
    else:
        print("\tcirc_three:\t\tFAIL")

    if str(east_wind) == "east wind":
         print("\teast_wind:\t\tGOOD")
    else:
         print("\teast_wind:\t\tFAIL")

    if str(red_dragon) == "red dragon":
        print("\tred_dragon:\t\tGOOD")
    else:
        print("\tred_dragon:\t\tFAIL")
    
    print("****\tTILE TESTS:\t\tDONE\t****")

def player_tests():
    print("****\tPLAYER TESTS:\t\tSTART\t****")

    # ensure that a player can discard (need a hand without duplicates; would break "id != id")

    tile_list = [Tile.Tile(1), Tile.Tile(17), Tile.Tile(19), 
                 Tile.Tile(3), Tile.Tile(24), Tile.Tile(30), 
                 Tile.Tile(5), Tile.Tile(18), Tile.Tile(6), 
                 Tile.Tile(22), Tile.Tile(28), Tile.Tile(8),
                 Tile.Tile(10)]
    
                # 0  1  2
                # 3  4  5
                # 6  7  8
                # 9  10 11
                # 12
    
    list_copy = tile_list

    # ensure a player can discard a tile from their hand
    
    bob = Player.Player("bob", tile_list) 
    before_size = len(bob.hand)
    before_tile : Tile = bob.hand[3]

    bob.discard(3) # removing tile at index 3
    after_size = len(bob.hand)
    after_tile = bob.hand[3]

    if (before_size - 1 == after_size) and (before_tile.id != after_tile.id):
        print("\tdiscard index 3:\tGOOD")
    else:
        print("\tdiscard index 3:\tFAIL")

    # ensure that a player can swap the position of two tiles in their hand
        
    bob = Player.Player("bob", list_copy) 
    tile_1_id = bob.hand[2].id
    tile_2_id = bob.hand[4].id
    bob.swap_tiles(2, 4)      # this should swap index 2 (id = 19) with index  (id = 24)

    if bob.hand[2].id == tile_2_id and bob.hand[4].id == tile_1_id:
        print("\ttile swap 2 & 4:\tGOOD")
    else:
        print("\ttile swap 2 & 4:\tFAIL")

    bob = Player.Player("bob", list_copy)
    tile_1_id = bob.hand[0].id
    tile_2_id = bob.hand[5].id
    bob.swap_tiles(0, 5)      # this should swap the (id = 19) with the (id = 24)

    if bob.hand[0].id == tile_2_id and bob.hand[5].id == tile_1_id:
        print("\ttile swap 0 & 5:\tGOOD")
    else:
        print("\ttile swap 0 & 5:\tFAIL")

    bob = Player.Player("bob", list_copy)
    tile_1_id = bob.hand[12].id
    tile_2_id = bob.hand[1].id
    bob.swap_tiles(12, 1)      # this should swap the (id = 19) with the (id = 24)

    if bob.hand[12].id == tile_2_id and bob.hand[1].id == tile_1_id:
        print("\ttile swap 12 & 1:\tGOOD")
    else:
        print("\ttile swap 12 & 1:\tFAIL")

    # ensure that hand-sorting works (4 players, with reds)

    dealer = Dealer.Dealer(4, False)
    bob = Player.Player("bob", dealer.deal_player()) # when a player is instantiated, their hand will be sorted

    test_passed = True
    first_tile : Tile = bob.hand[0]

    for i in range(len(bob.hand)):
        # the first tile in the player's hand should have the smallest id
        if bob.hand[i].id < first_tile.id:
            print(f"failed on {bob.hand[i].id} < {first_tile.id}")
            test_passed = False

    if test_passed:
        print("\t4P with reds sorting:\tGOOD")
    else:
        print("\t4P with reds sorting:\tFAIL")
    
    # ensure that hand-sorting works (4 players, no reds)

    dealer = Dealer.Dealer(4, False)
    bob = Player.Player("bob", dealer.deal_player()) # when a player is instantiated, their hand will be sorted

    test_passed = True
    first_tile : Tile = bob.hand[0]

    for i in range(len(bob.hand)):
        # the first tile in the player's hand should have the smallest id
        if bob.hand[i].id < first_tile.id:
            print(f"failed on {bob.hand[i].id} < {first_tile.id}")
            test_passed = False

    if test_passed:
        print("\t4P no reds sorting:\tGOOD")
    else:
        print("\t4P no reds sorting:\tFAIL")

    # ensure that hand-sorting works (3 players, with reds)

    dealer = Dealer.Dealer(4, False)
    bob = Player.Player("bob", dealer.deal_player()) # when a player is instantiated, their hand will be sorted

    test_passed = True
    first_tile : Tile = bob.hand[0]

    for i in range(len(bob.hand)):
        # the first tile in the player's hand should have the smallest id
        if bob.hand[i].id < first_tile.id:
            print(f"failed on {bob.hand[i].id} < {first_tile.id}")
            test_passed = False

    if test_passed:
        print("\t3P with reds sorting:\tGOOD")
    else:
        print("\t3P with reds sorting:\tFAIL")

    # ensure that hand-sorting works (3 players, no reds)

    dealer = Dealer.Dealer(4, False)
    bob = Player.Player("bob", dealer.deal_player()) # when a player is instantiated, their hand will be sorted

    test_passed = True
    first_tile : Tile = bob.hand[0]

    for i in range(len(bob.hand)):
        # the first tile in the player's hand should have the smallest id
        if bob.hand[i].id < first_tile.id:
            print(f"failed on {bob.hand[i].id} < {first_tile.id}")
            test_passed = False

    if test_passed:
        print("\t3P no reds sorting:\tGOOD")
    else:
        print("\t3P no reds sorting:\tFAIL")
    

    print("****\tPLAYER TESTS:\t\tDONE\t****")

def dealer_tests():
    print("****\tDEALER TESTS:\t\tSTART\t****")

    # ensure 136 tiles for 4 players

    dealer = Dealer.Dealer(4, True)
    if len(dealer.tile_list) == 136:
        print("\t4 players tile count:\tGOOD")
    else:
        print("\t4 players tile count:\tFAIL")

    # ensure 108 tiles for 3 players
        
    dealer = Dealer.Dealer(3, True)
    if len(dealer.tile_list) == 108:
        print("\t3 players tile count:\tGOOD")
    else:
        print("\t3 players tile count:\tFAIL")

    # ensure dealer has correct number of each kind of tile
    dealer = Dealer.Dealer(4, False)
    if dealer.validate_tileset():
        print("\t4 players NO reds:\tGOOD")
    else:
        print("\t4 players NO reds:\tFAIL")

    dealer = Dealer.Dealer(4, True)
    if dealer.validate_tileset():
        print("\t4 players with reds:\tGOOD")
    else:
        print("\t4 players with reds:\tFAIL")

    dealer = Dealer.Dealer(3, False)
    if dealer.validate_tileset():
        print("\t3 players with reds:\tGOOD")
    else:
        print("\t3 players with reds:\tFAIL")

    dealer = Dealer.Dealer(3, True)
    if dealer.validate_tileset():
        print("\t3 players NO reds:\tGOOD")
    else:
        print("\t3 players NO reds:\tFAIL")
    
    # ensure dealer can give a player a hand (and tiles are correctly removed)
        
    # ensure dealer can create a dead wall (and tiles are correctly removed)
        
    # ensure dealer can deal a tile (and tiles are correctly removed)
        
    # dealer = Dealer.Dealer(NUM_PLAYERS= , RED_FIVES= )
    # if():
    #     print("")
    # else:
    #     print("")
    
    print("****\tDEALER TESTS:\t\tDONE\t****")

def scorer_tests():
    print("****\tSCORER TESTS:\t\tSTART\t****")
    print("****\tSCORER TESTS:\t\tDONE\t****")



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
