from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

from common.direction import Direction
from model.grid_coordinate import GridCoordinate
from model.grid_entity import GridEntity

if TYPE_CHECKING:
    from model.grid import Grid


class MovementStrategy(ABC):
    @abstractmethod
    def move(self, mover: GridEntity, grid: 'Grid', direction: Direction, distance: int = 1) -> Optional[GridCoordinate]:
        pass
