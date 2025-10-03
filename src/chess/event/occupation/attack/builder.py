from enum import Enum
from typing import cast

from assurance import ThrowHelper
from chess.board import BoardSearch
from chess.common import IdValidator, BuildResult, InvalidIdException
from chess.event import TargetSquareMismatchException, AttackEvent
from chess.event.occupation.attack.exception import AttackEventBuilderException
from chess.event.occupation.exception import ActorSquareNotFoundException
from chess.piece import PieceValidator, InvalidPieceException, CombatantPiece
from chess.piece.exception import CircularCaptureException, CaptureFriendException, KingCaptureException


class AttackEventBuilder(Enum):
    """
    Builder class responsible for safely constructing `AttackEvent` instances.

    `AttackEventBuilder` ensures that `AttackEvent` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `AttackEventBuilder` 
     focuses on creation while `AttackEventValidator` is used for validating existing `AttackEvent` instances that are passed 
     around the system.

    The builder runs through all validation checks individually to guarantee that any `AttackEvent` instance it produces 
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe attackEvent creation with validation
        build_outcome = AttackEventBuilder.build(attackEvent_id=id_emitter.attackEvent_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        attackEvent = build_outcome.payload
        ```
    
    See Also:
        `AttackEvent`: The data structure being constructed
        `AttackEventValidator`: Used for validating existing `AttackEvent` instances
        `BuildResult`: Return type containing the built `AttackEvent` or error information
    """

    @staticmethod
    def build(
        event_id: int,
        actor: Piece,
        enemy: Piece,
        destination_square: Square,
        context: ExecutionContext
    ) -> BuildResult[AttackEvent]:
        """
        Constructs a new `AttackEvent` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `AttackEvent` meets all
        specifications. If all checks are passed, a `AttackEvent` instance will be returned. It is not necessary to perform
        any additional validation checks on the returned `AttackEvent` instance. This method guarantees if a `BuildResult`
        with a successful status is returned, the contained `AttackEvent` is valid and ready for use.

        Args:
            `event_id`(`int`): The unique id for the attackEvent. Must pass `IdValidator` checks.
            `actor`(`Piece`): Initiates attack after successful validation`.
            `enemy`(`Piece`): The `Piece` attackned by `actor`.
            `context`(`ExecutionContext`): `context.board` verifies `actor` and `enemy` are on the board.

        Returns:
            BuildResult[AttackEvent]: A `BuildResult` containing either:
                - On success: A valid `AttackEvent` instance in the payload
                - On failure: Error information and exception details

        Raises:
           AttackEventBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `InvalidIdException`: if `attackEvent_id` fails validation checks
                * `NameValidationException`: if `name` fails validation checks
                * `InvalidRankException`: if `rank` fails validation checks
                * `InvalidTeamException`: if `team` fails validation checks
                * `InvalidTeamAssignmentException`: If `attackEvent.team` is different from `team` parameter
                * `FullRankQuotaException`: If the `team` has no empty slots for the `attackEvent.rank`
                * `FullRankQuotaException`: If `attackEvent.team` is equal to `team` parameter but `team.roster` still does
                    not have the attackEvent

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `AttackEvent` is
            created, while `AttackEventValidator` is used for validating `AttackEvent` instances that are passed around after
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            # Valid attackEvent creation
            build_outcome = AttackEventBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "AttackEventBuilder.build"

        try:
            id_validation = IdValidator.validate(event_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(AttackEventBuilder, id_validation)

            actor_validation = PieceValidator.validate(actor)
            if not actor_validation.is_success():
                raise InvalidPieceException(f"{method}: AttackEvent actor failed validation")

            enemy_validation = PieceValidator.validate(enemy)
            if not enemy_validation.is_success():
                raise InvalidPieceException(f"{method}: AttackEvent enemy failed validation")

            if actor == enemy:
                ThrowHelper.throw_if_invalid(
                    AttackEventBuilder,
                    CircularCaptureException(CircularCaptureException.DEFAULT_MESSAGE)
                )

            enemy_square_search = BoardSearch.square_by_coord(
                board=context.board,
                coord=enemy.current_position
            )
            if not enemy_square_search.payload == destination_square:
                ThrowHelper.throw_if_invalid(
                    AttackEventBuilder,
                    TargetSquareMismatchException(
                        f"{method}: {TargetSquareMismatchException.DEFAULT_MESSAGE}"
                    )
                )

            actor_square_search = BoardSearch.square_by_coord(
                board = context.board,
                coord=actor.current_position
            )
            if not actor_square_search.is_success():
                ThrowHelper.throw_if_invalid(
                    AttackEventBuilder,
                    ActorSquareNotFoundException(
                        f"{method}: {ActorSquareNotFoundException.DEFAULT_MESSAGE}")
                )
            actor_square = actor_square_search.payload

            if not actor.is_enemy(enemy):
                ThrowHelper.throw_if_invalid(
                    AttackEventBuilder,
                    CaptureFriendException(CaptureFriendException.DEFAULT_MESSAGE)
                )

            if not isinstance(enemy, CombatantPiece):
                ThrowHelper.throw_if_invalid(
                    AttackEventBuilder,
                    KingCaptureException(KingCaptureException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=AttackEvent(
                actor=actor,
                enemy=enemy,
                event_id=event_id,
                actor_square=actor_square,
                destination_square=destination_square
                )
            )

        except (
            InvalidIdException,
            InvalidPieceException,
            CircularCaptureException,
            TargetSquareMismatchException,
            CaptureFriendException,
            KingCaptureException,
            ActorSquareNotFoundException
        ) as e:
            raise AttackEventBuilderException(f"{method}: {e}") from e

        # Catch any unexpected errors with details about type and message
        except Exception as e:
            raise AttackEventBuilderException(
                f"{method}: Unexpected error ({type(e).__name__}): {e}"
            ) from e



            