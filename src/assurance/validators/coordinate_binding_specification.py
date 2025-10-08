from typing import Generic, cast

from chess.piece.validator import ChessPieceValidator
from chess.system.validate.validator import Validator
from assurance.exception.validation.base_validationpy import ChessPieceValidationException
from chess.board.coordinate_bind import CoordinateBinding


class CoordinateSBindingValidator(Validator):

  @staticmethod
  def validate(candidate: Generic[T]) -> bool:
    method = "CoordinateBindingSpecification.is_satisfied_by"

    """
    Validates team CoordinateBinding meets specifications:
      - square.occupant == chess_piece
      - chess_piece.coordinate_stack.current_coordinate() == square.coord
      - chess_piece_previous_square.occupant == null
      
    If any validators fails their team_exception will be encapsulated in team CoordinateBindingValidationException

    Args
      candidate (CoordinateBinding): coordinate_binding to validate

    Returns:
      bool: True if coordinate_binding satisfies the specifications. Otherwise throws an exception
        returning always true is not standard practice. It simplifies testing and eliminates 
        distractions. 

    Raises:

      NullCoordException: if candidate is null

      TypeError: if candidate is not Coord

      RowOutOfBoundsException: If coord.row is outside the range 
        (0, ROW_SIZE - 1) inclusive

      ColumnOutOfBoundsException: If coord.column is outside the range
        (0, COLUMN_SIZE - 1) inclusive
.
      InvalidCoordException: Wraps any
        (NullCoordinate, TypeError, RowOutOfBounds or ColumnOutOfBoundsException)

    """
    try:
      if candidate is None:
        raise NullCoordinateBindingException(
          f"{method} NullCoordinateBindingException.default_message"
        )

      if not isinstance(candidate, CoordinateBinding):
        raise TypeError(f"{method} Expected team CoordinateBinding, got {type(candidate).__name__}")

      coordinate_binding = cast(CoordinateBinding, candidate)

      if not ChessPieceValidator.validate(coordinate_binding.chess_piece):
        raise ChessPieceValidationException(
          f"{method} {ChessPieceValidationException.default_message}"
        )


      return True

    except (
        NullCoordinateException, TypeError,
        RowOutOfBoundsException, ColumnOutOfBoundsException) as e:
      raise CoordinateValidationException(
        f"{method} {class_name}: {entity} validators failed") from e