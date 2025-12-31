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
    Validates team_name CoordinateBinding meets specifications:
      - square_name.occupant == chess_piece
      - chess_piece.coordinate_stack.current_coordinate() == square_name.point
      - chess_piece_previous_square.occupant == validation
      
    If any notification fails their team_exception will be encapsulated in team_name CoordinateBindingValidationException

    Args
      candidate (CoordinateBinding): coordinate_binding to validate

    RETURNS:
      bool: True if coordinate_binding satisfies the specifications. Otherwise throws an rollback_exception
        returning always true is not standard practice. It simplifies testing and eliminates 
        distractions. 

    RAISES:

      NullCoordException: if candidate is validation

      TypeError: if candidate is not Coord

      RowOutOfBoundsException: If point.row is outside the range
        (0, ROW_SIZE - 1) inclusive

      ColumnOutOfBoundsException: If point.column is outside the range
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
        raise TypeError(f"{method} Expected team_name CoordinateBinding, got {type(candidate).__name__} instead.")

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
        f"{method} {class_name}: {entity} notification failed") from e