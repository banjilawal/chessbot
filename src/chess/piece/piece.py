from dataclasses import dataclass

from chess.geometry.coordinate.coordinate import Coordinate
from chess.geometry.coordinate.coordinate_stack import CoordinateStack
from chess.piece.mobility_status import MobilityStatus
from chess.piece.label import Label

from typing import List, TYPE_CHECKING

from chess.transaction.failure import Failure
from chess.transaction.old_transaction_result import OldTransactionResult
from chess.square.repo.square_repo_validator import SquareRepoValidator
from chess.geometry.coordinate.coordinate_validator import CoordinateValidator
from chess.piece.piece_validator import ChessPieceValidator

if TYPE_CHECKING:
    from chess.player.player import Player
    from chess.rank.rank import Rank
    from chess.geometry.board import ChessBoard

@dataclass(frozen=True)
class RankTag:
    member_id: int
    rank: Rank


class ChessPiece:
    _id: int
    _label: Label
    _player: 'Player'
    _rank_tag: RankTag
    _coordinate_stack: CoordinateStack
    _status: MobilityStatus

    def __init__(self, piece_id: int, label: Label, rank_tag: RankTag, player: 'Player'):
        if not piece_id:
            raise ValueError("Cannot create a chess_piece with an empty id.")
        if piece_id < 0:
            raise ValueError("Cannot create a chess_piece with a negative id.")
        if rank_tag is None:
            raise ValueError("Cannot create a chess_piece with an null rank.")

        self._id = piece_id
        self._player = player
        self._rank_tag = rank_tag
        self._label = label
        self._status = MobilityStatus.FREE
        self._coordinate_stack: List[Coordinate] = []


    @property
    def id(self) -> int:
        return self._id

    @property
    def label(self) -> Label:
        return self._label


    @property
    def player(self) -> 'Player':
        return self._player


    @property
    def rank_tag(self) -> 'RankTag':
        return self._rank_tahg


    @property
    def status(self) -> MobilityStatus:
        return self._status


    @property
    def position_history(self) -> List[Coordinate]:
        return self._coordinate_stack


    @status.setter
    def status(self, status: MobilityStatus):
        if self._status != status:
            self._status = status

    def forward_move_request(self, chess_board: 'ChessBoard', destination: Coordinate) -> OldTransactionResult:
        method = "ChessPiece.forward_move_request"

        chess_piece_can_be_moved = ChessPieceValidator.can_be_moved(self)
        if chess_piece_can_be_moved.is_failure:
            return OldTransactionResult(method, Failure("The chess chess_piece cannot be moved."))

        destination_validation_result = CoordinateValidator.coordinate_exists(destination)
        if destination_validation_result.is_failure:
            return destination_validation_result

        return self._rank.delegate_move_excution(piece=self, board=chess_board, destination=destination)


    def explore_destinations(self, board: 'ChessBoard') -> List[Coordinate]:

        chess_piece_rank_validation_result = ChessPieceValidator.has_rank(self)
        if chess_piece_rank_validation_result.is_failure:
            print(f"{self._label} does not have a rank. It cannot explore without a rank.")
            return []

        board_validation_result = SquareRepoValidator.board_exists(board)
        if board_validation_result.is_failure:
            print(f"{self._label} cannot explore without a board. The board is null.")
            return []

        print(f"Everything is fine with {self._label} calling Rank.explore for the list")
        return self._rank.explore(self, board)


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, ChessPiece):
            return False
        if isinstance(other, ChessPiece):
            self.id == other.id and self.rank == other.rank
        return False


    def __hash__(self):
        return hash((self.id, self.rank))

    def __str__(self):
        return f"{self.id} {self.label} {self.status.name} stack_size:{len(self._coordinate_stack)}"

    def is_enemy(self, chess_piece: 'ChessPiece'):
        if chess_piece is None:
            print(f"{self._label} cannot be an enemy of a null chess_piece.")
            return False
        return self._player == chess_piece.player

    def __rebuild_label(self):
        old_label = self._label

        if self._player is not None:
            letters = self._player.color.name[0] + self._label.letters
            number = self._label.number % 2 + 1 # <--- This will still cause labels to cycle between 1 and 2
            self._label = Label(letters, number)

