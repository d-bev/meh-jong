
class Tile():

    def __init__(self, suit: str, value : str):
        # Attributes a Tile MUST have
        self.__suit = suit
        self.__value = value
        # Attributes a Tile MIGHT have
        self.__is_dora = False
        self.__is_ura_dora = False
        self.__is_red_five = False


# Getters

    @property
    def is_dora(self):
        return self.__is_dora

    @property
    def is_ura_dora(self):
        return self.__is_ura_dora

    @property
    def is_red_five(self):
        return self.__is_red_five

# Setters

    @is_dora.setter
    def is_dora(self, boolean: bool):
        self.__is_dora = boolean

    @is_ura_dora.setter
    def is_ura_dora(self, boolean: bool):
        self.__is_ura_dora = boolean

    @is_red_five.setter
    def is_red_five(self, boolean: bool):
        self.__is_red_five = boolean