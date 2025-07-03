from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING

from model.board.grid_coordinate import GridCoordinate
from common.game_color import GameColor
from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError

if TYPE_CHECKING:
    from model.occupant.occupant import Occupant


@dataclass
class Cell:
    id: int
    coordinate: GridCoordinate
    occupant: Optional['Occupant'] = field(default=None)

    def __post_init__(self):
        if self.id < GameDefault.MIN_ID:
            raise InvalidIdError("Cell id below minimum value.")
        object.__setattr__(self, 'id', self.id)
        object.__setattr__(self, 'coordinate', self.coordinate)
        object.__setattr__(self, 'occupant', self.occupant)
