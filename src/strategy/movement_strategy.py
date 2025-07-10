from abc import ABC, abstractmethod

from common.direction import Direction
from model.grid import Grid
from model.grid_entity import GridEntity


class MovementStrategy(ABC):
    @abstractmethod
    def move(self, mover: GridEntity, grid: Grid, direction: Direction, distance: int = 1):
        pass