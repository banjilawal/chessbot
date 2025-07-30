# src/chess/validator/piece_validator.py


# src/chess/validator/piece_validator.py

from chess.piece.piece import ChessPiece
from chess.piece.mobility_status import MobilityStatus
from chess.rank.promotable.promotable_rank import PromotableRank
from chess.transaction.transaction_result import TransactionResult


class ChessPieceValidator:

    @staticmethod
    def is_not_null(self, piece: ChessPiece) -> TransactionResult:
        if piece is None:
            return TransactionResult.failure("ChessPiece does not exist. It is null (None).")
        return TransactionResult.success()


    @staticmethod
    def can_move(self, piece: ChessPiece) -> TransactionResult:
        if piece.mobility_status == MobilityStatus.FREE and piece.current_position() is not None:
            return TransactionResult.success()
        return TransactionResult.failure(f"{piece.label} is not free to move.")


    @staticmethod
    def can_add_to_board(self, piece: ChessPiece) -> TransactionResult:
        if piece.mobility_status == MobilityStatus.FREE and piece.current_position() is None:
            return TransactionResult.success()
        return TransactionResult.failure(f"{piece.label} Cannot be added to the board")


    @staticmethod
    def is_prisoner(self, piece: ChessPiece) -> TransactionResult:
        if piece.mobility_status != MobilityStatus.PRISONER:
            return TransactionResult.failure(f"{piece.label} is not a prisoner.")
        return TransactionResult.success()


    @staticmethod
    def is_promotable(self, piece: ChessPiece) -> TransactionResult:
        rank = piece.rank

        if not isinstance(rank, PromotableRank):
            return TransactionResult.failure(f"{piece.label} does not have a promotable rank")

        if isinstance(rank, PromotableRank):
            if rank.previous_rank is not None:
                return TransactionResult.failure(
                    f"{piece.label} has already been promoted from {rank.previous_rank.name}"
                )
            else:
                return TransactionResult.is_success()
        return TransactionResult.failure(f"{piece.label} unexpected rank mutation")


    @staticmethod
    def is_on_board(self, piece: ChessPiece) -> TransactionResult:
        if piece.coordinate is None:
            return TransactionResult.failure(f"{piece.label} is not on the board.")
        return TransactionResult.success()

