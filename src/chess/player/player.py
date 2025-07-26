from abc import abstractmethod, ABC
from typing import Optional, List, Dict

from chess.board.board import Board
from chess.common.constant import GameColor
from chess.common.geometry import Coordinate
from chess.common.piece import Piece, Label
from chess.game.record.turn_record import TurnRecord
from chess.rank.rank_value import RankValue
from chess.team.team import Team


class Player(ABC):
    _id: int
    _name: str
    _color: GameColor
    _captives: List[Piece]
    _pieces: Dict[RankValue, List[Piece]]
    def __init__(self, player_id: int, name: str, color: GameColor):
        self._id = player_id
        self._name = name
        self._color = color
        self._captives = []
        self._pieces = {}

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def team(self) -> Team:
        return self._team

    @property
    def color(self) -> GameColor:
        return self._color

    @abstractmethod
    def advance_piece(
        self,
        piece: Piece,
        destination: Coordinate,
        board: Board
    ) -> Optional[TurnRecord]:
        pass

    @abstractmethod
    def hunt(self, board: Board) -> Dict[Label, List[Piece]]:
        pass

    @abstractmethod
    def prepare_kill_list(self) -> List[Piece]:
        pass

    @abstractmethod
    def select_killer(self) -> Piece:
        pass

    @abstractmethod
    def select_target(self, board: Board) -> Optional[TurnRecord]:
        pass