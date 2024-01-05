

class Tile():

    def __init__(self, id: int):
        self.__id = id

    def __str__(self):
        s : str

        match self.id:
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
                s = "6 of characters"
            case 6: 
                s = "7 of characters"
            case 7: 
                s = "8 of characters"
            case 8:
                s = "9 of characters"
            case 9:
                s = "1 of circles"
            case 10:
                s = "2 of circles"
            case 11:
                s = "3 of circles"
            case 12:
                s = "4 of circles"
            case 13:
                s = "5 of circles"
            case 14:
                s = "6 of circles"
            case 15: 
                s = "7 of circles"
            case 16: 
                s = "8 of circles"
            case 17:
                s = "9 of circles"
            case 18:
                s = "1 of bamboo"
            case 19:
                s = "2 of bamboo"
            case 20:
                s = "3 of bamboo"
            case 21:
                s = "4 of bamboo"
            case 22:
                s = "5 of bamboo"
            case 23:
                s = "6 of bamboo"
            case 24: 
                s = "7 of bamboo"
            case 25: 
                s = "8 of bamboo"
            case 26:
                s = "9 of bamboo"
            case 27:
                s = "east wind"
            case 28:
                s = "south wind"
            case 29:
                s = "west wind"
            case 30:
                s = "north wind"
            case 31:
                s = "green dragon"
            case 32:
                s = "red dragon"
            case 33:
                s = "white dragon"
            case 34:
                s = "5 of characters (red)"
            case 35:
                s = "5 of circles (red)"
            case 36:
                s = "5 of bamboo (red)"
        return s
        
    @property
    def id(self):
        return self.__id
    