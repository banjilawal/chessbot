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
    color: GameColor
    occupant: Optional['Obstacle'] = field(default=None)

    def __init__(self, id: int, row: int, column: int, color: GameColor=GameColor.LIGHT_GRAY_2):
        if id < GameDefault.MINIMUM_ID:
            raise InvalidIdError("Cell id below minimum value.")
        if row < 0:
            raise NegativeRowError("Cell cannot be on a negative row.")
        if column < 0:
            raise NegativeColumnError("Cell cannot be on a negative column.")

        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'row', row)
        object.__setattr__(self, 'column', column)
        object.__setattr__(self, 'occupant', None)
        object.__setattr__(self, 'color', color)
