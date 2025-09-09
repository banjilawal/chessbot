from abc import abstractmethod, ABC
from typing import Optional

from chess.board.board import Board
from chess.system.request import Request


class Flow(ABC):

    @staticmethod
    @abstractmethod
    def enter(request: Request, board: Optional[Board]):
        pass
