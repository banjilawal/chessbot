from abc import ABC, abstractmethod

from game.model.board.game_board import GameBoard
from game.common.coordinate import Coordinate
from game.model.occupant.obstacle import Obstacle


class Moveable(ABC):

    @abstractmethod
    def move(self, board: GameBoard, figure: Obstacle, destination: Coordinate):
        pass