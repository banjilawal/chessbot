from abc import ABC, abstractmethod

from game.model.board.game_board import GameBoard
from game.common.coordinate import Coordinate
from game.model.occupy.game_figure import GameFigure


class Moveable(ABC):

    @abstractmethod
    def move(self, board: GameBoard, figure: GameFigure, destination: Coordinate):
        pass