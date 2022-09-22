
class Hand():
    def __init__(self, starting_tiles:list):
        self.__tiles = starting_tiles


    #   GETTERS 

    @property
    def tiles(self):
        return self.__tiles


    #   SETTERS

    @tiles.setter
    def tiles(self, new_hand):
        self.__tiles = new_hand

    @tiles.setter
    def add_tile(self, new_tile):
        self.__tiles.append(new_tile)


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