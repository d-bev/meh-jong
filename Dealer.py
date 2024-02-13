import Tile
import random

DEBUG = False

class Dealer():

    # you ask the 'dealer' to give you tiles to play with,
    #   for {num_players} players and {with/without} Red Fives
    
    def __init__(self, num_players : int, red_fives : bool):
        self.__tile_list : list = []
        self.__red_fives = red_fives
        self.__num_players = num_players
        
        if red_fives and num_players == 4:
            for i in range(4):
                # skip the indeces of all '5' tiles
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

        elif (not red_fives) and (num_players == 4):
            for i in range(4):
                for i in range(34):
                    self.__tile_list.append(Tile.Tile(i))

        elif red_fives and num_players == 3:
            for i in range(4):
                # only add outside character tiles
                self.__tile_list.append(Tile.Tile(0))
                self.__tile_list.append(Tile.Tile(8))

                # skip the indeces of all '5' tiles
                for i in range(9, 13):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(14, 22):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(23, 34):
                    self.__tile_list.append(Tile.Tile(i))

            # add the non-red fives
            for i in range(3):
                self.__tile_list.append(Tile.Tile(13))
                self.__tile_list.append(Tile.Tile(22))

            # add a red 5 of each suit
            self.__tile_list.append(Tile.Tile(35))
            self.__tile_list.append(Tile.Tile(36))

        elif (not red_fives) and (num_players == 3):
            for i in range(4):
                # only add outside character tiles
                self.__tile_list.append(Tile.Tile(0))
                self.__tile_list.append(Tile.Tile(8))

                # skip the indeces of all '5' tiles
                for i in range(9, 13):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(14, 22):
                    self.__tile_list.append(Tile.Tile(i))
                for i in range(23, 34):
                    self.__tile_list.append(Tile.Tile(i))

            # add the non-red fives
            for i in range(4):
                self.__tile_list.append(Tile.Tile(13))
                self.__tile_list.append(Tile.Tile(22))
        else:
            print("\nEOC REACHED IN DEALER INIT\n")

        # Shuffle the tiles after
        random.shuffle(self.__tile_list)

        # Ensure correct number of copies of each tile
        self.validate_tileset()

    
    # GETTERS
        

    @property
    def tile_list(self):
        return self.__tile_list
    
    @property
    def num_players(self):
        return self.__num_players
    
    @property
    def red_fives(self):
        return self.__red_fives

    
    # METHODS
        
    def deal_turn(self):
        return self.tile_list.pop()

    def deal_player(self):
        tiles : list = []
        
        for i in range(13):
            tiles.append(self.tile_list.pop())

        return tiles
    
    def deal_wall(self):
        tiles : list = []
        
        for i in range(10):
            tiles.append(self.tile_list.pop())

        return tiles


    # TESTING


    def remaining(self):
        print(f"Dealer has %d tiles" % (len(self.tile_list)))


    def validate_tileset(self):
        is_valid = True
        red_fives = self.red_fives 
        num_players = self.num_players
        error : str = "\n"

        freq = {}
        for i in range(len(self.tile_list)):
            item : Tile = self.tile_list[i]

            if (item.id in freq):
                freq[item.id] += 1
            else:
                freq[item.id] = 1

        if DEBUG:
            print(f"\ncount: 4, red: {red_fives}\n")
            for key, value in freq.items():
                print(Tile.Tile(key))

        

        if red_fives and num_players == 4:
            for key, value in freq.items():
                if key in [4, 13, 22]: # if tile is a non-red five, should only be 3
                    if value != 3:
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 3\n" % (value, key)
                elif key in [34, 35, 36]: # if tile is a red five, should only be 1
                    if value != 1:
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 1\n" % (value, key)
                else:
                    if value != 4: # if tile isn't a five, should only be 4
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 4\n" % (value, key)
        elif (not red_fives) and num_players == 4:
            for key, value in freq.items():
                if value != 4:
                    is_valid = False
                    error += f"counted (%d) copies of Tile #%d, but expected 4\n" % (value, key)
        elif red_fives and num_players == 3:
            pass
        elif (not red_fives) and num_players == 3:
            if [1, 2, 3, 4, 5, 6, 7] in freq.items():
                error += "tileset contains non-terminal characters!\n"
            else:
                pass
        else:
            print("EOC REACHED IN VALIDATE_TILESET")
    
        if is_valid == False:
            print(error)
        
        return is_valid

 