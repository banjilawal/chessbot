from typing import Generic

from assurance.validation.specification import Specification, T
from chess.board.board import MissingPlacementException, CapturedPieceMoveException
from chess.exception.null_exception import NullChessPieceException, NullCoordinateStackException
from chess.token.chess_piece import ChessPiece


class ChessPieceSpecification(Specification):
    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        pass

class MoveSpecification(ChessPieceSpecification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        method = "ChessPieceMoveSpecification.is_satisfied_by"

        """
        Validates that the provided chess piece can be moved according to the rules of chess.
        Raises exceptions if the chess piece is null, not a ChessPieceSpecification, has no coordinate
        """

        if t is None:
            raise NullChessPieceException(f"{method} {NullChessPieceException.default_message}")

        if not isinstance(t, ChessPieceSpecification):
            raise TypeError(f"Expected a ChessPieceSpecification, got {type(t).__name__}")

        chess_piece = ChessPiece(t)
        # Implement specific validation logic for chess piece movement here

        if chess_piece.coordinate_stack is None:
            raise NullCoordinateStackException(f"{method} {NullCoordinateStackException.default_message}")

        if chess_piece.coordinate_stack.is_empty():
            raise MissingPlacementException(
                f"{method} {MissingPlacementException.default_message}"
            )

        if chess_piece.captor is not None:
            raise CapturedPieceMoveException(f"{method} {CapturedPieceMoveException.default_message}")

        return True

class PromotionSpecification(ChessPieceSpecification):
    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        pass

