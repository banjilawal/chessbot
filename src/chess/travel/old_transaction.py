# src/chess/owner/travel/old_transaction.py

"""
Module: chess.owner.travel.notification
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
# THEME:
# PURPOSE:
# DEPENDENCIES:
# CONTAINS:
 * `TravelEventFactory`
"""


from typing import cast


from chess.system import Transaction, TransactionResult, TransactionState, LoggingLevelRouter, \
  SearchResult

from chess.square import Square
from chess.agent.finder import BoardSearch

from chess.team import AddEnemyHostageRolledBackException, PieceCollectionCategory
from chess.team.exception import RemoveTeamMemberRolledBackException


from chess.transaction import AttackValidator
from chess.piece.event import (
  OldOccupationEventValidator,
  OccupationSearchEventException,
  TravelEvent,
  OccupationEventException,

    # Rollback attack errors (dual inheritance)
  BoardPieceRemovalRollbackException,
)


class OldTravelTransaction(Transaction[TravelEvent]):
  """
  Implements the `OccupationExecutor` class, which handles executing travel
  directives in the chess engine. This includes moving pieces, capturing enemies,
  and coordinating rollback logic in case of inconsistencies or failed rollback.

  Attributes:
    * `OccupationExecutor:` Main class responsible for executing travel directives.
    * `_attack_enemy`: Static method for processing attacks on enemy pieces.
    * `_run_scan`: Static method for handling discoveries on occupied squares.
    * `_switch_squares`: Static method the transferring team_name owner to team_name different `Square`.
  """
  @classmethod
  @LoggingLevelRouter.monitor
  def execute(cls, event: TravelEvent, execution_environment: Board) -> TransactionResult:
    """
    # ACTION:
    Verify the `candidate` is a valid ID. The Application requires
    1. Candidate is not validation.
    2. Is a positive integer.

    # PARAMETERS:
        * `candidate` (`int`): the visitor_id.

    # RETURNS:
    `ValidationResult[str]`: A `ValidationResult` containing either:
        `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
        `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.

    # RAISES:
    `InvalidIdException`: Wraps any specification violations including:
        * `TypeError`: if candidate is not an `int`
        * `IdNullException`: if candidate is validation
        * `NegativeIdException`: if candidate is negative `
    """
    method = "TravelEventFactory.execute"

    event_validation = TravelEventValidator.validate(event)
    if not event_validation.is_success():
      return TransactionResult(
        event_update=event,
        transaction_state=TransactionState.FAILURE,
        exception=event_validation.exception
      )

    actor_square_search = BoardSearch.find(
      board=context.board,
      data_source=BoardDatasource.SQUARE,
      context=BoardSearchcontext(coord=event.actor.current_position)
    )

    if not actor_square_search.is_success():
      return TransactionResult(
        event_update=event,
        transaction_state=TransactionState.FAILURE,
        exception=actor_square_search.exception
      )

    destination_search = BoardSearch.find(
      board=context.board,
      data_source=BoardDatasource.SQUARE,
      context=BoardSearchcontext(event.enemy_square.visitor_id)
    )
    if not destination_search.is_success():
      return TransactionResult(exception=EventResourceNotFoundExeception(
          f"{method}: {DestinationSquareNotFoundException.DEFAULT_MESSAGE}"
        # EventResourceNotFoundException
        )
      )

    if len(destination_search.payload) > 1:
      return TransactionResult(exception=DestinationSquareColiisonException(
          f"{method}: {DestinationSquareCollisionException.DEFAULT_MESSAGE}"
        )
      )

    destination_occupant = event.enemy_square.occupant
    actor_square = BoardSearch.find()

    if destination_occupant is None:
      build_result = OccupationEventBuilder.build(
        parent=event,
        actor=event.actor,
        actor_square=actor_square,
        destination_square=event.enemy_square
      )
      if not build_result.is_success():
        return TransactionResult(exception=build_result.exception)
      return

    if isinstance(destination_occupant.rank_name, King) or (not event.actor.is_enemy(destination_occupant):
      build_result = ScanEventBuilder(

      )
      if not build_result.is_success():
        return TransactionResult(exception=build_result.exception)
      return OccupationTransacti()


    )









    TravelTransactionsearch_result = BoardSearch.square_by_coord(coord=event.actor.current_position, board=context.board)
    if search_result.exception is not None:
      return TransactionResult(op_result_id, event, search_result.exception)

    if search_result.is_empty():
      return TransactionResult(
        op_result_id,
        event,
        OccupationSearchEventException(f"{method}: {OccupationSearchEventException.DEFAULT_MESSAGE}")
      )
    actor_square = cast(Square, search_result.payload)

    if event.friend.occupant is None:
      return TravelTransaction._switch_squares(op_result_id, event, actor_square)

    actor = event.actor
    destination_occupant = event.friend.occupant
    if not actor.is_enemy(destination_occupant) or (
      actor.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
    ):
      return TravelTransaction._run_scan(
        op_result_id=op_result_id,
        directive=ScanDirective(
          actor=event.actor,
          occupation_id=event.visitor_id,
          scan_id=id_emitter.scan_id,
          subject=destination_occupant,
          destination_square=event.friend
        )
      )


    attack_validation = AttackValidator.validate(
      CaptureContext(piece=event.actor, enemy=destination_occupant, board=context.board)
    )
    if not attack_validation.is_success():
      return TransactionResult(op_result_id, event, attack_validation.exception)

    enemy_combatant = cast(CombatantPiece, attack_validation.payload.enemy_combatant)
    return TravelTransaction._attack_enemy(
      op_result_id=op_result_id,
      directive=AttackDirective(
        board=context.board,
        actor=event.actor,
        enemy=enemy_combatant,
        occupation_id=event.visitor_id,
        attack_id=id_emitter.attack_id,
        actor_square=actor_square,
        destination_square=event.friend
      )

  @classmethod
  @LoggingLevelRouter.monitor
  def _search_board_for_square(cls, square: Square, board: Board) -> SearchResult[List[Square]]:


  @staticmethod)
  def _switch_squares(op_result_id: int, directive: TravelEvent, actor_square: Square) -> TransactionResult:
    """
    Transfers `Piece` occupying`actor_square` to `directive.blocked_square` leaving `actor_square` empty.
    `Traveltransaction.execute` is the single entry point to `_switch_squares`. Before `_switch_squares`
    was called `execute_directive`: validated the parameters, handled exceptions, and confirmed
    `directive.blocked_square` contained either
      * A friendly owner blocking `actor_candidate` from `blocked_square`
      * An enemy occupation. Kings cannot be captured, only checked or checkmated.

    Args:
      - `op_result_id` (`int`): The `visitor_id` of the `OperationResult` passed to the caller.
      - `directive` (`OccupationDirective`): The `OccupationDirective` to be executed.
      - `actor_square` (`Square`): The `Square` occupied by `actor_candidate`.

    Returns:
    `OccupationResult` containing:
      - On success: A new `OccupationDirective` with the updated squares and `owner`.
      - On failure: The original `OccupationDirective`or verifying any rollbacks succeeded and the err
        describing the failure.

    Raises:
    Errors raised will be about service and state inconsistencies OccupationException: Wraps any errors including:
      -

    Note:
    *  If the notification fails, `OperationResult.was_rolled_back = True`
    """
    method = "OccupationExecutor._switch_squares"

    directive.friend.occupant = directive.actor
    if not directive.friend.occupant == directive.actor:
      # Rollback all changes in reverse order
      directive.friend.occupant = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
      )

    actor_square.occupant = None
    if actor_square.occupant == directive.actor:
      # Rollback all changes in reverse order
      actor_square.occupant = directive.actor
      directive.friend.occupant = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
      )

    directive.actor.positions.push_coord(directive.friend.position)
    if not directive.actor.current_position == directive.friend.position:
      # Rollback all changes in reverse order
      directive.actor.positions.undo_push()
      actor_square.occupant = directive.actor
      directive.friend.occupant = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
      )

    return TransactionResult(
      result_id=op_result_id,
      event=TravelEvent(id_emitter.event_id, directive.actor, directive.friend)
    )


  @staticmethod
  def _run_scan(op_result_id :int, directive: ScanDirective) -> TransactionResult:
    """
    Creates team_name new `Checker` object for directive.actor_candidate which is blocking from moving to
    `blocked_square` by `directive.enemy`. The enemy is either team_name friendly owner or an enemy `KingPiece`.
    `Traveltransaction.execute` is the single entry point to `_run_scan`. Validations, error chains
    confirmed parameters ar are correct. No additional sanity checks are needed.

    Args
      - `op_result_id` (`int`): The `visitor_id` of the `OperationResult` passed to the caller.
      - `directive` (`ScanDirective`): The `ScanDirective` to execute.

    Returns:
    `OccupationResult` containing:
      - On success: A new `ScanDirective` object that containing updated `actor_candidate`. Observer will have
        team_name new `Checker` instance inside `actor_candidate.discoveries`.
      - On failure: The original `ScanDirective` for verifying any rollbacks succeeded and the err
        describing the failure.

    Raises:
    Errors raised will be about service and state inconsistencies OccupationException: Wraps any errors including:
      -
    Note:
    """
    method = "OccupationExecutor._run_scan"

    build_outcome = DiscoveryBuilder.build(observer=directive.observer, subject=directive.friend)
    if not build_outcome.is_success():
      return TransactionResult(op_result_id, directive, exception=build_outcome.exception)

    discovery = cast(Discovery, build_outcome.payload)
    if discovery not in directive.observer.discoveries.items:
      directive.observer.discoveries.record_discovery(discovery=discovery)

    if discovery not in directive.observer.discoveries.items:
      return TransactionResult(
        # There is nothing to actually do so there is no rollback because the discover was not added
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
      )

    success_directive = ScanDirective(
      actor=directive._owner,
      subject=directive.friend,
      occupation_id=directive.visitor_id,
      scan_id=id_emitter.scan_id,
      destination_square=directive.friend
    )
    return TransactionResult(result_id=op_result_id, event=success_directive)


  @staticmethod
  def _attack_enemy(op_result_id: int, directive: AttackDirective) -> TransactionResult:

    method = "OccupationExecutor._attack_enemy"

    directive.enemy_combatant.captor = directive._owner
    if directive.enemy_combatant.captor != directive._owner:
      # Rollback all changes in reverse order
      directive.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
        was_rolled_back=True
      )

    directive.enemy_combatant.team_name.roster.remove(directive.enemy_combatant)
    if directive.enemy_combatant in directive.enemy_combatant.team_name.roster:
      # Rollback all changes in reverse order
      directive.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=RemoveTeamMemberRolledBackException(
          f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    directive._owner.team_name.hostages.append(directive.enemy_combatant)
    if directive.enemy_combatant not in directive._owner.team_name.hostages:
      # Rollback all changes in reverse order
      directive.enemy_combatant.team_name.add_to_roster(directive.enemy_combatant)
      directive.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=AddEnemyHostageRolledBackException(
          f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
        )
      )

    directive.friend.occupant = None
    if directive.friend.occupant is not None:
      # Rollback all changes in reverse order
      directive._owner.team_name.hostages.remove(directive.enemy_combatant)
      directive.enemy_combatant.team_name.add_to_roster(directive.enemy_combatant)
      directive.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
      )

    directive.board.pieces.remove(directive.enemy_combatant)
    if directive.enemy_combatant in directive.board.pieces:
      # Rollback all changes in reverse order
      directive.friend.occupant = directive.enemy_combatant
      directive._owner.team_name.hostages.remove(directive.enemy_combatant)
      directive.enemy_combatant.team_name.add_to_roster(directive.enemy_combatant)
      directive.enemy_combatant.captor = None

      # Send the notification indicating rollback
      return TransactionResult(
        result_id=op_result_id,
        event=directive,
        was_rolled_back=True,
        exception=BoardPieceRemovalRollbackException(
          f"{method}: {BoardPieceRemovalRollbackException.DEFAULT_MESSAGE}"
        )
      )

    return OldTravelTransaction._switch_squares(op_result_id, directive, directive.actor_square)

