from Game import *

NUM_PLAYERS = 4

new_game = Game(NUM_PLAYERS)

# print(new_game.players[0].hand.tiles)
# print(new_game.dead_wall)

new_hands_and_wall = new_game.deal_new_hands(NUM_PLAYERS)

for i in range(len(new_game.players)):
    new_game.players[i].hand = new_hands_and_wall[i]
new_game.dead_wall = new_hands_and_wall[-1:]

# print(new_game.players[0].hand.tiles)
# print(new_game.dead_wall)


"""
ASSUMPTIONS:

    4-player game
    standard tileset (riichi)
    no time limits

LOGIC:

    Game-Mode is selected and/or number of players is chosen
    A Game() object is created WITH:
        A Player() object created for each player
            has a DiscardPile()
            has a Hand()
            a default amount of points (maybe not in Player())
        A TileSet()
        ...
    
    The Game() will then take the TileSet() and 'give tiles' to each Player(), which they store in their Hand()


"""