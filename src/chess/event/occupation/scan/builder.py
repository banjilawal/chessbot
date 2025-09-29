from enum import Enum

from assurance import ThrowHelper
from chess.common import IdValidator
from chess.event.occupation.scan import ScanEvent


class ScanEventBuilder(Enum):
    """
    Builder class responsible for safely constructing `ScanEvent` instances.

    `ScanEventBuilder` ensures that `ScanEvent` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `ScanEventBuilder` 
     focuses on creation while `ScanEventValidator` is used for validating existing `ScanEvent` instances that are passed 
     around the system.

    The builder runs through all validation checks individually to guarantee that any `ScanEvent` instance it produces 
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe scanEvent creation with validation
        build_outcome = EncounterBuilder.build(scanEvent_id=id_emitter.scanEvent_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        scanEvent = build_outcome.payload
        ```
    
    See Also:
        `ScanEvent`: The data structure being constructed
        `ScanEventValidator`: Used for validating existing `ScanEvent` instances
        `BuildResult`: Return type containing the built `ScanEvent` or error information
    """

class ScanEventBuilder(Enum):

    @staticmethod
    def build(event_id: int,  observer: Piece, subject: Piece, context: ExecutionContext) -> BuildResult[ScanEvent]:

        """
        Constructs a new `ScanEvent` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `ScanEvent` meets all
        specifications. If all checks are passed, a `ScanEvent` instance will be returned. It is not necessary to perform
        any additional validation checks on the returned `ScanEvent` instance. This method guarantees if a `BuildResult`
        with a successful status is returned, the contained `ScanEvent` is valid and ready for use.

        Args:
            `event_id`(`int`): The unique id for the scanEvent. Must pass `IdValidator` checks.
            `observer`(`Piece`): Initiates scan after successful validation`.
            `subject`(`Piece`): The `Piece` scanned by `observer`.
            `context`(`ExecutionContext`): `context.board` verifies `observer` and `subject` are on the board.

        Returns:
            BuildResult[ScanEvent]: A `BuildResult` containing either:
                - On success: A valid `ScanEvent` instance in the payload
                - On failure: Error information and exception details

        Raises:
           ScanEventBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `IdValidationException`: if `scanEvent_id` fails validation checks
                * `NameValidationException`: if `name` fails validation checks
                * `RankValidationException`: if `rank` fails validation checks
                * `TeamValidationException`: if `team` fails validation checks
                * `InvalidTeamAssignmentException`: If `scanEvent.team` is different from `team` parameter
                * `RankQuotaFullException`: If the `team` has no empty slots for the `scanEvent.rank`
                * `RankQuotaFullException`: If `scanEvent.team` is equal to `team` parameter but `team.roster` still does
                    not have the scanEvent

        Note:
            The builder runs through all the checks on parameters and state to guarantee only a valid `ScanEvent` is
            created, while `ScanEventValidator` is used for validating `ScanEvent` instances that are passed around after
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            # Valid scanEvent creation
            build_outcome = EncounterBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "EncounterBuilder.build"

        try:
            id_validation = IdValidator.validate(event_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(ScanEventBuilder, id_validation)

            observer_validation = PieceValidator.validate(observer)
            if not observer_validation.is_success():
                ThrowHelper.throw_if_invalid(ScanEventBuilder, observer_validation)

            if observer not in context.board.pieces:
                ThrowHelper.throw_if_invalid(ScanEventBuilder, )

            rank_validation = RankValidator.validate(rank)
            if not rank_validation.is_success():
                ThrowHelper.throw_if_invalid(ScanEventBuilder, rank_validation)

            team_validation = TeamValidator.validate(team)
            if not team_validation.is_success():
                ThrowHelper.throw_if_invalid(ScanEventBuilder, team_validation)

            if len(TeamSearch.by_rank(rank, team).payload) >= rank.quota:
                ThrowHelper.throw_if_invalid(
                    ScanEventBuilder,
                    RankQuotaFullException(RankQuotaFullException.DEFAULT_MESSAGE)
                )

            scanEvent = None
            if isinstance(rank, King):
                scanEvent = KingScanEvent(scanEvent_id=scanEvent_id, name=name, rank=rank, team=team)
            scanEvent = CombatantScanEvent(scanEvent_id=scanEvent_id, name=name, rank=rank, team=team)

            if not scanEvent.team == team:
                ThrowHelper.throw_if_invalid(
                    ScanEventBuilder,
                    InvalidTeamAssignmentException(InvalidTeamAssignmentException.DEFAULT_MESSAGE)
                )

            if not scanEvent.team == team:
                team.add_to_roster(scanEvent)

            if scanEvent not in team.roster:
                ThrowHelper.throw_if_invalid(
                    ScanEventBuilder,
                    RelationshipException(RelationshipException.DEFAULT_MESSAGE)
                )

            return BuildResult(payload=scanEvent)
        except Exception as e:
            raise ScanEventBuilderException(f"{method}: {ScanEventBuilderException.DEFAULT_MESSAGE}")



            