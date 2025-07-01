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
