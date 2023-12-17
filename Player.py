import Tile

class Player():
    def __init__(self, name:str, starting_tiles:list):
        self.__name : str = name
        self.__hand : list = starting_tiles
        self.__score : int = 0

        # Handling the '14th' tile in each player's hand:
        #   the tile a player draws at the start of their turn
        #   the tile another player discards

        self.__drawn_tile = None
        self.__called_tiles : list = []
        self.__winning_tiles : list = []

        self.sort_tiles()
        
    #   GETTERS
        

    @property
    def name(self):
        return self.__name
        
    @property
    def hand(self):
        return self.__hand

    @property
    def score(self):
        return self.__score

    @property
    def called_tiles(self):
        return self.__called_tiles

    @property
    def drawn_tile(self):
        return self.__drawn_tile
    
    @property
    def winning_tiles(self):
        return self.__winning_tiles


    #   SETTERS


    @name.setter
    def name(self, new_name : str):
        self.__name = new_name

    @hand.setter
    def hand(self, new_hand : list):
        self.__hand = new_hand

    @score.setter
    def score(self, new_score : int):
        self.__score = new_score

    @called_tiles.setter
    def add_tile(self, new_tiles : list):

        # FIXME: not sure if this is correct method to append a small group of tiles, as you would have to append either:
        #       Chi / Pon   : two tiles from player's hand and 1 other player's discarded tile
        #       Kan         : three tiles from player's hand and 1 other player's discarded tile
        #       Natural Kan : all four tiles from player's hand

        self.__called_tiles.append(new_tiles)

    @drawn_tile.setter
    def drawn_tile(self, new_draw : Tile.Tile):
        self.drawn_tile = new_draw     

    @winning_tiles.setter
    def winning_tiles(self, tiles : list):
        self.__winning_tiles = tiles


    # FUNCTIONS
        

    # method to allow player to re-order the tiles in their respective hands
    def swap_tiles(self, index_1: int, index_2: int):
        temp : Tile = self.hand[index_1]
        self.hand[index_1] = self.hand[index_2]
        self.hand[index_2] = temp


    # method to allow a player to select a specific tile to discard at the end of the turn
    def discard(self, tile_to_discard: int):
        # get metadata of selected Tile
        discard_copy = self.hand[tile_to_discard]

        # "remove" tile from hand (overwrite hand with a new hand that doesn't contain the 'discarded' value)
        hand = []
        for i in range(len(self.hand)):
            if i != tile_to_discard:
                hand.append(self.hand[i])
        self.hand = hand

        # return Tile to caller so that Tile can be 'moved' to DiscardPile
        return discard_copy


    # method to (if a player runs out of time on their turn) force them to discard their newly-drawn tile
    def force_discard(self):
        # store drawn tile
        draw = self.__drawn_tile

        #clear drawn tile
        self.__drawn_tile = None

        # return Tile to caller so that Tile can be 'moved' to DiscardPile
        return draw


    #   Create an equivalent tile set, but sorted first by suit, and then by value
    def sort_tiles(self):
        hand = []
        
        red_character = False
        red_circle = False
        red_bamboo = False
        
        for i in range(len(self.hand)):
            tile = self.hand[i]
            if tile.id in [4, 13, 22] and tile.is_red == True:
                match tile.id:
                    case 4:
                        red_character = True
                    case 13:
                        red_circle = True
                    case 22:
                        red_bamboo = True
            hand.append(tile.id)

        hand = sorted(hand)

        for i in range(len(hand)):
            if hand[i] == 4 and red_character:
                red_character = False
                self.hand[i] = Tile.Tile(hand[i], True)
            elif hand[i] == 13 and red_circle:
                red_circle = False
                self.hand[i] = Tile.Tile(hand[i], True)
            elif hand[i] == 22 and red_bamboo:
                red_bamboo = False
                self.hand[i] = Tile.Tile(hand[i], True)
            else:
                self.hand[i] = Tile.Tile(hand[i], False)

        return self.hand


    # TESTING
        

    """
        TODO: Determine whether or not closed Kan calls should be 'in hand' or aside
                Thinking that should be considered as 'in hand' to avoid game logic thinking hand has 'been opened'

        if(is player's turn):
            # hand size of 13   no calls,         1 drawn tile

            # hand size of 10,  called Chi/Pon,   1 drawn tile
            # hand size of 9,   called Kan,       1 drawn tile

            # hand size of 7,   2 Chi/Pon,        1 drawn tile
            # hand size of 6,   1 Kan 1 Chi/Pon,  1 drawn tile
            # hand size of 5,   2 Kan calls,      1 drawn tile

            # hand size of 4,   3 Chi/Pon,        1 drawn tile
            # hand size of 3,   1 Kan 2 Chi/Pon,  1 drawn tile
            # hand size of 2,   2 Kan 1 Chi/Pon,  1 drawn tile

            # hand size of 1,   called 4 Chi/Pon, 1 drawn tile
            # hand size of 1,   3 Kan,            1 drawn tile

        if(not player's turn):
            # hand size of 13   no calls

            # hand size of 10,  called Chi/Pon
            # hand size of 9,   called Kan

            # hand size of 7,   2 Chi/Pon
            # hand size of 6,   1 Kan 1 Chi/Pon
            # hand size of 5,   2 Kan calls

            # hand size of 4,   3 Chi/Pon
            # hand size of 3,   1 Kan 2 Chi/Pon
            # hand size of 2,   2 Kan 1 Chi/Pon

            # hand size of 1,   called 4 Chi/Pon
            # hand size of 1,   3 Kan
    """