from typing import Generic, TypeVar, cast

from chess.board import NullBoardException
from chess.system import Result, Validator
from chess.transaction import CaptureContext
from chess.piece import  PieceValidator, InvalidPieceException, CombatantPiece

from chess.transaction.exception import (
    NullCaptureContextException, AutoCaptureException, FriendlyFireException, EnemyNotOnBoardException,
    AttackOnEmptySquareException, KingTargetException, AlreadyCapturedException, MissingFromRosterException,
    HostageTransferConflictException, InvalidCaptureContextException
)



T = TypeVar('T')

class AttackValidator(Validator):

    @staticmethod
    def validate(t: CaptureContext) -> Result[CaptureContext]:
        """
        Validates an OccupationDirective meets specifications:
            - Not null
            - `id` does not fail validator
            - `actor` is a valid chess enemy
            - `target` is a valid square
        Any validation failure raises an `InvalidOccupationDirectiveException`.

        Argument:
            `t` (`OccupationDirective`): `occupationDirective `to validate

         Returns:
             `Result[T]`: A `Result` object containing the validated payload if the specification is satisfied,
                `InvalidOccupationDirectiveException` otherwise.

        Raises:
            `TypeError`: if `t` is not OperationDirective
            `NullOccupationDirectiveException`: if `t` is null

            `InvalidIdException`: if invalid `id`
            `PieceValidationException`: if `actor` fails validator
            `InvalidSquareException`: if `target` fails validator

            `AutoOccupationException`: if target already occupies the square
            `KingAttackException`: if the target square is occupied by an enemy king

            `InvalidOccupationDirectiveException`: Wraps any preceding exceptions
        """
        method = "AttackValidator.validate"

        try:
            if t is None:
                raise NullCaptureContextException(
                    f"{method}: {NullCaptureContextException.DEFAULT_MESSAGE}"
                )

            if not isinstance(t, CaptureContext):
                raise TypeError(f"{method} Expected an CaptureContext, got {type(t).__name__}")

            context = cast(CaptureContext, t)

            if context.board is None:
                raise NullBoardException(f"{method}: {NullBoardException.DEFAULT_MESSAGE}")

            piece_validation = PieceValidator.validate(context.piece)
            if not piece_validation.is_success():
                raise InvalidPieceException(f"{method}: the piece is invalid")

            enemy_validation = PieceValidator.validate(context.enemy)
            if not enemy_validation.is_success():
                raise InvalidPieceException(f"{method}: the enemy is not a valid piece")

            if context.piece is context.enemy:
                raise AutoCaptureException(f"{method}: {AutoCaptureException.DEFAULT_MESSAGE}")

            if not context.piece.is_enemy(context.enemy):
                raise FriendlyFireException(f"{method}: {FriendlyFireException.DEFAULT_MESSAGE}")

            if not context.enemy in context.board.pieces:
                raise EnemyNotOnBoardException(f"{method}: {EnemyNotOnBoardException.DEFAULT_MESSAGE}")

            if context.enemy.positions.is_empty():
                raise AttackOnEmptySquareException(f"{method}: {AttackOnEmptySquareException.DEFAULT_MESSAGE}")

            if not isinstance(context.enemy, CombatantPiece):
                raise KingTargetException(f"{method}: {KingTargetException.DEFAULT_MESSAGE}")

            enemy_combatant = cast(CombatantPiece, context.enemy)

            if enemy_combatant.captor is not None:
                raise AlreadyCapturedException(f"{method}: {AlreadyCapturedException.DEFAULT_MESSAGE}")

            enemy_team = enemy_combatant.team
            if enemy_combatant not in enemy_team.roster:
                raise MissingFromRosterException(f"{method}: {MissingFromRosterException.DEFAULT_MESSAGE}")


            if enemy_combatant in context.piece.team.hostages:
                raise HostageTransferConflictException(f"{method}: {HostageTransferConflictException.DEFAULT_MESSAGE}")
            
            return Result(payload=context)

        except (
                TypeError,
                NullCaptureContextException,
                NullCaptureContextException,
                InvalidPieceException,
                AutoCaptureException,
                FriendlyFireException,
                KingTargetException,
                AlreadyCapturedException,
                MissingFromRosterException,
                HostageTransferConflictException
        ) as e:
            raise InvalidCaptureContextException(
                f"{method}: {InvalidCaptureContextException.DEFAULT_MESSAGE}"
            ) from e

        # This block catches any unexpected exceptions
        # You might want to log the exception here before re-raising
        except Exception as e:
            raise InvalidCaptureContextException(f"An unexpected error occurred during validation: {e}") from e

