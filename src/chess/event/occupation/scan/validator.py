from typing import Generic, TypeVar, cast

from chess.board import BoardSearch
from chess.event import AttackEvent, CircularOccupationException
from chess.event.occupation.scan.exception import TargetSquareMismatchException, ScanSubjectException
from chess.piece import PieceValidator, InvalidPieceException, CircularDiscoveryException, CombatantPiece
from chess.system import ExecutionContext, Result, IdValidator, InvalidIdException
from chess.event.occupation import (
    ScanEvent,
    NullScanEventException,
    InvalidScanEventException
)
from chess.square import InvalidSquareException

T = TypeVar('T')

class AttackEventValidator(EventValidator):

    @staticmethod
    def validate(t: AttackEvent, context: ExecutionContext) -> Result[ScanEvent]:
        """
        Validates an ScanEvent meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess enemy
            - `target` is a valid square
        Any validate failure raises an `InvalidScanEventException`.

        Argument:
            `t` (`ScanEvent`): `scanEvent `to validate

         Returns:
             `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
                `InvalidScanEventException` otherwise.

        Raises:
            `TypeError`: if `t` is not OperationEvent
            `NullScanEventException`: if `t` is null

            `InvalidIdException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `InvalidSquareException`: if `target` fails validator

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
                raise InvalidIdException(f"{method}: {InvalidIdException.DEFAULT_MESSAGE}")

            actor_validation = PieceValidator.validate(event.actor)
            if not actor_validation.is_success():
                raise InvalidPieceException(f"{method}: ScanEvent actor failed validate")

            subject_validation = PieceValidator.validate(event.subject)
            if not subject_validation.is_success():
                raise InvalidPieceException(f"{method}: ScanEvent enemy failed validate")

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
                NullScanEventException,
                InvalidPieceException,
                CircularOccupationException,
        ) as e:
            raise InvalidScanEventException(f"{method}: {InvalidScanEventException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the err here before re-raising
        except Exception as e:
            raise InvalidScanEventException(f"{method}: {e}") from e

