# src/chess/validator/piece_validator.py


# src/chess/validator/piece_validator.py

from chess.piece.piece import ChessPiece
from chess.piece.mobility_status import MobilityStatus
from chess.transaction.transaction_result import TransactionResult


class PieceValidator:



    @staticmethod
    def is_present(self, piece: ChessPiece) -> TransactionResult:
        if piece is None:
            return TransactionResult.failure("ChessPiece is missing (None).")
        return TransactionResult.success()

    @staticmethod
    def is_mobile(self, piece: ChessPiece) -> TransactionResult:
        if piece.mobility_status != MobilityStatus.FREE:
            return TransactionResult.failure(f"{piece.label} is not free to move.")
        return TransactionResult.success()

    @staticmethod
    def is_promotable(self, piece: ChessPiece) -> TransactionResult:
        if not piece.is_promotable():
            return TransactionResult.failure(f"{piece.label} cannot be promoted.")
        return TransactionResult.success()

    @staticmethod
    def is_on_board(self, piece: ChessPiece) -> TransactionResult:
        if piece.coordinate is None:
            return TransactionResult.failure(f"{piece.label} is not on the board.")
        return TransactionResult.success()

