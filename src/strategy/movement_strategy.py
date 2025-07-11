from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional


from model.grid_coordinate import GridCoordinate
from model.grid_entity import Mover

if TYPE_CHECKING:
    from model.board import Board


class MovementStrategy(ABC):
    @abstractmethod
    def move(self, mover: Mover, board: 'Board', destination_coordinate: GridCoordinate) -> bool:
        pass
