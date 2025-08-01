

from chess.geometry.board.coordinate import Coordinate
from chess.piece.mobility_status import MobilityStatus
from chess.piece.label import Label

from typing import List, Optional, TYPE_CHECKING

from chess.transaction.failure import Failure
from chess.transaction.status_code import StatusCode
from chess.transaction.transaction_result import TransactionResult
from assurance.validation.board_validator import BoardValidator
from assurance.validation.coordinate_validator import CoordinateValidator
from assurance.validation.piece_validator import ChessPieceValidator

if TYPE_CHECKING:
    from chess.player.player import Player
    from chess.rank.rank import Rank
    from chess.geometry.board import ChessBoard

class ChessPiece:
    _id: int
    _label: Label
    _rank: 'Rank'
    _player: 'Player'
    _coordinate_stack: List[Coordinate]
    _status: MobilityStatus

    def __init__(self, piece_id: int, rank: 'Rank'):
        if not piece_id:
            raise ValueError("Cannot create a chess_piece with an empty id.")
        if piece_id < 0:
            raise ValueError("Cannot create a chess_piece with a negative id.")
        if rank is None:
            raise ValueError("Cannot create a chess_piece with an null rank.")

        # rank.members.append(self)
        self._rank = rank
        self._label = Label(rank.acronym, piece_id)

        self._id = piece_id
        self._player = None
        self._status = MobilityStatus.FREE
        self._coordinate_stack: List[Coordinate] = []


    # === Immutable attributes ===
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
    def rank(self) -> 'Rank':
        return self._rank


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


    @player.setter
    def player(self, player: 'Player'):
        self._player = player
        if self not in player.chess_pieces:
            player.chess_pieces.append(self)
        self.__rebuild_label()


    def forward_move_request(self, chess_board: 'ChessBoard', destination: Coordinate) -> TransactionResult:
        method = "ChessPiece.forward_move_request"

        chess_piece_can_be_moved = ChessPieceValidator.can_be_moved(self)
        if chess_piece_can_be_moved.is_failure:
            return TransactionResult(method, Failure("The chess chess_piece cannot be moved."))

        destination_validation_result = CoordinateValidator.coordinate_exists(destination)
        if destination_validation_result.is_failure:
            return destination_validation_result

        return self._rank.delegate_move_excution(piece=self, board=chess_board, destination=destination)


    def explore_destinations(self, board: 'ChessBoard') -> List[Coordinate]:

        chess_piece_rank_validation_result = ChessPieceValidator.has_rank(self)
        if chess_piece_rank_validation_result.is_failure:
            print(f"{self._label} does not have a rank. It cannot explore without a rank.")
            return []

        board_validation_result = BoardValidator.board_exists(board)
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

    # === Stack operations ===
    def push_new_coordinate(self, coordinate: Coordinate) -> TransactionResult:
        method = "ChessPiece.push_new_coordinate"
        old_size = len(self._coordinate_stack)

        if coordinate is None:
            return TransactionResult(method, Failure("Cannot push a null coordinate on to te stack"))
        if coordinate in self._coordinate_stack:
            print(f"{coordinate} is already on {self._label}'s stack. No need for a push.")
            return TransactionResult(method, StatusCode.SUCCESS)

        self._coordinate_stack.append(coordinate)

        if coordinate == self.current_coordinate() and old_size + 1 == len(self._coordinate_stack):
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult(method, Failure("Failed to push coordinate on to stack"))


    def undo_last_coordinate_push(self) -> Optional[Coordinate]:

        if len(self._coordinate_stack) == 0:
            print(f"{self._label} has no coordinates to undo")
            return None

        if self._coordinate_stack:
            return self._coordinate_stack.pop()
        return None


    def current_coordinate(self) -> Optional[Coordinate]:
        return self._coordinate_stack[-1] if self._coordinate_stack else None