from typing import Generic, cast

from assurance.validation.specification import Specification, T
from assurance.exception.validation.base_validationpy import ChessPieceValidationException
from chess.exception.move.empty_stack_chess_piece import EmptyStackChessPieceMoveException
from chess.exception.move.move import CapturedPieceMoveException
from chess.exception.null.coord_stack import NullCoordinateStackException
from chess.exception.null.null_exception import NullException
from chess.token.piece import ChessPiece


class ChessPieceSpecification(Specification):
    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        pass

class PromotionSpecification(ChessPieceSpecification):
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

        try:
            if t is None:
                print("t was null")
                raise NullException(
                    f"{method} NullException.default_message"
                )

            if not isinstance(t, ChessPiece):
                print("t is not a ChessPiece")
                raise TypeError(f"{method} Expected a Coordinate, got {type(t).__name__}")

            chess_piece = cast(ChessPiece, t)

            if chess_piece.positions is None:
                print(f"{chess_piece.name} has a null stack")
                raise NullCoordinateStackException(
                    f"{method} {NullCoordinateStackException.default_message}"
                )

            if chess_piece.positions.is_empty():
                print(f"{chess_piece.name}  coordinate stack is empty")
                raise EmptyStackChessPieceMoveException(
                    f"{method} {EmptyStackChessPieceMoveException.default_message}"
                )

            if chess_piece.captor is not None:
                print(f"{chess_piece.name} cannot move captured by {chess_piece.captor.name}")
                raise CapturedPieceMoveException(
                    f"{method} {CapturedPieceMoveException.default_message}"
                )

            return True

        except (
            TypeError,
            NullException,
            CapturedPieceMoveException,
            NullCoordinateStackException,
            EmptyStackChessPieceMoveException,
        ) as e:
            print("Unknown exception")
            raise ChessPieceValidationException(
                f"{method} ChessPieceValidationException.default_message: {str(e)}") from e
