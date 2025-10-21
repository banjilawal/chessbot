from typing import TypeVar, cast

from chess.board import BoardSearch
from chess.event import CircularOccupationException
from chess.piece.event.encounter.event.exception import TargetSquareMismatchException, ScanSubjectException
from chess.piece import PieceValidator, InvalidAttackException, CircularDiscoveryException, CombatantPiece
from chess.system import Result, IdValidator, InvalidIdException, ValidationResult, Validator, LoggingLevelRouter
from chess.piece import (
  EncounterEvent,
  NullEncounterEventException,
  InvalidScanEventException
)

T = TypeVar('T')

class EncounterEventValidator(Validator[EncounterEvent]):

  @classmethod
  @LoggingLevelRouter.monitor
  def validate(cls, candidate: T) -> ValidationResult[EncounterEvent]:
    """"""
    method = "EncounterEventValidator.validate"

    try:
      if candidate is None:
        return ValidationResult(
          exception=NullEncounterEventException(
            f"{method}: {NullEncounterEventException.DEFAULT_MESSAGE}"
        ))

      if not isinstance(candidate, EncounterEvent):
        return ValidationResult(
          exception=TypeError(f"{method} Expected an EncounterEvent, got {type(candidate).__name__}"
        ))

      event = cast(EncounterEvent, candidate)

      id_validation = IdValidator.validate(event.id)
      if id_validation.is_success():
        return ValidationResult(exception=InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}"))

      actor_validation = PieceValidator.validate(event.actor)
      if not actor_validation.is_success():
        raise InvalidAttackException(f"{method}: EncounterEvent actor_candidate failed validate")

      subject_validation = PieceValidator.validate(event.subject)
      if not subject_validation.is_success():
        raise InvalidAttackException(f"{method}: EncounterEvent enemy failed validate")

      if event.actor == event.subject:
        raise CircularDiscoveryException(f"{method}: {CircularDiscoveryException.DEFAULT_MESSAGE}")

      destination_search = BoardSearch.square_by_coord(
        coord=event.subject.current_position,
        board=context.board
      )
      if destination_search.payload == event.destination_square:
        raise TargetSquareMismatchException(
          f"{method}: {TargetSquareMismatchException.DEFAULT_MESSAGE}"
        )

      actor = event.actor
      subject = event.subject
      if actor.is_enemy(subject) and isinstance(subject, CombatantPiece):
        raise ScanSubjectException(f"{method}: {ScanSubjectException.DEFAULT_MESSAGE}")


      return Result(payload=event)

    except (
        TypeError,
        InvalidIdException,
        NullEncounterEventException,
        InvalidAttackException,
        CircularOccupationException,
    ) as e:
      raise InvalidScanEventException(f"{method}: {InvalidScanEventException.DEFAULT_MESSAGE}") from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidScanEventException(f"{method}: {e}") from e

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
    Validates an EncounterEvent meets specifications:
      - Not null
      - `id` does not fail validator
      - `actor_candidate` is team valid chess enemy
      - `target` is team valid square
    Any validate failure raises an `InvalidScanEventException`.

    Argument:
      `candidate` (`EncounterEvent`): `scanEvent `to validate

     Returns:
       `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
        `InvalidScanEventException` otherwise.

    Raises:
      `TypeError`: if `candidate` is not OperationEvent
      `NullEncounterEventException`: if `candidate` is null

      `InvalidIdException`: if invalid `id`
      `PieceValidationException`: if `actor_candidate` fails validator
      `InvalidSquareException`: if `target` fails validator

      `AutoOccupationException`: if target already occupies the square
      `KingAttackException`: if the target square is occupied by an enemy king

      `InvalidScanEventException`: Wraps any preceding exceptions
    """