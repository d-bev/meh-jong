import itertools
import random

suits = ['circles', 'characters', 'bamboo']
vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
dragon_colors = ['GREEN', 'WHITE', 'RED'] 
wind_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

class TileSet():

    def __init__(self):
        self.__tile_list = []

        

# Getters

    @property
    def tile_list(self):
        return self.__tile_list

# Setters

    @tile_list.setter
    def tile_list(self, new_tiles: list):
        self.__tile_list = new_tiles

# Class Methods

    @classmethod
    def shuffleSelf(self):
        new_tile_list : list = self.tile_list()
        random.shuffle(new_tile_list)
        self.tile_list(self,new_tile_list)

    @classmethod
    def generateNewTileSet(self, SET_RULES):
        new_tile_list : list = []
        num_copies : int = 4

        for i in range(num_copies):
            #   add number tiles
            new_tile_list += list(itertools.product(vals, suits))

            #   add honors tiles
            new_tile_list += list(itertools.product(dragon_colors, ['dragon']))
            new_tile_list += list(itertools.product(wind_directions, ['wind']))

            random.shuffle(new_tile_list)
        
        self.tile_list(self, new_tile_list)
        