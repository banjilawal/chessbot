from typing import Generic, TypeVar, cast

from chess.piece import Piece, CombatantPiece, KingPiece, PieceValidator, InvalidPieceException
from chess.system import Result, ExecutionContext
from chess.system.actor.exception import (
    CapturedActorCannotActException, ActorPlacementRequiredException,
    CheckMatedKingActivityException, InvalidActorException, ActorNotOnBoardException
)



class ActorValidator:

    @staticmethod
    def validate(piece: Piece, context: ExecutionContext) -> Result[Piece]:
        """
        Validates an Piece meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess enemy
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

            `InvalidIdException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `InvalidSquareException`: if `target` fails validator

            `AutoOccupationException`: if target already occupies the square
            `KingAttackException`: if the target square is occupied by an enemy king

            `InvalidPieceException`: Wraps any preceding exceptions
        """
        method = "ActorValidator.validate"

        try:
            validation = PieceValidator.validate(piece)
            if not validation.is_success():
                raise validation.exception

            if piece not in context.board:
                raise ActorNotOnBoardException(f"{method}: {ActorNotOnBoardException.DEFAULT_MESSAGE}")

            if piece.positions.is_empty() or piece.current_position is None:
                raise ActorPlacementRequiredException(
                    f"{method}: {ActorPlacementRequiredException.DEFAULT_MESSAGE}"
                )

            if isinstance(piece, CombatantPiece) and piece.captor is not None:
                raise CapturedActorCannotActException(
                    f"{method}: {CapturedActorCannotActException.DEFAULT_MESSAGE}"
                )

            if isinstance(piece, KingPiece) and piece.is_checkmated:
                raise CheckMatedKingActivityException(
                    f"{method}: {CheckMatedKingActivityException.DEFAULT_MESSAGE}"
                )

            team = piece.team



            return Result(payload=piece)

        except (
            InvalidPieceException,
            ActorNotOnBoardException,
            CapturedActorCannotActException
        ) as e:
            raise InvalidActorException( f"{method}: {InvalidActorException.DEFAULT_MESSAGE}") from e

        # This block catches any unexpected exceptions
        # You might want to log the exception here before re-raising
        except Exception as e:
            raise InvalidActorException(f"An unexpected error occurred during validation: {e}") from e

