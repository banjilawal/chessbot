from dataclasses import dataclass, field
from typing import Optional

from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError
from model.grid_coordinate import GridCoordinate


@dataclass
class Cell:
    cell_id: int
    coordinate: GridCoordinate
    occupant: Optional['GridEntity'] = field(default=None)

    def __post_init__(self):
        if self.cell_id < GameDefault.MIN_ID:
            raise InvalidIdError("Cell cell_id below minimum value.")
        object.__setattr__(self, 'cell_id', self.cell_id)
        object.__setattr__(self, 'coordinate', self.coordinate)
        object.__setattr__(self, 'occupant', self.occupant)





