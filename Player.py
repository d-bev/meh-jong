from Hand import *

class Player():
    def __init__(self, name:str, starting_tiles:list):
        self.__name = name
        self.__hand = Hand(starting_tiles)
        self.__score = 0

        # Handling the '14th' tile in each player's hand:
        #   the tile they draw at the start of the turn
        #   the tile another player discards
    

    #   GETTERS


    @property
    def name(self):
        return self.__name
        
    @property
    def hand(self):
        return self.__hand

    @property
    def score(self):
        return self.__score


    #   SETTERS


    @name.setter
    def name(self, new_name:str):
        self.__name = new_name

    @hand.setter
    def hand(self, new_hand:list):
        self.__hand = Hand(new_hand)

    @score.setter
    def score(self, new_score:int):
        self.__score = new_score