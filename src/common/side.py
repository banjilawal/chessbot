from dataclasses import dataclass

from src.common.direction import Direction


@dataclass
class Side:
    orientation: Direction
    dimension: int
