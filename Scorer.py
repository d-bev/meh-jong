import Tile



class Scorer():

    def __init__(self, winner : list):
        self.__full_flush : bool = False
        self.__half_flush : bool = False
        self.__half_outside : bool = False
        self.__full_outside : bool = False
        self.__num_triples : int = 0
        self.__num_quads : int = 0
        self.__hand = winner
        self.__tile_dict = {}

        """
            Attempting to create a dictionary of key-value pairs, where
                the key is a tile in the winning hand, and the value is 
                the frequency of said tile in the winning hand

            The idea behind this dictionary being that it simplifies a 
                lot of the expense and problems that come with extensive
                pattern-matching (i.e. if I need to check)
        """
        
        tiles = {}

        for i in winner.tiles:
            temp : Tile = winner.tiles.pop()

            if temp in tiles:
                tiles[temp] += 1
            else:
                tiles[temp] = 1

        self.tile_dict = tiles


    def print_dict(self):
        tiles = self.tile_dict
        for key, value in tiles.items():
            print("% s \t: % d" % (key, value))


    # GETTERS
        

    @property
    def full_flush(self):
        return self.__full_flush
    
    @property
    def half_flush(self):
        return self.__half_flush
    
    @property
    def full_outside(self):
        return self.__full_outside
    
    @property
    def half_outside(self):
        return self.__half_outside
    
    @property
    def num_triples(self):
        return self.__num_triples
    
    @property
    def num_quads(self):
        return self.__num_quads
    
    @property
    def hand(self):
        return self.__hand
    
    @property
    def tile_dict(self):
        return self.__tile_dict

        
    # SETTERS

        
    @full_flush.setter
    def full_flush(self, b : bool):
        self.__full_flush = b

    @half_flush.setter
    def half_flush(self, b : bool):
        self.__half_flush = b

    @full_outside.setter
    def full_outside(self, b : bool):
        self.__full_outside = b

    @half_outside.setter
    def half_outside(self, b : bool):
        self.__half_outside = b

    @num_triples.setter
    def num_triples(self, i : int):
        if (0 <= i and i <= 4):
            self.__num_triples = i
        else:
            ValueError(self)

    @num_quads.setter
    def num_quads(self, i : int):
        if (0 <= i and i <= 3):
            self.__num_quads = i
        else:
            ValueError(self)

    @hand.setter
    def hand(self, hand : list):
        self.__hand = hand

    @tile_dict.setter
    def tile_dict(self, tiles : dict):
        self.__tile_dict = tiles


    # FUNCTIONS