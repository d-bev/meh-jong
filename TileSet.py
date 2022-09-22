import itertools
import random

suits = ['circles', 'characters', 'bamboo']
vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
dragon_colors = ['GREEN', 'WHITE', 'RED'] 
wind_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

class TileSet():

    def __init__(self, NUM_TILE_COPIES:int):
        self.__tile_list = []

        for i in range(NUM_TILE_COPIES):
            #   add number tiles
            self.__tile_list += list(itertools.product(vals, suits))

            #   add honors tiles
            self.__tile_list += list(itertools.product(dragon_colors, ['dragon']))
            self.__tile_list += list(itertools.product(wind_directions, ['wind']))

            random.shuffle(self.__tile_list)


    #   GETTERS

    @property
    def tiles(self):
        return self.__tile_list


    #   SETTERS

    @tiles.setter
    def tiles(self, new_tiles: list):
        self.__tile_list = new_tiles


    #   CLASS METHODS