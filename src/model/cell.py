from dataclasses import dataclass, field
from typing import Optional

from src.common.constants import Config
from src.exception.exception import InvalidIdError
from model.grid_coordinate import GridCoordinate


@dataclass
class Cell:
    id: int
    coordinate: GridCoordinate
    occupant: Optional['GridEntity'] = field(default=None)

    def __post_init__(self):
        if self.id < Config.MIN_ID:
            raise InvalidIdError("Cell mover_id below minimum value.")
        object.__setattr__(self, 'mover_id', self.id)
        object.__setattr__(self, 'top_left_coordinate', self.coordinate)
        object.__setattr__(self, 'occupant', self.occupant)





