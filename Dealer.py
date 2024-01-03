import Tile
import random


class Dealer():

    # you ask the 'dealer' to give you tiles to play with,
    #   for {num_copies} players and {with/without} Red Fives
    
    def __init__(self, num_copies : int, red_fives : bool):
        self.__tile_list : list = []
        self.__red_fives = red_fives

        #TODO: Implement 
        
        if red_fives:
            # skip the indeces of all '5' tiles
            for i in range(num_copies):
                for i in range(4):
                    self.__tile_list.append(Tile.Tile(i, False))
                for i in range(5, 13):
                    self.__tile_list.append(Tile.Tile(i, False))
                for i in range(14, 22):
                    self.__tile_list.append(Tile.Tile(i, False))
                for i in range(23, 34):
                    self.__tile_list.append(Tile.Tile(i, False))

            # add the non-red fives
            for i in range(3):
                self.__tile_list.append(Tile.Tile(4, False))
                self.__tile_list.append(Tile.Tile(13, False))
                self.__tile_list.append(Tile.Tile(22, False))

            # add a red 5 of each suit
            self.__tile_list.append(Tile.Tile(4, True))
            self.__tile_list.append(Tile.Tile(13, True))
            self.__tile_list.append(Tile.Tile(22, True))
        else:
            for i in range(num_copies):
                for i in range(34):
                    self.__tile_list.append(Tile.Tile(i, False))

        # Shuffle the tiles after
        random.shuffle(self.__tile_list)

        # Ensure correct number of copies of each tile
        self.validate_tileset()

    
    # GETTERS
        

    @property
    def tile_list(self):
        return self.__tile_list
    
    @property
    def red_fives(self):
        return self.__red_fives

    
    # METHODS
        
    def deal_turn(self):
        return self.__tile_list.pop()

    def deal_player(self):
        tiles : list = []
        
        for i in range(13):
            tiles.append(self.__tile_list.pop())

        return tiles
    
    
    def deal_wall(self):
        tiles : list = []
        
        for i in range(10):
            tiles.append(self.__tile_list.pop())

        return tiles


    def remaining(self):
        print(f"Dealer has %d tiles" % (len(self.__tile_list)))
    

    # TESTING


    def validate_tileset(self):
        freq = {}
        for i in range(len(self.__tile_list)):
            item : Tile = self.__tile_list[i]

            if (item.id in freq):
                freq[item.id] += 1
            else:
                freq[item.id] = 1
    
        for key, value in freq.items():
            if value != 4:
                print(f"only (%d) copies of Tile #%d" % (value, key))

 