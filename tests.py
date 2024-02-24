import Tile
import Player
import Dealer
import Scorer


#   Establish various test "suites"


def tile_tests():
    print("****\tTILE TESTS:\t\tSTART\t****")
    
    print(f"\tred_char_five:\t\t{str(test_tile_to_string(Tile.Tile(5), '5 of characters (red)'))}")
    print(f"\tchar_five:\t\t{str(test_tile_to_string(Tile.Tile(4), '5 of characters'))}")
    print(f"\tcirc_three:\t\t{str(test_tile_to_string(Tile.Tile(12), '3 of circles'))}")
    print(f"\teast_wind:\t\t{str(test_tile_to_string(Tile.Tile(30), 'east wind'))}")
    print(f"\tred_dragon:\t\t{str(test_tile_to_string(Tile.Tile(35), 'red dragon'))}")
    
    print("****\tTILE TESTS:\t\tDONE\t****")

def player_tests():
    print("****\tPLAYER TESTS:\t\tSTART\t****")

    # instantiating a Dealer to create hands for the Players to use in these tests
    dealer = Dealer.Dealer(4, True)
    example_hand = dealer.deal_player()
    
    # ensure a player can discard a tile from their hand (also ensures hand size is correct before and after discarding)
    print(f"\tdiscard index 3:\t{str(test_discard_tile(example_hand, 3))}")
    print(f"\tdiscard index 0:\t{str(test_discard_tile(example_hand, 0))}")
    print(f"\tdiscard index 12:\t{str(test_discard_tile(example_hand, 12))}")

    # ensure that a player can swap the position of two tiles in their hand
    print(f"\ttile swap 2 & 4:\t{str(test_tile_swap(example_hand, 2, 4))}")
    print(f"\ttile swap 0 & 5:\t{str(test_tile_swap(example_hand, 0, 5))}")
    print(f"\ttile swap 12 & 1:\t{str(test_tile_swap(example_hand, 12, 1))}")

    # ensure that hand-sorting works (4 players, with reds)
    dealer = Dealer.Dealer(4, True)
    example_hand = dealer.deal_player()
    print(f"\t4P with reds sorting:\t{test_hand_sorting(example_hand)}")
    
    # ensure that hand-sorting works (4 players, no reds)
    dealer = Dealer.Dealer(4, False)
    example_hand = dealer.deal_player()
    print(f"\t4P no reds sorting:\t{test_hand_sorting(example_hand)}")

    # ensure that hand-sorting works (3 players, with reds)
    dealer = Dealer.Dealer(3, True)
    example_hand = dealer.deal_player()
    print(f"\t3P with reds sorting:\t{test_hand_sorting(example_hand)}")

    # ensure that hand-sorting works (3 players, no reds)
    dealer = Dealer.Dealer(3, False)
    example_hand = dealer.deal_player()
    print(f"\t3P no reds sorting:\t{test_hand_sorting(example_hand)}")
    

    print("****\tPLAYER TESTS:\t\tDONE\t****")

def dealer_tests():
    print("****\tDEALER TESTS:\t\tSTART\t****")

    # ensure 136 tiles for 4 players
    dealer = Dealer.Dealer(4, True)
    print(f"\t4P with reds count:\t{test_tile_count(4, dealer.remaining())}")

    # ensure 136 tiles for 4 players
    dealer = Dealer.Dealer(4, False)
    print(f"\t4P no reds count:\t{test_tile_count(4, dealer.remaining())}")

    # ensure 108 tiles for 3 players
    dealer = Dealer.Dealer(3, True)
    print(f"\t3P with reds count:\t{test_tile_count(3, dealer.remaining())}")

    # ensure 108 tiles for 3 players
    dealer = Dealer.Dealer(3, False)
    print(f"\t3P no reds count:\t{test_tile_count(3, dealer.remaining())}")

    # ensure dealer has correct number of each kind of tile
    dealer = Dealer.Dealer(4, False)
    print(f"\t4P no reds tileset:\t{dealer.validate_tileset()}")

    # ensure dealer has correct number of each kind of tile
    dealer = Dealer.Dealer(4, True)
    print(f"\t4P with reds tileset:\t{dealer.validate_tileset()}")

    # ensure dealer has correct number of each kind of tile
    dealer = Dealer.Dealer(3, False)
    print(f"\t3P with reds tileset:\t{dealer.validate_tileset()}")

    # ensure dealer has correct number of each kind of tile
    dealer = Dealer.Dealer(3, True)
    print(f"\t3P no reds tileset:\t{dealer.validate_tileset()}")
    
    # TODO: ensure dealer can give a player a hand (and tiles are correctly removed)
        
    # TODO: ensure dealer can create a dead wall (and tiles are correctly removed)
        
    # TODO: ensure dealer can deal a tile (and tiles are correctly removed)
    
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

    # create a player with the hand we were provided
    bob = Player.Player("bob", hand) 

    # ask the player for the value of the tile at each index
    tile_1_id = bob.hand[first_tile_index].id
    tile_2_id = bob.hand[second_tile_index].id

    # have the player swap the tiles
    bob.swap_tiles(first_tile_index, second_tile_index) 
    
    return bob.hand[first_tile_index].id == tile_2_id and bob.hand[second_tile_index].id == tile_1_id

def test_hand_sorting(hand : list):
    bob = Player.Player("bob", hand) # when a player is instantiated, their hand will be sorted

    passed = True
    first_tile : Tile = bob.hand[0]
    error = "\n"

    for i in range(len(bob.hand)):
        # the first tile in the player's hand should have the smallest id
        if bob.hand[i].id < first_tile.id:
            error += f"failed on {bob.hand[i].id} < {first_tile.id}"
            passed = False

    if passed == False:
        print(error)

    return passed

def test_tile_count(num_players : int, tiles_remaining : int):
    if num_players == 3 and tiles_remaining == 108:
        return True
    elif num_players == 4 and tiles_remaining == 136:
        return True
    else:
        return False

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






