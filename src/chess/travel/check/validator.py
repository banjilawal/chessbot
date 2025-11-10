from logging import Logger
from typing import Any, Generic, TypeVar, cast

from chess.event import EventValidator
from chess.piece import KingCheckEvent, PieceValidator, InvalidAttackException
from chess.square import SquareValidator, InvalidSqaureException
from chess.system import LoggingLevelRouter, Result, IdValidator, InvalidIdException, ValidationResult, Validator
from chess.piece.event import (
  AttackEvent,
  NullAttackEventException,
  CircularOccupationException,
  InvalidAttackEventException
)

T = TypeVar('T')

class KingCheckEventValidator(Validator[KingCheckEvent]):

  @staticmethod
  @LoggingLevelRouter.monitor
  def validate(candidate: Any) -> ValidationResult:
    """
    Validates an KingCheckEvent meets specifications:
      - Not null
      - `visitor_id` does not fail validator
      - `actor_candidate` is team valid chess enemy
      - `target` is team valid square
    Any validate failure raises an `InvalidAttackEventException`.

    Argument:
      `candidate` (`KingCheckEvent`): `attackEvent `to validate

     Returns:
       `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
        `InvalidAttackEventException` otherwise.

    Raises:
      `TypeError`: if `candidate` is not OperationEvent
      `NullAttackEventException`: if `candidate` is null

      `InvalidIdException`: if invalid `visitor_id`
      `PieceValidationException`: if `actor_candidate` fails validator
      `InvalidSquareException`: if `target` fails validator

      `AutoOccupationException`: if target already occupies the square
      `KingAttackException`: if the target square is occupied by an enemy occupation

      `InvalidAttackEventException`: Wraps any preceding exceptions
    """
    method = "KingCheckEvent.validate"

    try:
      if t is None:
        raise NullAttackEventException(
          f"{method}: {NullAttackEventException.DEFAULT_MESSAGE}"
        )

      if not isinstance(t, AttackEvent):
        raise TypeError(f"{method} Expected an KingCheckEvent, got {type(t).__name__}")

      event = cast(AttackEvent, t)

      id_validation = IdValidator.validate(event.visitor_id)
      if not id_validation.is_success():
        raise InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")

      actor_validation = PieceValidator.validate(event.actor)
      if not actor_validation.is_success():
        raise InvalidAttackException(f"{method}: actor_candidate validation failed.")

      destination_square_validation = SquareValidator.validate(event.enemy_square)
      if not destination_square_validation.is_success():
        raise InvalidSqaureException(f"{method}: {InvalidSqaureException.DEFAULT_MESSAGE}")

      if event.enemy_square.visitor_coord == event.actor.current_position:
        raise CircularOccupationException(f"{method}: {CircularOccupationException.DEFAULT_MESSAGE}")

      return Result(payload=event)

    except (
        TypeError,
        InvalidIdException,
        InvalidAttackException,
        InvalidSqaureException,
        NullAttackEventException,
        CircularOccupationException
    ) as e:
      raise InvalidAttackEventException(
        f"{method}: {InvalidAttackEventException.DEFAULT_MESSAGE}"
      ) from e

    # This block catches any unexpected exceptions
    # You might want to log the error here before re-raising
    except Exception as e:
      raise InvalidAttackEventException(f"An unexpected error occurred during validate: {e}") from e

