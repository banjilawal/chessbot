from dataclasses import dataclass


@dataclass
class Coordinate:
    bottom_left: int
    bottom_right: int
    top_left: int
    top_right: int
    right: int