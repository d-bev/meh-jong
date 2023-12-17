from array import *


MAX_COLS = 6
MAX_ROWS = 4

class DiscardPile():

    def __init__(self):
        self.__discards : list = []


    


    # Getters


    @property
    def discards(self):
        return self.__discards


    # Setters


    @discards.setter
    def discards(self, new_discard):
        self.discards.append(new_discard)
