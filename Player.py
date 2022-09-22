from Hand import *

class Player():
    def __init__(self, name:str, starting_tiles:list):
        self.__name = name
        self.__hand = Hand(starting_tiles)
        self.__score = 0

        # TODO:     might need a variable to store the '14th' tile in each player's hand:
        #           the tile they draw at the start of the turn
        #           the tile another player discards

        # TODO:     how to track what tiles Player has called
    

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


    #   CLASS METHODS
    @classmethod
    def call_chi():
        # take tile discarded by previous player
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player discard
        pass

    @classmethod
    def call_pon():
        # take tile discarded by previous player
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player discard
        pass

    @classmethod
    def call_open_kan():
        # take tile discarded by previous player
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player discard
        pass

    @classmethod
    def call_closed_kan():
        # move tiles to __table_side
        # make called_tile perpendicular
        # make player draw a tile
        # flip next Dora Indicator in Dead Wall
        # make player discard
        pass

    @classmethod
    def call_kita():
        # move tile to __table_side
        # player draws a tile
        # make player discard
        pass

    @classmethod
    def call_ron():
        # take tile discarded by previous player
        # evaluate point value of player's hand
        pass

    @classmethod
    def call_tsumo():
        # evaluate point value of player's hand
        pass