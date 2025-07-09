from dataclasses import dataclass, field
from typing import Optional

from src.common.game_default import GameDefault
from src.exception.exception import InvalidIdError
from model.grid_coordinate import GridCoordinate


@dataclass
class Cell:
    id: int
    coordinate: GridCoordinate
    occupant: Optional['GridEntity'] = field(default=None)
    door: Optional['Portal'] = field(default=None)

def __post_init__(self):
    if self.id < GameDefault.MIN_ID:
        raise InvalidIdError("Cell id below minimum value.")
    object.__setattr__(self, 'id', self.id)
    object.__setattr__(self, 'coordinate', self.coordinate)
    object.__setattr__(self, 'occupant', self.occupant)

def enter_cell(self, occupant: 'GridEntity'):
    """
    Allows the given occupant to enter this cell if it is unoccupied.
    Returns True if successful, False otherwise.
    """
    if self.occupant is None:
        self.occupant = occupant
        occupant.cells.append(self)

