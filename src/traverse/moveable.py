from abc import ABC, abstractmethod

from src.model.board.game_board import GameBoard
from src.common.coordinate import Coordinate
from src.model.occupant.obstacle import Obstacle


class Moveable(ABC):

    @abstractmethod
    def move(self, board: GameBoard, figure: Obstacle, destination: Coordinate):
        pass