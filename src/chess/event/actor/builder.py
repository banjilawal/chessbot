from enum import Enum

from assurance import ThrowHelper
from chess.common import BuildResult
from chess.event.actor import ActorPlacementRequiredException, CapturedActorCannotActException, \
    RequiredActorNotFoundException
from chess.piece import Piece, PieceValidator, CombatantPiece
from chess.piece.exception import UnregisteredTeamMemberException
from chess.team import NullTeamException
from chess.transaction import ExecutionContext


class ActorBuilder(Enum):
    """
    Builder class responsible for safely constructing `Actor` instances.

    `ActorBuilder` ensures that `Actor` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `ActorBuilder` 
     focuses on creation while `ActorValidator` is used for validating existing `Actor` instances that are passed 
     around the system.

    The builder runs through all validation checks individually to guarantee that any `Actor` instance it produces 
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe actor creation with validation
        build_outcome = EncounterBuilder.build(actor_id=id_emitter.actor_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        actor = build_outcome.payload
        ```
    
    See Also:
        `Actor`: The data structure being constructed
        `ActorValidator`: Used for validating existing `Actor` instances
        `BuildResult`: Return type containing the built `Actor` or error information
    """

class ActorBuilder(Enum):

    @staticmethod
    def build(actor: Piece, context: ExecutionContext) -> BuildResult[Piece]:

        """
        Constructs a new `Actor` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `Actor` meets all
        specifications. If all checks are passed, a `Actor` instance will be returned. It is not necessary to perform
        any additional validation checks on the returned `Actor` instance. This method guarantees if a `BuildResult`
        with a successful status is returned, the contained `Actor` is valid and ready for use.

        Args:
            `event_id`(`int`): The unique id for the actor. Must pass `IdValidator` checks.
            `observer`(`Piece`): Initiates scan after successful validation`.
            `subject`(`Piece`): The `Piece` scanned by `observer`.
            `context`(`ExecutionContext`): `context.board` verifies `observer` and `subject` are on the board.

        Returns:
            BuildResult[Actor]: A `BuildResult` containing either:
                - On success: A valid `Actor` instance in the payload
                - On failure: Error information and exception details

        Raises:
           ActorBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `IdValidationException`: if `actor_id` fails validation checks
                * `NameValidationException`: if `name` fails validation checks
                * `RankValidationException`: if `rank` fails validation checks
                * `TeamValidationException`: if `team` fails validation checks
                * `InvalidTeamAssignmentException`: If `actor.team` is different from `team` parameter
                * `RankQuotaFullException`: If the `team` has no empty slots for the `actor.rank`
                * `RankQuotaFullException`: If `actor.team` is equal to `team` parameter but `team.roster` still does
                    not have the actor

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `Actor` is
            created, while `ActorValidator` is used for validating `Actor` instances that are passed around after
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            # Valid actor creation
            build_outcome = EncounterBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "ActorBuilder.build"

        try:

            piece_validation = PieceValidator.validate(actor)
            if not piece_validation.is_success():
                ThrowHelper.throw_if_invalid(ActorBuilder, piece_validation.exception)

            if actor not in context.board.pieces:
                ThrowHelper.throw_if_invalid(
                    ActorBuilder,
                    RequiredActorNotFoundException(RequiredActorNotFoundException.DEFAULT_MESSAGE)
                )

            if actor.current_position is None or actor.positions.is_empty():
                ThrowHelper.throw_if_invalid(
                    ActorBuilder,
                    ActorPlacementRequiredException(ActorPlacementRequiredException.DEFAULT_MESSAGE)
                )

            if isinstance(actor, CombatantPiece) and actor.captor is not None:
                ThrowHelper.throw_if_invalid(
                    ActorBuilder,
                    CapturedActorCannotActException(CapturedActorCannotActException.DEFAULT_MESSAGE)
                )

            team = actor.team
            if team is None:
                ThrowHelper.throw_if_invalid(ActorBuilder, NullTeamException(NullTeamException.DEFAULT_MESSAGE))

            if actor not in team.roster:
                ThrowHelper.throw_if_invalid(
                    ActorBuilder,
                    UnregisteredTeamMemberException(UnregisteredTeamMemberException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=actor)
        except Exception as e:
            raise ActorBuilderException(f"{method}: {ActorBuilderException.DEFAULT_MESSAGE}")



            