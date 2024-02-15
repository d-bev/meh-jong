import Tile
import Player
import Dealer
import Scorer


#   Establish various test "suites"


def tile_tests():
    print("****\tTILE TESTS:\t\tSTART\t****")
    
    print("\tred_char_five:\t\t", str(test_tile_to_string(Tile.Tile(34), "5 of characters (red)")))
    print("\tchar_five:\t\t", str(test_tile_to_string(Tile.Tile(4), "5 of characters")))
    print("\tcirc_three:\t\t", str(test_tile_to_string(Tile.Tile(11), "3 of circles")))
    print("\teast_wind:\t\t", str(test_tile_to_string(Tile.Tile(27), "east wind")))
    print("\tred_dragon:\t\t", str(test_tile_to_string(Tile.Tile(32), "red dragon")))
    
    print("****\tTILE TESTS:\t\tDONE\t****")

def player_tests():
    print("****\tPLAYER TESTS:\t\tSTART\t****")

    # instantiating a Dealer to create hands for the Players to use in these tests
    dealer = Dealer.Dealer(4, True)
    
    # ensure a player can discard a tile from their hand (also ensures hand size is correct before and after discarding)
    
    print("\tdiscard index 3:\t", str(test_discard_tile(dealer.deal_player(), 3)))
    print("\tdiscard index 0:\t", str(test_discard_tile(dealer.deal_player(), 0)))
    print("\tdiscard index 12:\t", str(test_discard_tile(dealer.deal_player(), 12)))

    # ensure that a player can swap the position of two tiles in their hand

    print("\ttile swap 2 & 4:\t", str(test_tile_swap(dealer.deal_player(), 2, 4)))
    print("\ttile swap 0 & 5:\t", str(test_tile_swap(dealer.deal_player(), 0, 5)))
    print("\ttile swap 12 & 1:\t", str(test_tile_swap(dealer.deal_player(), 12, 1)))

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


#   Individual test functions 
    
    
def test_tile_to_string(tile : Tile, expected : str):
        
    # print("\ttest_tile_to_string(", tile, ",", expected, ")")
    return str(tile) == expected
    
def test_discard_tile(hand : list, discard_index : int):

    # create the Player object
    bob = Player.Player("bob", hand) 

    # FIXME: FOR SOME GOD-FORSAKEN REASON, THE HAND SIZE IS SOMETIMES 12 HERE INSTEAD OF 13
    #           I CHECKED DEALER.DEAL_PLAYER() AND THAT'S NOT THE ISSUE
    print(f"\nsize: {len(bob.hand)}, index: {discard_index}\n")

    intended_discard : Tile = bob.hand[discard_index]

    # map the frequency of the selected tile BEFORE discarding
    freq = {}
    for i in range(len(bob.hand)):
        item : Tile = bob.hand[i]

        if (item.id in freq):
            freq[item.id] += 1
        else:
            freq[item.id] = 1

    # record the hand size and the starting tile frequency
    size_before = len(bob.hand)
    freq_before : int = freq[intended_discard.id]

    # have the player discard the tile from their hand
    bob.discard(discard_index) 

    # map the frequency of the selected tile AFTER discarding
    freq.clear()
    for i in range(len(bob.hand)):
        item : Tile = bob.hand[i]

        if (item.id in freq):
            freq[item.id] += 1
        else:
            freq[item.id] = 1

    # record the new hand size, and the new tile frequency
    size_after = len(bob.hand)

    # need to grab the frequency this way in case the frequency is zero (would raise KeyError)
    freq_after = freq.get(intended_discard.id)

    # if freq_after has no value, assign it a value of 0 so that the boolean can be evaluated
    if not freq_after:
        freq_after = 0

    # ensure that the hand size is 1 less than it started, and that the frequency of the tile type
    #   at the discard_index is 1 less than whatever it was before discarding
    return (size_before == (size_after + 1)) and (freq_before == (freq_after + 1))

def test_tile_swap(hand : list, first_tile_index : int, second_tile_index : int):

    # create a player with the hand we were passed
    bob = Player.Player("bob", hand) 

    # FIXME: FOR SOME GOD-FORSAKEN REASON, THE HAND SIZE IS SOMETIMES 12 HERE INSTEAD OF 13
    #           I CHECKED DEALER.DEAL_PLAYER() AND THAT'S NOT THE ISSUE
    print(f"\nsize: {len(bob.hand)}, first index: {first_tile_index}, second index: {second_tile_index}\n")

    # ask the player for the value of the tile at each index
    tile_1_id = bob.hand[first_tile_index].id
    tile_2_id = bob.hand[second_tile_index].id

    # have the player swap the tiles
    bob.swap_tiles(first_tile_index, second_tile_index) 
    
    return bob.hand[first_tile_index].id == tile_2_id and bob.hand[second_tile_index].id == tile_1_id

def test_hand_sorting():
    pass



### MAIN ###


# prompt for test suites
print("Select a test suite to run:")
print("1 - Tile Tests")
print("2 - Player Tests")
print("3 - Dealer Tests")
print("4 - Scorer Tests")
# ...
print("9 - Run all tests")

selection = int(input())

match selection:
    case 1:
        tile_tests()
    case 2:
        player_tests()
    case 3:
        dealer_tests()
    case 4:
        scorer_tests()
    case 9:
        tile_tests()
        player_tests()
        dealer_tests()
        scorer_tests()
    case _:
        tile_tests()
        player_tests()
        dealer_tests()
        scorer_tests()
