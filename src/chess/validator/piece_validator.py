# src/chess/validator/piece_validator.py

from chess.piece.piece import Piece
from chess.piece.mobility_status import MobilityStatus
from chess.rank.king import King
from chess.rank.pawn import Pawn
from chess.transaction.transaction_result import TransactionResult
from chess.transaction.status_code import StatusCode


# src/chess/validator/piece_validator.py

from chess.piece.piece import Piece
from chess.piece.mobility_status import MobilityStatus
from chess.transaction.transaction_result import TransactionResult
from chess.transaction.status_code import StatusCode


class PieceValidator:



    @staticmethod
    def is_present(self, piece: Piece) -> TransactionResult:
        if piece is None:
            return TransactionResult.failure("Piece is missing (None).")
        return TransactionResult.success()

    @staticmethod
    def is_mobile(self, piece: Piece) -> TransactionResult:
        if piece.mobility_status != MobilityStatus.FREE:
            return TransactionResult.failure(f"{piece.label} is not free to move.")
        return TransactionResult.success()

    @staticmethod
    def is_promotable(self, piece: Piece) -> TransactionResult:
        if not piece.is_promotable():
            return TransactionResult.failure(f"{piece.label} cannot be promoted.")
        return TransactionResult.success()

    @staticmethod
    def is_on_board(self, piece: Piece) -> TransactionResult:
        if piece.coordinate is None:
            return TransactionResult.failure(f"{piece.label} is not on the board.")
        return TransactionResult.success()

