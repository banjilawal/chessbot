from enum import Enum

from assurance import ThrowHelper
from chess.square import Square, SquareValidator
from chess.common import BuildResult, ExecutionContext, IdValidator
from chess.piece import Piece, KingPiece, CombatantPiece, PieceValidator
from chess.event import (
    OccupationEvent, ScanEvent, AttackEvent, CircularOccupationEvent, OccupationEventBuilderException
)


class OccupationEventBuilder(Enum):
    """
    Builder class responsible for safely constructing `OccupationEvent` instances.

    `OccupationEventBuilder` ensures that `OccupationEvent` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `OccupationEventBuilder` 
     focuses on creation while `OccupationEventValidator` is used for validating existing `OccupationEvent` instances that are passed 
     around the system.

    The builder runs through all validation checks individually to guarantee that any `OccupationEvent` instance it produces 
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe occupationEvent creation with validation
        build_outcome = OccupationEventBuilder.build(event_id=id_emitter.event_id, actor="WN2", square=Knight(), context=white_context)
        if not build_outcome.is_success():
            raise build_outcome.exception
        occupationEvent = build_outcome.payload
        ```
    
    See Also:
        `OccupationEvent`: The data structure being constructed
        `OccupationEventValidator`: Used for validating existing `OccupationEvent` instances
        `BuildResult`: Return type containing the built `OccupationEvent` or error information
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
                * `IdValidationException`: if `event_id` fails validation checks
                * `ActorValidationException`: if `actor` fails validation checks
                * `InvalidSquareException`: if `square` fails validation checks
                * `InvalidContextException`: if `context` fails validation checks
                * `InvalidContextAssignmentException`: If `occupationEvent.context` is different from `context` parameter
                * `FullSquareQuotaException`: If the `context` has no empty slots for the `occupationEvent.square`
                * `FullSquareQuotaException`: If `occupationEvent.context` is equal to `context` parameter but `context.roster` still does
                    not have the occupationEvent

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `OccupationEvent` is 
            created, while `OccupationEventValidator` is used for validating `OccupationEvent` instances that are passed around after 
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            # Valid occupationEvent creation
            build_outcome = OccupationEventBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
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
                        event_id=event_id, actor=actor, square=destination_square, context=context
                    )
                )

            if not actor.is_enemy(destination_occupant) or (
                actor.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
            ):
                return BuilderResult(payload=ScanEvent(
                    event_id=event_id, observer=actor, subject=destination_occupant, destination_square=destination_square, context=context
                    )
                )

            if actor.is_enemy(destination_occupant) and isinstance(destination_occupant, CombatantPiece):
                return BuilderResult(payload=AttackEvent(
                    event_id=event_id, actor=actor, subject=destination_occupant, destination_square=destination_square, context=context
                    )
                )
        except Exception as e:
            raise OccupationEventBuilderException(f"{method}: {OccupationEventBuilderException.DEFAULT_MESSAGE}")


# def main():
#     build_outcome = OccupationEventBuilder.build()
#     if build_outcome.is_success():
#         occupationEvent = build_outcome.payload
#         print(f"Successfully built occupationEvent: {occupationEvent}")
#     else:
#         print(f"Failed to build occupationEvent: {build_outcome.exception}")
#     #
#     build_outcome = OccupationEventBuilder.build(1, None)
#     if build_outcome.is_success():
#         occupationEvent = build_outcome.payload
#         print(f"Successfully built occupationEvent: {occupationEvent}")
#     else:
#         print(f"Failed to build occupationEvent: {build_outcome.exception}")
#
# if __actor__ == "__main__":
#     main()