from enum import Enum
import helper

characters_string = ["rouge", "rose", "gris", "bleu", "violet", "marron", "noir", "blanc"]


class Color(Enum):
    RED = 0
    PINK = 1
    GREY = 2
    BLUE = 3
    PURPLE = 4
    BROWN = 5
    BLACK = 6
    WHITE = 7
    NONE = 8


class Character:
    def __init__(self, _color, _position, _suspect):
        self.color = _color
        self.position = _position
        self.suspect = _suspect

    def dump(self):
        print("  "+str(self.color)+", position: "+str(self.position)+", suspect: "+str(self.suspect))

    def get_character_color_to_string(self):
        return characters_string[self.color]

    @staticmethod
    def convert_from_tile_color(tile_color: helper.Tuile.Color):
        conversion = [[Color.RED, helper.Tuile.Color.rouge], [Color.PINK, helper.Tuile.Color.rose],
                      [Color.GREY, helper.Tuile.Color.gris], [Color.BLUE, helper.Tuile.Color.bleu],
                      [Color.PURPLE, helper.Tuile.Color.violet], [Color.BROWN, helper.Tuile.Color.marron],
                      [Color.BLACK, helper.Tuile.Color.noir], [Color.PURPLE, helper.Tuile.Color.blanc]]
        for c in conversion:
            if c[1] == tile_color:
                return c[0]
