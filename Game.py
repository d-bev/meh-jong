from tracemalloc import start
from Player import *
from TileSet import *



class Game():
    def __init__(self, NUM_PLAYERS:int, PLAYERS_NAMES:list=["1","2","3","4"]):
        self.__num_players = NUM_PLAYERS
        self.__players = list()
        self.__tile_set = TileSet(NUM_PLAYERS)
        self.__dead_wall = list()
        self.__dora_counter = 0

        for i in range(NUM_PLAYERS):
            starting_hand : list = self.tile_set.tiles[0:13]
            self.players.append(Player(PLAYERS_NAMES[i],starting_hand))
            del self.tile_set.tiles[:13]

        self.dead_wall.append(self.tile_set.tiles[-10:])
        del self.tile_set.tiles[-10:]


    # GETTERS

    @property
    def num_players(self):
        return self.__num_players

    @property
    def players(self):
        return self.__players

    @property
    def tile_set(self):
        return self.__tile_set

    @property
    def dead_wall(self):
        return self.__dead_wall


    # SETTERS
    
    @num_players.setter
    def num_players(self, new_player_count):
        self.__num_players = new_player_count

    @tile_set.setter
    def tile_set(self, new_tile_set):
        self.__tile_set = new_tile_set

    @players.setter
    def players(self, list_of_players):
        self.__players = list_of_players

    @dead_wall.setter
    def dead_wall(self, new_wall):
        self.__dead_wall = new_wall


    # CLASS METHODS

    @classmethod
    def deal_new_hands(self, NUM_PLAYERS):
        self.tile_set = TileSet(NUM_PLAYERS)
        new_hands = []

        for i in range(NUM_PLAYERS):
            starting_hand : list = self.tile_set.tiles[0:13]
            new_hands.append(starting_hand)
            del self.tile_set.tiles[:13]

        new_hands.append(self.tile_set.tiles[-10:])
        del self.tile_set.tiles[-10:]

        return new_hands

    @classmethod
    def flip_new_dora(self):
        pass            

    @classmethod
    def nextRound(self):
        #determine if we should advance to next round, or to end the game
        # gameEnd() or self.gameEnd() ?
        pass

    @classmethod
    def gameEnd(self):
        # compare scores of players
        pass


