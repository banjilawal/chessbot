from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List

from gi.overrides.Gdk import Color

from game.board.board_square import GameBoardSquare
from game.common.game_coordinate import GameCoordinate


@dataclass
class Occupier(ABC):
    _id: int
    _color: Color
    _length: int
    _height: int
    _coordinates: [GameCoordinate]
    _squares: Optional[List[GameBoardSquare]]

    def __init__(self, _id: int, color: Color, length: int, height: int):
        self._id = _id
        self._color = color
        self._length = length
        self._height = height

        self._coordinates = [GameCoordinate]
        self.square = Optional[List[GameBoardSquare]]

    @property
    def id(self):
        return self._id

    @property
    def color(self):
        return self.color

    @property
    def length(self):
        return self.length

    @property
    def height(self):
        return self.height

    @property
    def coordinates(self):
        return self.coordinates

    @property
    def squares(self):
        return self.squares

    def area(self):
        return self.length * self.height


@dataclass
class Wall(Occupier):

    def __init__(self, _id: int, color: Color, length: int, height: int):
        super().__init__(_id, color, length, height)


@dataclass
class Wall(Occupier):

    def __init__(self, _id: int, color: Color, length: int, height: int):
        super().__init__(_id, color, length, height)