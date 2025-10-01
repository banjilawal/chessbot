from typing import Generic, TypeVar, cast

from chess.common.actor.exception import ActorNotOnBoardException
from chess.piece import Piece, PieceValidator, InvalidPieceException, CircularDiscoveryException, KingPiece, \
    CombatantPiece
from chess.square import Square, SquareValidator, InvalidSqaureException
from chess.common import Validator, Result, IdValidator, IdValidationException
from chess.event.occupation import (
    Piece,
    NullPieceException,
    CircularOccupationException,
    InvalidPieceException
)
from chess.transaction import ExecutionContext

T = TypeVar('T')

class ActorValidator(Validator):

    @staticmethod
    def validate(t: Piece, context: ExecutionContext) -> Result[Piece]:
        """
        Validates an Piece meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess subject
            - `target` is a valid square
        Any validation failure raises an `InvalidPieceException`.

        Argument:
            `t` (`Piece`): `piece `to validate

         Returns:
             `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
                `InvalidPieceException` otherwise.

        Raises:
            `TypeError`: if `t` is not OperationEvent
            `NullPieceException`: if `t` is null

            `IdValidationException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `InvalidSquareException`: if `target` fails validator

            `AutoOccupationException`: if target already occupies the square
            `KingAttackException`: if the target square is occupied by an enemy king

            `InvalidPieceException`: Wraps any preceding exceptions
        """
        method = "ActorValidator.validate"

        try:
            validation = PieceValidator(t)
            if not validation.is_success():
                raise validation.exception

            piece = cast(Piece, t)
            actor = piece

            if piece.positions.is_empty() or piece.current_position is None:
                raise ActorNotOnBoardException(
                    f"{method}: {ActorNotOnBoardException.DEFAULT_MESSAGE}"
                )

            if isinstance(piece, CombatantPiece) and piece.captor is not None:
                raise Exception(f"{method}:")

            if isinstance(piece, KingPiece) and piece.is_checkmated:
                raise Exception(f"{method}:")

            actor = None
            if isinstance(t, CombatantPiece):
                actor = cast(CombatantPiece, t)
            elif isinstance(t, KingPiece):
                actor = cast(KingPiece, t)
            else:
                raise TypeError(f"{method} Expected CombatantPiece or KingPiece, got {type(t).__name__}")

            validation = PieceValidator.validate(actor)
            if not validation.is_success():
                raise InvalidPieceException(f"{method}: {InvalidPieceException.DEFAULT_MESSAGE}")

            if actor.current_position is None or actor.positions.is_empty():
                raise ActorPlacementRequiredException(ActorPlacementRequiredException.DEFAULT_MESSAGE)


            if isinstance(actor, CombatantPiece) and actor.captor is not None:
                raise CapturedActortActException(CapturedActorCannotActException.DEFAULT_MESSAGE)


            subject_validation = SquareValidator.validate(event.subject)
            if not subject_validation.is_success():
                raise InvalidSubjectException(f"{method}: {InvalidActorException.DEFAULT_MESSAGE}")

            if event.actor == event.subject:
                raise CircularDiscoveryException(f"{method}: {CircularDiscoveryException.DEFAULT_MESSAGE}")
            
            return Result(payload=event)

        except (
                TypeError,
                IdValidationException,
                NullPieceException,
                InvalidActorException,
                InvalidSubjectException,
        ) as e:
            raise InvalidPieceException( f"{method}: {InvalidPieceException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the error here before re-raising
        except Exception as e:
            raise InvalidPieceException(f"An unexpected error occurred during validation: {e}") from e

