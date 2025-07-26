from abc import abstractmethod, ABC
from typing import Optional, List, Dict, TYPE_CHECKING

from chess.geometry.board import Board
from chess.common.constant import GameColor
from chess.geometry.coordinate import Coordinate
from chess.geometry.quadrant import Quadrant

from chess.piece.piece import Piece, Label
from chess.game.record.turn_record import TurnRecord
from chess.rank.rank_value import RankValue

if TYPE_CHECKING:
    from chess.geometry.board import Board
    from chess.piece.piece import Piece

class Player(ABC):
    _id: int
    _name: str
    _color: GameColor
    _captives: List['Piece']
    _home_quadrant: Quadrant
    _pieces: Dict[RankValue, List['Piece']]
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
    def color(self) -> GameColor:
        return self._color

    @property
    def captives(self) -> List['Piece']:
        return self._captives.copy()

    @property
    def pieces(self) -> Dict[RankValue, List[Piece]]:
        return self._pieces.copy()

    @property
    def home_quadrant(self) -> Quadrant:
        return self._home_quadrant


    @abstractmethod
    def advance_piece(
        self,
        piece: 'Piece',
        destination: Coordinate,
        board: 'Board'
    ) -> Optional[TurnRecord]:
        pass

    @abstractmethod
    def hunt(self, board: 'Board') -> Dict[Label, List[Piece]]:
        pass

    @abstractmethod
    def prepare_kill_list(self) -> List['Piece']:
        pass

    @abstractmethod
    def select_killer(self) -> 'Piece':
        pass

    @abstractmethod
    def select_target(self, board: 'Board') -> Optional[TurnRecord]:
        pass


    # @staticmethod
    # def occupy_destination(self, piece: Piece, destination: Coordinate, board: Board):
    #    if piece is None:
    #        print("Bishop is None")
    #        return None
    #    if piece.current_position() is None:
    #        print("Bishop current position is None.")
    #
    #        return None
    #    if board is None:
    #        print("Board is None")
    #        return None
    #    if not board.coordinate_is_valid(destination):
    #        print("Destination is not valid")
    #        return None
    #    if not DiagonalPattern.points_match_pattern(piece.current_position(), destination):
    #        print("points are not in diagonal pattern")
    #        return
    #    board.capture_square(piece, destination)