import Tile
import Hand
import random


class Dealer():

    # you ask the 'dealer' to give you tiles to play with,
    #   for {num_copies} players and {with/without} Red Fives
    
    def __init__(self, num_copies : int, red_fives : bool):
        self.__num_tile_copies = num_copies
        self.__red_fives = red_fives
        self.__tile_list : list = []

        # There can't be Red Fives for Winds nor Dragons
        excluded_suits = [3, 4]

        # Create 'num_copies' worth of copies for each kind of tile
        for i in range(num_copies):

            # For each suit, create tiles 1 through 9
            for suit in range(3):
                for val in range(1, 10):
                    new_tile = Tile.Tile(suit, val)

                    if red_fives and (val == 5) and (suit not in excluded_suits):
                        new_tile.is_red_five = True
                        excluded_suits.append(suit)
                    
                    self.__tile_list.append( new_tile )

            # Add a copy of each wind
            self.__tile_list.append( Tile.Tile(3, 10) )   # Tile.__init__
            self.__tile_list.append( Tile.Tile(3, 11) )
            self.__tile_list.append( Tile.Tile(3, 12) )
            self.__tile_list.append( Tile.Tile(3, 13) )

            # Add a copy of each dragon
            self.__tile_list.append( Tile.Tile(4, 14) )
            self.__tile_list.append( Tile.Tile(4, 15) )
            self.__tile_list.append( Tile.Tile(4, 16) )

        # Shuffle the tiles after
        random.shuffle(self.__tile_list)   


    def __str__(self):
        string : str = ""
        for num, attr in enumerate(self.__tile_list):
            string += f"{num}\t{str(attr)}\n"

        return string


    def __repr__(self) -> str:
        string : str = ""
        for num, attr in enumerate(self.__tile_list):
            string += f"{num}\t{repr(attr)}\n"

        return string   


    """
        CORE FUNCTIONS
    """    


    # pass tiles from the dealer's tileset to a player (for the player to then put in heir hand)
    def deal(self):
        newTiles : list = []
        
        for i in range(13):
            newTiles.append(self.__tile_list.pop())

        return newTiles


    """
        HELPER FUNCTIONS
    """


    def tilesLeft(self):
        return len(self.__tile_list)