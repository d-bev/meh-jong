import Tile
import random


class Dealer():

    # you ask the 'dealer' to give you tiles to play with,
    #   for {num_copies} players and {with/without} Red Fives
    
    def __init__(self, num_copies : int, red_fives : bool):
        self.__tile_list : list = []
        self.__red_fives = red_fives
        self.__num_copies = num_copies
        
        if red_fives:
            # skip the indeces of all '5' tiles
            for i in range(num_copies):
                for i in range(4):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(5, 13):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(14, 22):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(23, 34):
                    self.__tile_list.append(Tile.Tile(i))

            # add the non-red fives
            for i in range(3):
                self.__tile_list.append(Tile.Tile(4))
                self.__tile_list.append(Tile.Tile(13))
                self.__tile_list.append(Tile.Tile(22))

            # add a red 5 of each suit
            self.__tile_list.append(Tile.Tile(34))
            self.__tile_list.append(Tile.Tile(35))
            self.__tile_list.append(Tile.Tile(36))
        else:
            for i in range(num_copies):
                for i in range(34):
                    self.__tile_list.append(Tile.Tile(i))

        # Shuffle the tiles after
        random.shuffle(self.__tile_list)

        # Ensure correct number of copies of each tile
        self.validate_tileset()

    
    # GETTERS
        

    @property
    def tile_list(self):
        return self.__tile_list
    
    @property
    def num_copies(self):
        return self.__num_copies
    
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


    # TESTING


    def remaining(self):
        print(f"Dealer has %d tiles" % (len(self.__tile_list)))


    def validate_tileset(self):
        is_valid = True
        expected_value = self.num_copies
        error : str = "\n"

        freq = {}
        for i in range(len(self.__tile_list)):
            item : Tile = self.__tile_list[i]

            # TODO: need to account for red fives

            if (item.id in freq):
                freq[item.id] += 1
            else:
                freq[item.id] = 1


        for key, value in freq.items():
            print(key.id)


        if self.red_fives:
            for key, value in freq.items():
                if value in [4, 13, 22]: # if tile is a non-red five, should only be (expected - 1)
                    if value != (expected_value - 1):
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected %d\n\n" % (value, key, (expected_value - 1))
                elif value in [34, 35, 36]: # if tile is a red five, should only be 1
                    if value != 1:
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 1\n\n" % (value, key)
                else:
                    if value != expected_value:
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected %d\n\n" % (value, key, expected_value)
        else:
            for key, value in freq.items():
                if value != expected_value:
                    is_valid = False
                    error += f"counted (%d) copies of Tile #%d, but expected %d\n\n" % (value, key, expected_value)
    
        if is_valid == False:
            print(error)
        
        return is_valid

 