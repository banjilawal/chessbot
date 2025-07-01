from dataclasses import dataclass, field
from email.policy import default
from typing import Optional

from common.game_color import GameColor
from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError, NegativeRowError, NegativeColumnError
from src.model.occupant.obstacle import Obstacle


@dataclass
class Cell:
    id: int
    row: int
    column: int
    color: GameColor = field(default=GameDefault.CELL_COLOR)
    occupant: Optional['Obstacle'] = field(default=None)

    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Cell id below minimum value.")
        if self.row < 0:
            raise NegativeRowError("Cell cannot be on a negative row.")
        if self.column < 0:
            raise NegativeColumnError("Cell cannot be on a negative column.")
        object.__setattr__(self, 'id', self.id)
        object.__setattr__(self, 'row', self.row)
        object.__setattr__(self, 'column', self.column)
        object.__setattr__(self, 'color', self.color)
        object.__setattr__(self, 'occupant', self.occupant)
