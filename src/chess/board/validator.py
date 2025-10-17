from typing import cast, TypeVar

from chess.board import Board, BoardNullPieceCollectionException, BoardNullSquareCollectionException
from chess.exception.hostage.hostage import KingCheckMateStateException
from chess.board import Board, NullBoardException, InvalidBoardException, UnregisteredTeamMemberException, \
  CombatantBoard, HostageActivityException, KingBoard
from chess.system import Result, Validator, IdValidator, NameValidator, InvalidIdException, InvalidNameException, \
  LoggingLevelRouter, ValidationResult
from chess.team import NullTeamException

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
        * `candidate` (`int`): the id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    """
    Validates team discover with chained exceptions for discover meeting specifications:
      - Not null
      - id fails validator
      - name fails validator
      - coord fails validator
    If validator fails their team_exception will be encapsulated in team BoardValidationException

    Args
      candidate (Board): discover to validate

     Returns:
       Result[T]: A Result object containing the validated payload if the specification is satisfied,
        BoardValidationException otherwise.

    Raises:
      TypeError: if candidate is not Board
      NullBoardException: if candidate is null

      InvalidIdException: if invalid id
      InvalidNameException: if invalid name
      InvalidCoordException: if invalid coord

      BoardValidationException: Wraps any preceding exceptions
    """
    method = "BoardValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(exception=NullBoardException(f"{method} {NullBoardException.DEFAULT_MESSAGE}"))

      if not isinstance(candidate, Board):
        return ValidationResult(exception=TypeError(f"{method} Expected team Board, got {type(candidate).__name__}"))

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
#   person = CommanderBuilder.build(commander_id=id_emitter.person_id, name=RandomName.person())
#   team = TeamBuilder.build()