from enum import Enum

from assurance import ThrowHelper
from chess.board import BoardSearch
from chess.system import IdValidator, BuildResult, InvalidIdException
from chess.event import TargetSquareMismatchException, AttackEvent
from chess.piece.event.attack.exception import AttackEventBuilderException
from chess.piece.event.exception import ActorSquareNotFoundException
from chess.piece import PieceValidator, InvalidPieceException, CombatantPiece
from chess.piece.exception import CircularCaptureException, CaptureFriendException, KingCaptureException


class AttackEventBuilder(Enum):
  """
  Builder class responsible for safely constructing `AttackEvent` instances.

  `AttackEventBuilder` ensures that `AttackEvent` objects are always created successfully by performing comprehensive validate
   checks during construction. This separates the responsibility of building from validating - `AttackEventBuilder`
   focuses on creation while `AttackEventValidator` is used for validating existing `AttackEvent` instances that are passed
   around the system.

  The build runs through all validate checks individually to guarantee that any `AttackEvent` instance it produces
  meets all required specifications before construction completes

  Usage:
    ```python
    # Safe attackEvent creation with validate
    build_outcome = AttackEventBuilder.build(attackEvent_id=id_emitter.attackEvent_id, name="WN2", rank=Knight(), team=white_team)
    if not build_outcome.is_success():
      raise build_outcome.err
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
    Constructs team new `AttackEvent` instance with comprehensive checks on the parameters and states during the
    build process.

    Performs individual validate checks on each component to ensure the resulting `AttackEvent` meets all
    specifications. If all checks are passed, team `AttackEvent` instance will be returned. It is not necessary to perform
    any additional validate checks on the returned `AttackEvent` instance. This method guarantees if team `BuildResult`
    with team successful status is returned, the contained `AttackEvent` is valid and ready for use.

    Args:
      `event_id`(`int`): The unique id for the attackEvent. Must pass `IdValidator` checks.
      `actor`(`Piece`): Initiates attack after successful validate`.
      `enemy`(`Piece`): The `Piece` attackned by `actor`.
      `roster`(`ExecutionContext`): `roster.board` verifies `actor` and `enemy` are on the board.

    Returns:
      BuildResult[AttackEvent]: A `BuildResult` containing either:
        - On success: A valid `AttackEvent` instance in the payload
        - On failure: Error information and error details

    Raises:
      AttackEventBuilderException: Wraps any underlying validate failures that occur during the construction process.
      This includes:
        * `InvalidIdException`: if `attackEvent_id` fails validate checks
        * `InvalidNameException`: if `name` fails validate checks
        * `InvalidRankException`: if `rank` fails validate checks
        * `InvalidTeamException`: if `team` fails validate checks
        * `InvalidTeamAssignmentException`: If `attackEvent.team` is different from `team` parameter
        * `FullRankQuotaException`: If the `team` has no empty slots for the `attackEvent.rank`
        * `FullRankQuotaException`: If `attackEvent.team` is equal to `team` parameter but `team.roster` still does
          not have the attackEvent

    Note:
      The build runs through all the checks on parameters and state to guarantee only team valid `AttackEvent` is
      created, while `AttackEventValidator` is used for validating `AttackEvent` instances that are passed around after
      creating. This separation of concerns makes the validate and building independent of each other and
      simplifies maintenance.

    Example:
      ```python
      # Valid attackEvent creation
      build_outcome = AttackEventBuilder.build(value=1)
      if not build_outcome.is_success():
        return BuildResult(err=build_outcome.err)
      return BuildResult(payload=build_outcome.payload)
      ```
    """
    method = "AttackEventBuilder.build"

    try:
      id_validation = IdValidator.validate(event_id)
      if not id_validation.is_success():
        ThrowHelper.log_and_raise_error(AttackEventBuilder, id_validation)

      actor_validation = PieceValidator.validate(actor)
      if not actor_validation.is_success():
        raise InvalidPieceException(f"{method}: AttackEvent actor failed validate")

      enemy_validation = PieceValidator.validate(enemy)
      if not enemy_validation.is_success():
        raise InvalidPieceException(f"{method}: AttackEvent enemy failed validate")

      if actor == enemy:
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          CircularCaptureException(CircularCaptureException.DEFAULT_MESSAGE)
        )

      enemy_square_search = BoardSearch.square_by_coord(
        board=context.board,
        coord=enemy.current_position
      )
      if not enemy_square_search.payload == destination_square:
        ThrowHelper.log_and_raise_error(
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
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          ActorSquareNotFoundException(
            f"{method}: {ActorSquareNotFoundException.DEFAULT_MESSAGE}")
        )
      actor_square = actor_square_search.payload

      if not actor.is_enemy(enemy):
        ThrowHelper.log_and_raise_error(
          AttackEventBuilder,
          CaptureFriendException(CaptureFriendException.DEFAULT_MESSAGE)
        )

      if not isinstance(enemy, CombatantPiece):
        ThrowHelper.log_and_raise_error(
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



