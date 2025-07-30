
from chess.piece.piece import ChessPiece
from chess.piece.mobility_status import MobilityStatus
from chess.rank.promotable.promotable_rank import PromotableRank
from chess.transaction.failure import Failure
from chess.transaction.status_code import StatusCode
from chess.transaction.transaction_result import TransactionResult


class ChessPieceValidator:

    @staticmethod
    def has_rank(self, chess_piece: ChessPiece) -> TransactionResult:
        method = "ChessPieceValidator.has_rank"

        if chess_piece.rank is None:
            return TransactionResult(method, Failure(f"{chess_piece.label} does not have a rank."))
        return TransactionResult(method, StatusCode.SUCCESS)


    @staticmethod
    def is_not_null(self, piece: ChessPiece) -> TransactionResult:
        method = "ChessPieceValidator.is_not_null"

        if piece is None:
            return TransactionResult.failure("ChessPiece does not exist. It is null (None).")
        return TransactionResult(method, StatusCode.SUCCESS)


    @staticmethod
    def can_be_moved(self, piece: ChessPiece) -> TransactionResult:
        method = "ChessPieceValidator.can_move"

        if piece.status == MobilityStatus.FREE and piece.current_coordinate() is not None:
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult.failure(f"{piece.label} is not free to move.")


    @staticmethod
    def can_place_on_board(self, chess_piece: ChessPiece) -> TransactionResult:
        method = "ChessPieceValidator.can_add_to_board"
        if (
            chess_piece is not None and
            chess_piece.status == MobilityStatus.FREE and
            chess_piece.current_coordinate() is None
        ):
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult(method, Failure(f"{chess_piece.label} Cannot be added to the board"))


    @staticmethod
    def can_be_promoted(self, chess_piece: ChessPiece) -> TransactionResult:
        method = "ChessPieceValidator.is_promotable"

        rank = chess_piece.rank
        if isinstance(rank, PromotableRank) and not rank.is_promoted():
            return TransactionResult(method, StatusCode.SUCCESS)
        return TransactionResult(method, Failure(f"{chess_piece.label} of rank {rank.name} cannot be promoted."))


    @staticmethod
    def is_on_board(self, piece: ChessPiece) -> TransactionResult:
        method = "ChessPieceValidator.is_on_board"

        if piece.current_coordinate() is None:
            return TransactionResult(method, Failure(f"{piece.label} is not on the board."))
        return TransactionResult(method, StatusCode.SUCCESS)