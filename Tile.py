

# Decoding of integer values to readable values
DECODED_SUITS = ['chars', 'circles', 'bamboo', 'winds', 'dragons']
DECODED_VALS = ['NULL', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'East', 'South', 'West', 'North', 'Green', 'Red', 'White']

class Tile():

    def __init__(self, suit: int, value: int):
        # Attributes a Tile MUST have
        self.__suit = suit
        self.__value = value

        # Attributes a Tile MIGHT have
        self.__is_dora = False
        self.__is_ura_dora = False
        self.__is_red_five = False

    def __str__(self):
        return f"{DECODED_VALS[self.value]}\tof {DECODED_SUITS[self.suit]}"

    def __repr__(self) -> str:
        return f"Value: {DECODED_VALS[self.value]}\tSuit: {DECODED_SUITS[self.suit]}\tDora: {self.is_dora}  Ura-Dora: {self.is_ura_dora}  Red-Five: {self.is_red_five}"

# Getters
    @property
    def suit(self):
        return self.__suit

    @property
    def value(self):
        return self.__value

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