from typing import Generic, TypeVar, cast


from chess.piece import Piece, PieceValidator, InvalidPieceException, CircularDiscoveryException
from chess.square import Square, SquareValidator, SquareValidationException
from chess.common import Validator, Result, IdValidator, IdValidationException
from chess.event.occupation import (
    ScanEvent,
    NullScanEventException,
    CircularOccupationException,
    InvalidScanEventException
)

T = TypeVar('T')

class ScanEventValidator(Validator):

    @staticmethod
    def validate(t: ScanEvent) -> Result[ScanEvent]:
        """
        Validates an ScanEvent meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess subject
            - `target` is a valid square
        Any validation failure raises an `InvalidScanEventException`.

        Argument:
            `t` (`ScanEvent`): `scanEvent `to validate

         Returns:
             `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
                `InvalidScanEventException` otherwise.

        Raises:
            `TypeError`: if `t` is not OperationEvent
            `NullScanEventException`: if `t` is null

            `IdValidationException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `SquareValidationException`: if `target` fails validator

            `AutoOccupationException`: if target already occupies the square
            `KingAttackException`: if the target square is occupied by an enemy king

            `InvalidScanEventException`: Wraps any preceding exceptions
        """
        method = "ScanEvent.validate"

        try:
            if t is None:
                raise NullScanEventException(f"{method}: {NullScanEventException.DEFAULT_MESSAGE}")

            if not isinstance(t, ScanEvent):
                raise TypeError(f"{method} Expected an ScanEvent, got {type(t).__name__}")

            event = cast(ScanEvent, t)

            id_validation = IdValidator.validate(event.id)
            if not id_validation.is_success():
                raise IdValidationException(f"{method}: {IdValidationException.DEFAULT_MESSAGE}")

            actor_validation = PieceValidator.validate(event.actor)
            if not actor_validation.is_success():
                raise InvalidActorException(f"{method}: {InvalidActorException.DEFAULT_MESSAGE}")

            subject_validation = SquareValidator.validate(event.subject)
            if not subject_validation.is_success():
                raise InvalidSubjectException(f"{method}: {InvalidActorException.DEFAULT_MESSAGE}")

            if event.actor == event.subject:
                raise CircularDiscoveryException(f"{method}: {CircularDiscoveryException.DEFAULT_MESSAGE}")
            
            return Result(payload=event)

        except (
                TypeError,
                IdValidationException,
                NullScanEventException,
                InvalidActorException,
                InvalidSubjectException,
        ) as e:
            raise InvalidScanEventException( f"{method}: {InvalidScanEventException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise InvalidScanEventException(f"An unexpected error occurred during validation: {e}") from e

