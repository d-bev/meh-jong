import Tile

class Player():
    def __init__(self, name:str, starting_tiles:list):
        self.__name : str = name
        self.__hand : list= starting_tiles
        self.__score : int = 0

        # Handling the '14th' tile in each player's hand:
        #   the tile they draw at the start of the turn
        #   the tile another player discards

        self.__drawn_tile = None
        self.__called_tiles : list = []
        self.__winning_tiles : list = []

        
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
        #       Chi / Pon   : two tiles from player hand and 1 discarded tile
        #       Kan         : three tiles from player hand and 1 discarded tile
        #       Natural Kan : all four tiles from players hand

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
        current_hand = self.hand
        temp : Tile = current_hand[index_1]

        current_hand[index_1] = current_hand[index_2]
        current_hand[index_2] = temp

        self.hand = current_hand        


    # method to allow a player to select a specific tile to discard at the end of the turn
    def discard(self, tile_to_discard: int):
        # get metadata of selected Tile
        discard_copy = self.tiles[tile_to_discard]

        # remove tile from hand
        self.tiles = self.tiles - self.tiles[tile_to_discard]

        # return Tile to caller so that Tile can be 'moved' to DiscardPile
        return discard_copy


    # method to (if a player runs out of time on their turn) force them to discard their newly-drawn tile
    def force_discard(self, drawn_tile: int):
        # get metadata of drawn Tile
        discard_copy = self.tiles[drawn_tile]

        # remove tile from hand
        self.tiles = self.tiles - self.tiles[drawn_tile]

        # return Tile to caller so that Tile can be 'moved' to DiscardPile
        return discard_copy


    #   Going to create an equivalent tile set, but in an order 
    #       such that it is ordered (first by suit, then by value)
    def sort_tiles(self):
        pass

     # Ensure player has correct number of tiles at all times
    def validate_hand_size(self):

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