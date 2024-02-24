

class Tile():

    def __init__(self, id: int):
        self.__id = id

    def __str__(self):
        s : str

        match self.id:    
            # CHARACTERS  
            case 0:
                s = "1 of characters"
            case 1:
                s = "2 of characters"
            case 2:
                s = "3 of characters"
            case 3:
                s = "4 of characters"
            case 4:
                s = "5 of characters"
            case 5:
                s = "5 of characters (red)"
            case 6:
                s = "6 of characters"
            case 7: 
                s = "7 of characters"
            case 8: 
                s = "8 of characters"
            case 9:
                s = "9 of characters"
            # CIRCLES
            case 10:
                s = "1 of circles"
            case 11:
                s = "2 of circles"
            case 12:
                s = "3 of circles"
            case 13:
                s = "4 of circles"
            case 14:
                s = "5 of circles"
            case 15:
                s = "5 of circles (red)"
            case 16:
                s = "6 of circles"
            case 17: 
                s = "7 of circles"
            case 18: 
                s = "8 of circles"
            case 19:
                s = "9 of circles"
            # BAMBOO
            case 20:
                s = "1 of bamboo"
            case 21:
                s = "2 of bamboo"
            case 22:
                s = "3 of bamboo"
            case 23:
                s = "4 of bamboo"
            case 24:
                s = "5 of bamboo"
            case 25:
                s = "5 of bamboo (red)"
            case 26:
                s = "6 of bamboo"
            case 27: 
                s = "7 of bamboo"
            case 28: 
                s = "8 of bamboo"
            case 29:
                s = "9 of bamboo"
            # WINDS
            case 30:
                s = "east wind"
            case 31:
                s = "south wind"
            case 32:
                s = "west wind"
            case 33:
                s = "north wind"
            # DRAGONS
            case 34:
                s = "green dragon"
            case 35:
                s = "red dragon"
            case 36:
                s = "white dragon"

        return s
        
    @property
    def id(self):
        return self.__id
    