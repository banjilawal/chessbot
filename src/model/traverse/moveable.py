from abc import ABC, abstractmethod

from src.model.board.board import Board
from model.board.grid_coordinate import GridCoordinate
from src.model.occupant.obstacle import Obstacle


class Moveable(ABC):

    @abstractmethod
    def move(self, board: Board, figure: Obstacle, destination: GridCoordinate):
        pass