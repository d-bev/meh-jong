#   CLASS : Hand
#
#   DESCRIPTION:
#       Stores a list of tiles for a given player.
#       Whenever a player draws, discards, or calls a tile, Player() will call a method on Hand


#   INPUT:
#
#   OUTPUT:
#
#   FUNCTIONS:
#
#
#
#

class Hand():
    def __init__(self, starting_tiles:list):
        self.__tiles : list = starting_tiles
        self.__called_tiles : list = None


    #   GETTERS 

    @property
    def tiles(self):
        return self.__tiles

    @property
    def aside(self):
        return self.__called_tiles


    #   SETTERS

    @tiles.setter
    def tiles(self, new_hand : list):
        self.__tiles = new_hand

    @aside.setter
    def add_tile(self, new_tile):
        self.__called_tiles.append(new_tile)


    #   CLASS METHODS

    @classmethod
    def swap_tiles(self, index_1, index_2):
        # method to allow player to re-order the tiles in their hands
        pass

    @classmethod
    def discard(self, tile_to_discard):
        pass

    """
    @classmethod
    def sort_tiles:
        # sort tiles first by suit 
        #       chars < circles < bamboos < winds < dragons
        # sort tiles by value
    """