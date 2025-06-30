from abc import ABC
from dataclasses import dataclass
from typing import Optional, List

from gi.overrides.Gdk import Color

from game.model.cell.cell import Cell
from game.common.game_coordinate import GameCoordinate


@dataclass
class Occupier(ABC):
    _id: int
    _color: Color
    _length: int
    _height: int
    _coordinates: [GameCoordinate]
    _squares: Optional[List[Cell]]

    def __init__(self, _id: int, color: Color, length: int, height: int):
        self._id = _id
        self._color = color
        self._length = length
        self._height = height

        self._coordinates = [GameCoordinate]
        self.square = Optional[List[Cell]]

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