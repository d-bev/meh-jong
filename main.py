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

# for i in range(len(new_game.players)):
#     new_game.players[i].hand = new_hands_and_wall[i]
# new_game.dead_wall = new_hands_and_wall[-1:]
