from dataclasses import dataclass

from game.common.direction import Direction


@dataclass
class Side:
    orientation: Direction
    dimension: int
