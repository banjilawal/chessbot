from typing import cast, TypeVar


from chess.system import Validator, ValidationResult, LoggingLevelRouter
from chess.board import (
  Board, BoardNullPieceCollectionException, BoardNullSquareCollectionException, NullBoardException,
  InvalidBoardException
)


T = TypeVar('T')

class BoardValidator(Validator[Board]):

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[Board]:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the visitor_id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    """
    Validates team_name discover with chained exceptions for discover meeting specifications:
      - Not null
      - visitor_id fails validator
      - visitor_name fails validator
      - visitor_coord fails validator
    If validator fails their team_exception will be encapsulated in team_name BoardValidationException

    Args
      candidate (Board): discover to validate

     Returns:
       Result[T]: A Result object containing the validated payload if the specification is satisfied,
        BoardValidationException otherwise.

    Raises:
      TypeError: if candidate is not Board
      NullBoardException: if candidate is null

      InvalidIdException: if invalid visitor_id
      InvalidNameException: if invalid visitor_name
      InvalidCoordException: if invalid visitor_coord

      BoardValidationException: Wraps any preceding exceptions
    """
    method = "BoardValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullBoardException(f"{method} {NullBoardException.DEFAULT_MESSAGE}"))

      if not isinstance(candidate, Board):
        return ValidationResult(exception=TypeError(f"{method} Expected team_name Board, got {type(candidate).__name__}"))

      board = cast(Board, candidate)

      if board.pieces is None:
        return ValidationResult(exception=BoardNullPieceCollectionException(
          f"{method}: {BoardNullPieceCollectionException.DEFAULT_MESSAGE}"
        ))

      if board.squares is None:
        return ValidationResult(exception=BoardNullSquareCollectionException(
          f"{method}: {BoardNullSquareCollectionException.DEFAULT_MESSAGE}"
        ))

      return ValidationResult(payload=board)

    except Exception as e:
      return ValidationResult(exception=InvalidBoardException(f"{method}: {e}"))


#
#
# def main():
#   person = CommanderBuilder.build(commander_id=id_emitter.person_id, visitor_name=RandomName.person())
#   team_name = TeamBuilder.build()