import Tile
import random


class Dealer():

    # you ask the 'dealer' to give you tiles to play with,
    #   for {num_copies} players and {with/without} Red Fives
    
    def __init__(self, num_copies : int, red_fives : bool):
        self.__tile_list : list = []

        
        for i in range(num_copies):
            for i in range(33):
                self.__tile_list.append(Tile.Tile(i))

        if red_fives:
            # remove a 5 from each suit
            self.tile_list.remove(4)
            self.tile_list.remove(13)
            self.tile_list.remove(22)

            # add a red 5 to each suit
            self.tile_list.append(34)
            self.tile_list.append(35)
            self.tile_list.append(36)

        # Shuffle the tiles after
        random.shuffle(self.__tile_list)   

    
    # GETTERS
        

    @property
    def tile_list(self):
        return self.__tile_list
    
    
    # SETTERS


    @tile_list.setter
    def tile_list(self, l : list):
        self.__tile_list = l

    
    # FUNCTIONS


    def deal(self):
        newTiles : list = []
        
        for i in range(13):
            newTiles.append(self.__tile_list.pop())

        return newTiles


    def remaining(self):
        return len(self.__tile_list)