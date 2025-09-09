from abc import abstractmethod, ABC
from typing import Optional

from chess.board.board import Board
from chess.system.command import Command


class Flow(ABC):

    @staticmethod
    @abstractmethod
    def enter(request: Command, board: Optional[Board]):
        pass
