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
  Responsible for safely constructing `TravelEvent` instances.

  `OccupationEventBuilder` ensures that `TravelEvent` objects are always created successfully by performing comprehensive validate
   checks during construction. This separates the responsibility of building from validating - `OccupationEventBuilder`
   focuses on creation while `OccupationEventValidator` is used for validating existing `TravelEvent` instances that are passed
   around the system.

  The build runs through all validate checks individually to guarantee that any `TravelEvent` instance it produces
  meets all required specifications before construction completes

  Usage:
    ```python
    ```

  See Also:
    `TravelEvent`: The data structure being constructed
    `OccupationEventValidator`: Used for validating existing `TravelEvent` instances
    `BuildResult`: Return type containing the built `TravelEvent` or error information
  """

  @staticmethod
  def build(event_id: int, actor: Piece, destination_square: Square, context: ExecutionContext) -> BuildResult:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not null.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `exception` (`Exception`) - An exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is null
        * `NegativeIdException`: if candidate is negative `
    """
    """
    Constructs team new `TravelEvent` instance with comprehensive checks on the parameters and states during the
    build process.

    Performs individual validate checks on each component to ensure the resulting `TravelEvent` meets all
    specifications. If all checks are passed, team `TravelEvent` instance will be returned. It is not necessary to perform
    any additional validate checks on the returned `TravelEvent` instance. This method guarantees if team `BuildResult`
    with team successful status is returned, the contained `TravelEvent` is valid and ready for use.

    Args:
      `event_id` (`int`): The unique id for the occupationEvent. Must pass `IdValidator` checks.
      `actor` (`Piece`): Must pass `PieceValidator` checks.
      `destination_`square` (`Square`): The `square` which determines how the occupationEvent moves and its capture value.
      `roster` (`ExecutionContext`): Specifies if the `occupationEvent` is white or black.

    Returns:
      BuildResult[TravelEvent]: A `BuildResult` containing either:
        - On success: A valid `TravelEvent` instance in the payload
        - On failure: Error information and error details

    Raises:
      OccupationEventBuilderException: Wraps any underlying validate failures that occur during the construction process.
      This includes:
        * `InvalidIdException`: if `event_id` fails validate checks
        * `ActorValidationException`: if `actor` fails validate checks
        * `InvalidSquareException`: if `square` fails validate checks
        * `InvalidContextException`: if `roster` fails validate checks
        * `InvalidContextAssignmentException`: If `occupationEvent.roster` is different from `roster` parameter
        * `FullSquareQuotaException`: If the `roster` has no empty slots for the `occupationEvent.square`
        * `FullSquareQuotaException`: If `occupationEvent.roster` is equal to `roster` parameter but `roster.roster` still does
          not have the occupationEvent

    Note:
      The build runs through all the checks on parameters and state to guarantee only team valid `TravelEvent` is
      created, while `OccupationEventValidator` is used for validating `TravelEvent` instances that are passed around after
      creating. This separation of concerns makes the validate and building independent of each other and
      simplifies maintenance.

    Example:
      ```python
      ```
    """
    method = "OccupationEventBuilder.build"

    try:
      id_validation = IdValidator.validate(event_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_error(OccupationEventBuilder, id_validation.exception)

      actor_validation = PieceValidator.validate(actor)
      if not actor_validation.is_success():
        ThrowHelper.log_and_raise_error(OccupationEventBuilder, actor_validation.exception)

      square_validation = SquareValidator.validate(destination_square)
      if not square_validation.is_success():
        ThrowHelper.log_and_raise_error(OccupationEventBuilder, square_validation.exception)

      # context_validation = ContextValidator.validate(roster)
      # if not context_validation.is_success():
      #   LoggingLevelRouter.throw_if_invalid(OccupationEventBuilder, context_validation)

      if destination_square.coord == actor.current_position:
        ThrowHelper.log_and_raise_error(
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