from enum import Enum


class PieceConfig(Enum):
    def __new__(cls, name: str, symbol, number_per_player: int, capture_value: int, quadrants: [Quadrant]):
        obj = object.__new__(cls)
        obj._value_ = name
        obj._symbol = symbol
        obj._number_per_player = number_per_player
        obj._capture_value = capture_value
        obj._quadrants = quadrants
        return obj