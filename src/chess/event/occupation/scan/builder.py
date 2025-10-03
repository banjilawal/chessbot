from enum import Enum

from chess.search import BoardSearch
from chess.square import Square
from assurance import ThrowHelper
from chess.event import ScanEvent, ScanEventBuilderException, TargetSquareMismatchException
from chess.system import IdValidator, BuildResult, ExecutionContext
from chess.piece import Piece, CircularDiscoveryException, PieceValidator, InvalidPieceException


class ScanEventBuilder(Enum):
    """
    Builder class responsible for safely constructing `ScanEvent` instances.

    `ScanEventBuilder` ensures that `ScanEvent` objects are always created successfully by performing comprehensive validation
     checks during construction. This separates the responsibility of building from validating - `ScanEventBuilder` 
     focuses on creation while `ScanEventValidator` is used for validating existing `ScanEvent` instances that are passed 
     around the system.

    The build runs through all validation checks individually to guarantee that any `ScanEvent` instance it produces
    meets all required specifications before construction completes
    
    Usage:
        ```python
        # Safe scanEvent creation with validation
        build_outcome = ScanEventBuilder.build(scanEvent_id=id_emitter.scanEvent_id, name="WN2", rank=Knight(), team=white_team)
        if not build_outcome.is_success():
            raise build_outcome.exception
        scanEvent = build_outcome.payload
        ```
    
    See Also:
        `ScanEvent`: The data structure being constructed
        `ScanEventValidator`: Used for validating existing `ScanEvent` instances
        `BuildResult`: Return type containing the built `ScanEvent` or exception information
    """

    @staticmethod
    def build(
        event_id: int,
        actor: Piece,
        subject: Piece,
        destination_square: Square,
        context: ExecutionContext
    ) -> BuildResult[ScanEvent]:

        """
        Constructs a new `ScanEvent` instance with comprehensive checks on the parameters and states during the
        build process.

        Performs individual validation checks on each component to ensure the resulting `ScanEvent` meets all
        specifications. If all checks are passed, a `ScanEvent` instance will be returned. It is not necessary to perform
        any additional validation checks on the returned `ScanEvent` instance. This method guarantees if a `BuildResult`
        with a successful status is returned, the contained `ScanEvent` is valid and ready for use.

        Args:
            `event_id`(`int`): The unique id for the scanEvent. Must pass `IdValidator` checks.
            `actor`(`Piece`): Initiates scan after successful validation`.
            `enemy`(`Piece`): The `Piece` scanned by `actor`.
            `context`(`ExecutionContext`): `context.board` verifies `actor` and `enemy` are on the board.

        Returns:
            BuildResult[ScanEvent]: A `BuildResult` containing either:
                - On success: A valid `ScanEvent` instance in the payload
                - On failure: Error information and exception details

        Raises:
           ScanEventBuilderException: Wraps any underlying validation failures that occur during the construction process.
           This includes:
                * `InvalidIdException`: if `scanEvent_id` fails validation checks
                * `InvalidNameException`: if `name` fails validation checks
                * `InvalidRankException`: if `rank` fails validation checks
                * `InvalidTeamException`: if `team` fails validation checks
                * `InvalidTeamAssignmentException`: If `scanEvent.team` is different from `team` parameter
                * `FullRankQuotaException`: If the `team` has no empty slots for the `scanEvent.rank`
                * `FullRankQuotaException`: If `scanEvent.team` is equal to `team` parameter but `team.roster` still does
                    not have the scanEvent

        Note:
            The build runs through all the checks on parameters and state to guarantee only a valid `ScanEvent` is
            created, while `ScanEventValidator` is used for validating `ScanEvent` instances that are passed around after
            creating. This separation of concerns makes the validation and building independent of each other and
            simplifies maintenance.

        Example:
            ```python
            # Valid scanEvent creation
            build_outcome = ScanEventBuilder.build(value=1)
            if not build_outcome.is_success():
                return BuildResult(exception=build_outcome.exception)
            return BuildResult(payload=build_outcome.payload)
            ```
        """
        method = "ScanEventBuilder.build"

        try:
            id_validation = IdValidator.validate(event_id)
            if not id_validation.is_success():
                ThrowHelper.throw_if_invalid(ScanEventBuilder, id_validation)


            actor_validation = PieceValidator.validate(actor)
            if not actor_validation.is_success():
                raise InvalidPieceException(f"{method}: ScanEvent actor failed validation")

            subject_validation = PieceValidator.validate(subject)
            if not subject_validation.is_success():
                raise InvalidPieceException(f"{method}: ScanEvent enemy failed validation")

            if actor == subject:
                ThrowHelper.throw_if_invalid(
                    ScanEventBuilder,
                    CircularDiscoveryException(CircularDiscoveryException.DEFAULT_MESSAGE)
                )

            search_result = BoardSearch.square_by_coord(coord=subject.current_position, board=context.board)
            if not search_result.payload == destination_square:
                ThrowHelper.throw_if_invalid(
                    ScanEventBuilder,
                    TargetSquareMismatchException(
                        f"{method}: {TargetSquareMismatchException.DEFAULT_MESSAGE}"
                    )
                )


            return BuildResult(payload=ScanEvent(
                event_id=event_id,
                actor=actor,
                subject=subject,
                destination_square=destination_square
                )
            )

        except Exception as e:
            raise ScanEventBuilderException(f"{method}: {e}") from e

            