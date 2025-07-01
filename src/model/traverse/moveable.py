from abc import ABC, abstractmethod

from src.model.board.board import Board
from model.board.grid_coordinate import GridCoordinate
from src.model.occupant.occupant import Occupant


class Moveable(ABC):

    @abstractmethod
    def move(self, board: Board, figure: Occupant, destination: GridCoordinate):
        pass