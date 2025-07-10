from abc import ABC, abstractmethod

from common.direction import Direction
from model.grid import Grid
from model.grid_entity import GridEntity


class MovementStrategy(ABC):
    @abstractmethod
    def move(self, mover: GridEntity, grid: Grid, direction: Direction, distance: int = 1):
        if mover is None:
            print("[Warning] Mover cannot be None.")
            return
        if grid is None:
            print("[Warning] Grid cannot be None.")
            return
        if mover.coordinate is None:
            print("[Warning] Mover has no coordinate.")
            return
        if direction is None:
            print("[Warning] Direction cannot be None.")
            return
        if distance < 0:
            print("[Warning] Distance cannot be negative.")
            return
        pass