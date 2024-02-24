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
            # add 4 copies of each tile that isn't a 5
            for i in range(4):
                for i in range(37):
                    # exclude all 5's
                    if i not in [4, 5, 14, 15, 24, 25]:
                        self.__tile_list.append(Tile.Tile(i))

            # add 3 copies of each normal 5
            for i in range(3):
                self.__tile_list.append(Tile.Tile(4))
                self.__tile_list.append(Tile.Tile(14))
                self.__tile_list.append(Tile.Tile(24))

            # add a red 5 to each suit
            self.__tile_list.append(Tile.Tile(5))
            self.__tile_list.append(Tile.Tile(15))
            self.__tile_list.append(Tile.Tile(25))

        elif (not red_fives) and num_players == 4:
            # add 4 copies of each tile, but skip red 5's
            for i in range(4):
                for i in range(37):
                    # exclude red 5's
                    if i not in [5, 15, 25]:
                        self.__tile_list.append(Tile.Tile(i))

        elif red_fives and num_players == 3:
            # 4 copies of each tile (except 5's), and no non-terminal bamboo
            for i in range(4):
                for i in range(37):
                    # exclude all 5's and all non-terminal bamboo
                    if i not in [4, 5, 14, 15, 21, 22, 23, 24, 25, 26, 27, 28]:
                        self.__tile_list.append(Tile.Tile(i))

            # add the non-red 5's
            for i in range(3):
                self.__tile_list.append(Tile.Tile(4))
                self.__tile_list.append(Tile.Tile(14))

            # add the red 5's
            self.__tile_list.append(Tile.Tile(5))
            self.__tile_list.append(Tile.Tile(15))

        elif (not red_fives) and num_players == 3:
            # add 4 copies of each tile, but no red 5's nor non-terminal bamboo
            for i in range(4):
                for i in range(37):
                    # exclude red 5's and all non-terminal bamboo
                    if i not in [5, 15, 21, 22, 23, 24, 25, 26, 27, 28]:
                        self.__tile_list.append(Tile.Tile(i))
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

        
    # returns a single tile
    def deal_turn(self):
        return self.tile_list.pop()

    # returns 13 tiles
    def deal_player(self):
        tiles : list = []
        
        for i in range(13):
            tiles.append(self.tile_list.pop())

        return tiles
    
    # returns 10 tiles
    def deal_wall(self):
        tiles : list = []
        
        for i in range(10):
            tiles.append(self.tile_list.pop())

        return tiles


    # TESTING


    # returns how many tiles the dealer has left
    def remaining(self):
        return len(self.tile_list)

    # ensures the tileset has the expected frequency of each tile (dictated by game rules)
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
                if key in [4, 14, 24]: # if tile is a non-red five, should only ever be 3
                    if value != 3:
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 3\n" % (value, key)
                elif key in [5, 15, 25]: # if tile is a red five, should only ever be 1
                    if value != 1:
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 1\n" % (value, key)
                else:
                    if value != 4: # if tile isn't a five, should only ever be 4
                        is_valid = False
                        error += f"counted (%d) copies of Tile #%d, but expected 4\n" % (value, key)
        elif (not red_fives) and num_players == 4:
            for key, value in freq.items():
                if value != 4:
                    is_valid = False
                    error += f"counted (%d) copies of Tile #%d, but expected 4\n" % (value, key)
        elif red_fives and num_players == 3:
            # TODO: implement 3-player tileset checks
            pass
        elif (not red_fives) and num_players == 3:
            if [21, 22, 23, 24, 25, 26, 27, 28] in freq.items():
                error += "tileset contains non-terminal bamboo!\n"
            else:
                # TODO: implement 3-player tileset checks
                pass
        else:
            print("EOC REACHED IN VALIDATE_TILESET")
    
        if is_valid == False:
            print(error)
        
        return is_valid

 