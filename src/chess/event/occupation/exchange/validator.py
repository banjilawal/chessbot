from typing import Generic, TypeVar, cast

from chess.event import TransferEvent
from chess.piece import Piece, PieceValidator, InvalidPieceException
from chess.square import Square, SquareValidator, InvalidSqaureException
from chess.common import Validator, Result, IdValidator, InvalidIdException
from chess.event.occupation import (
    AttackEvent,
    NullAttackEventException,
    CircularOccupationException,
    InvalidAttackEventException
)

T = TypeVar('T')

class TransferEventValidator:

    @staticmethod
    def validate(t: TransferEvent, context: Event) -> Result[TransferEvent]:
        """
        Validates an AttackEvent meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess enemy
            - `target` is a valid square
        Any validation failure raises an `InvalidAttackEventException`.

        Argument:
            `t` (`AttackEvent`): `attackEvent `to validate

         Returns:
             `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
                `InvalidAttackEventException` otherwise.

        Raises:
            `TypeError`: if `t` is not OperationEvent
            `NullAttackEventException`: if `t` is null

            `InvalidIdException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `InvalidSquareException`: if `target` fails validator

            `AutoOccupationException`: if target already occupies the square
            `KingAttackException`: if the target square is occupied by an enemy king

            `InvalidAttackEventException`: Wraps any preceding exceptions
        """
        method = "AttackEvent.validate"

        try:
            if t is None:
                raise NullAttackEventException(
                    f"{method}: {NullAttackEventException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, AttackEvent):
                raise TypeError(f"{method} Expected an AttackEvent, got {type(t).__name__}")

            event = cast(AttackEvent, t)

            id_validation = IdValidator.validate(event.id)
            if not id_validation.is_success():
                raise InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")

            actor_validation = PieceValidator.validate(event.actor)
            if not actor_validation.is_success():
                raise InvalidPieceException(f"{method}: actor validation failed")

            destination_square_validation = SquareValidator.validate(event.destination_square)
            if not destination_square_validation.is_success():
                raise InvalidSqaureException(f"{method}: {InvalidSqaureException.DEFAULT_MESSAGE}")

            if event.destination_square.coord == event.actor.current_position:
                raise CircularOccupationException(f"{method}: {CircularOccupationException.DEFAULT_MESSAGE}")
            
            return Result(payload=event)

        except (
                TypeError,
                InvalidIdException,
                InvalidPieceException,
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
            raise InvalidAttackEventException(f"An unexpected error occurred during validation: {e}") from e

