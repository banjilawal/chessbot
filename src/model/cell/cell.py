from dataclasses import dataclass, field
from typing import Optional

from model.board.grid_coordinate import Coordinate
from common.game_color import GameColor
from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError
from src.model.occupant.obstacle import Obstacle


@dataclass
class Cell:
    id: int
    coordinate: Coordinate
    color: GameColor = field(default=GameDefault.CELL_COLOR)
    occupant: Optional['Obstacle'] = field(default=None)

    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Cell id below minimum value.")
        object.__setattr__(self, 'id', self.id)
        object.__setattr__(self, 'coordinate', self.coordinate)
        object.__setattr__(self, 'color', self.color)
        object.__setattr__(self, 'occupant', self.occupant)
