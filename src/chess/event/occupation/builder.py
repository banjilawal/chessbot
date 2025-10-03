from enum import Enum
from typing import cast

from assurance import ThrowHelper
from chess.board import BoardSearch
from chess.exception import SearchException
from chess.square import Square, SquareValidator
from chess.system import BuildResult, ExecutionContext, IdValidator
from chess.piece import Piece, KingPiece, CombatantPiece, PieceValidator
from chess.event import (
    OccupationEvent, ScanEvent, AttackEvent, CircularOccupationException, OccupationEventBuilderException
)


class OccupationEventBuilder(Enum):
    """
    Responsible for safely constructing `OccupationEvent` instances.

    `OccupationEventBuilder` ensures that `OccupationEvent` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `OccupationEventBuilder` 
     focuses on creation while `OccupationEventValidator` is used for validating existing `OccupationEvent` instances that are passed 
     around the system.

    The build runs through all validation checks individually to guarantee that any `OccupationEvent` instance it produces
    meets all required specifications before construction completes
    
    Usage:
        ```python
        ```
    
    See Also:
        `OccupationEvent`: The data structure being constructed
        `OccupationEventValidator`: Used for validating existing `OccupationEvent` instances
        `BuildResult`: Return type containing the built `OccupationEvent` or exception information
    """

    @staticmethod
    def build(event_id: int, actor: Piece, destination_square: Square, context: ExecutionContext) -> BuildResult:
        """
        Constructs a new `OccupationEvent` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `OccupationEvent` meets all 
        specifications. If all checks are passed, a `OccupationEvent` instance will be returned. It is not necessary to perform 
        any additional validation checks on the returned `OccupationEvent` instance. This method guarantees if a `BuildResult` 
        with a successful status is returned, the contained `OccupationEvent` is valid and ready for use.

        Args:
            `event_id` (`int`): The unique id for the occupationEvent. Must pass `IdValidator` checks.
            `actor` (`Piece`): Must pass `PieceValidator` checks.
            `destination_`square` (`Square`): The `square` which determines how the occupationEvent moves and its capture value.
            `context` (`ExecutionContext`): Specifies if the `occupationEvent` is white or black.

        Returns:
            BuildResult[OccupationEvent]: A `BuildResult` containing either:
                - On success: A valid `OccupationEvent` instance in the payload
                - On failure: Error information and exception details

        Raises:
           OccupationEventBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `InvalidIdException`: if `event_id` fails validation checks
                * `ActorValidationException`: if `actor` fails validation checks
                * `InvalidSquareException`: if `square` fails validation checks
                * `InvalidContextException`: if `context` fails validation checks
                * `InvalidContextAssignmentException`: If `occupationEvent.context` is different from `context` parameter
                * `FullSquareQuotaException`: If the `context` has no empty slots for the `occupationEvent.square`
                * `FullSquareQuotaException`: If `occupationEvent.context` is equal to `context` parameter but `context.roster` still does
                    not have the occupationEvent

        Note:
            The build runs through all the checks on parameters and state to guarantee only a valid `OccupationEvent` is
            created, while `OccupationEventValidator` is used for validating `OccupationEvent` instances that are passed around after 
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            ```
        """
        method = "OccupationEventBuilder.build"

        try:
            id_validation = IdValidator.validate(event_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(OccupationEventBuilder, id_validation.exception)

            actor_validation = PieceValidator.validate(actor)
            if not actor_validation.is_success():
                ThrowHelper.throw_if_invalid(OccupationEventBuilder, actor_validation.exception)

            square_validation = SquareValidator.validate(destination_square)
            if not square_validation.is_success():
                ThrowHelper.throw_if_invalid(OccupationEventBuilder, square_validation.exception)

            # context_validation = ContextValidator.validate(context)
            # if not context_validation.is_success():
            #     ThrowHelper.throw_if_invalid(OccupationEventBuilder, context_validation)

            if destination_square.coord == actor.current_position:
                ThrowHelper.throw_if_invalid(
                    OccupationEventBuilder,
                    CircularOccupationException(CircularOccupationException.DEFAULT_MESSAGE)
                )

            destination_occupant = destination_square.occupant
            if destination_occupant is None:
                return BuildResult(payload=OccupationEvent(
                        event_id=event_id, actor=actor, destination_square=destination_square
                    )
                )

            if not actor.is_enemy(destination_occupant) or (
                actor.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
            ):
                return BuildResult(payload=ScanEvent(
                    event_id=event_id,
                    actor=actor,
                    subject=destination_occupant,
                    destination_square=destination_square
                    )
                )

            board_search_result = BoardSearch.square_by_coord(coord=actor.current_position, board=context.board)
            if not board_search_result.is_success():
                return BuildResult(exception=SearchException(
                    "Search did not find the square. This should not happen."
                    )
                )

            actor_square = cast(Square, board_search_result.payload)

            if actor.is_enemy(destination_occupant) and isinstance(destination_occupant, CombatantPiece):
                return BuildResult(payload=AttackEvent(
                    event_id=event_id,
                    actor=actor,
                    enemy=destination_occupant,
                    actor_square=actor_square,
                    destination_square=destination_square,
                    board=context.board
                )
            )

        except Exception as e:
            raise (OccupationEventBuilderException
                   (f"{method}: {OccupationEventBuilderException.DEFAULT_MESSAGE}")
            )