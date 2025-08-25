from typing import Generic, cast

from assurance.validation.chess_piece_specification import ChessPieceSpecification
from assurance.validation.specification import Specification
from assurance.exception.validation.base_validationpy import ChessPieceValidationException
from chess.board.coordinate_bind import CoordinateBinding


class CoordinateSBindiingpecification(Specification):

    @staticmethod
    def is_satisfied_by(t: Generic[T]) -> bool:
        method = "CoordinateBindingSpecification.is_satisfied_by"

        """
        Validates a CoordinateBinding meets specifications:
            - square.occupant == chess_piece
            - chess_piece.coordinate_stack.current_coordinate() == square.coordinate
            - chess_piece_previous_square.occupant == null
            
        If any validation fails their exception will be encapsulated in a CoordinateBindingValidationException

        Args
            t (CoordinateBinding): coordinate_binding to validate

        Returns:
            bool: True if coordinate_binding satisfies the specifications. Otherwise throws an exception
                returning always true is not standard practice. It simplifies testing and eliminates 
                distractions. 

        Raises:

            NullCoordinateException: if t is null

            TypeError: if t is not Coordinate

            RowOutOfBoundsException: If coordinate.row is outside the range 
                (0, ROW_SIZE - 1) inclusive

            ColumnOutOfBoundsException: If coordinate.column is outside the range
                (0, COLUMN_SIZE - 1) inclusive
.
            CoordinateValidationException: Wraps any
                (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)

        """
        try:
            if t is None:
                raise NullCoordinateBindingException(
                    f"{method} NullCoordinateBindingException.default_message"
                )

            if not isinstance(t, CoordinateBinding):
                raise TypeError(f"{method} Expected a CoordinateBinding, got {type(t).__name__}")

            coordinate_binding = cast(CoordinateBinding, t)

            if not ChessPieceSpecification.is_satisfied_by(coordinate_binding.chess_piece):
                raise ChessPieceValidationException(
                    f"{method} {ChessPieceValidationException.default_message}"
                )


            return True

        except (
                NullCoordinateException, TypeError,
                RowOutOfBoundsException, ColumnOutOfBoundsException) as e:
            raise CoordinateValidationException(
                f"{method} CoordinateValidationException.default_message") from e