# src/chess/piece/event/old_transaction.py

"""
Module: chess.piece.event.transaction
Author: Banji Lawal
Created: 2025-09-28

# SCOPE:
# THEME:
# PURPOSE:
# DEPENDENCIES:
# CONTAINS:
 * `TravelEventFactory`
"""
from abc import abstractmethod

from chess.piece import TravelEvent
from chess.system import LoggingLevelRouter, Transaction, TransactionResult


class TravelTransaction(Transaction):
  _event = TravelEvent

  def __init__(self, event: TravelEvent):
    super().__init__(event)

  @abstractmethod
  @LoggingLevelRouter.monitor
  def execute(self) -> TransactionResult:
    pass
  # """
  # Implements the `OccupationExecutor` class, which handles executing event
  # directives in the chess engine. This includes moving pieces, capturing enemies,
  # and coordinating rollback logic in case of inconsistencies or failed operations.
  #
  # Attributes:
  #   * `OccupationExecutor:` Main class responsible for executing event directives.
  #   * `_attack_enemy`: Static method for processing attacks on enemy pieces.
  #   * `_run_scan`: Static method for handling discoveries on occupied squares.
  #   * `_switch_squares`: Static method the transferring team piece to team different `Square`.
  # """
  # @classmethod
  # @LoggingLevelRouter.monitor
  # def execute(cls, event: TravelEvent, execution_environment: Board) -> TransactionResult:
  #   """
  #   # ACTION:
  #   Verify the `candidate` is a valid ID. The Application requires
  #   1. Candidate is not null.
  #   2. Is a positive integer.
  #
  #   # PARAMETERS:
  #       * `candidate` (`int`): the id.
  #
  #   # RETURNS:
  #   `ValidationResult[str]`: A `ValidationResult` containing either:
  #       `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
  #       `exception` (`Exception`) - An exception detailing which naming rule was broken.
  #
  #   # RAISES:
  #   `InvalidIdException`: Wraps any specification violations including:
  #       * `TypeError`: if candidate is not an `int`
  #       * `IdNullException`: if candidate is null
  #       * `NegativeIdException`: if candidate is negative `
  #   """
  #   method = "TravelEventFactory.execute"
  #
  #   event_validation = TravelEventValidator.validate(event)
  #   if not event_validation.is_success():
  #     return TransactionResult(
  #       event_update=event,
  #       transaction_state=TransactionState.FAILURE,
  #       exception=event_validation.exception
  #     )
  #
  #   actor_square_search = BoardSearch.search(
  #     board=context.board,
  #     data_source=BoardDatasource.SQUARE,
  #     context=BoardSearchcontext(coord=event.actor.current_position)
  #   )
  #
  #   if not actor_square_search.is_success():
  #     return TransactionResult(
  #       event_update=event,
  #       transaction_state=TransactionState.FAILURE,
  #       exception=actor_square_search.exception
  #     )
  #
  #   destination_search = BoardSearch.search(
  #     board=context.board,
  #     data_source=BoardDatasource.SQUARE,
  #     context=BoardSearchcontext(event.destination_square.id)
  #   )
  #   if not destination_search.is_success():
  #     return TransactionResult(exception=EventResourceNotFoundExeception(
  #         f"{method}: {DestinationSquareNotFoundException.DEFAULT_MESSAGE}"
  #       # EventResourceNotFoundException
  #       )
  #     )
  #
  #   if len(destination_search.payload) > 1:
  #     return TransactionResult(exception=DestinationSquareColiisonException(
  #         f"{method}: {DestinationSquareCollisionException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   destination_occupant = event.destination_square.occupant
  #   actor_square = BoardSearch.search()
  #
  #   if destination_occupant is None:
  #     build_result = OccupationEventBuilder.build(
  #       parent=event,
  #       actor=event.actor,
  #       actor_square=actor_square,
  #       destination_square=event.destination_square
  #     )
  #     if not build_result.is_success():
  #       return TransactionResult(exception=build_result.exception)
  #     return
  #
  #   if isinstance(destination_occupant.rank, King) or (not event.actor.is_enemy(destination_occupant):
  #     build_result = ScanEventBuilder(
  #
  #     )
  #     if not build_result.is_success():
  #       return TransactionResult(exception=build_result.exception)
  #     return OccupationTransacti()
  #
  #
  #   )
  #
  #
  #
  #
  #
  #
  #
  #
  #
  #   TravelTransactionsearch_result = BoardSearch.square_by_coord(coord=event.actor.current_position, board=context.board)
  #   if search_result.exception is not None:
  #     return TransactionResult(op_result_id, event, search_result.exception)
  #
  #   if search_result.is_empty():
  #     return TransactionResult(
  #       op_result_id,
  #       event,
  #       OccupationSearchEventException(f"{method}: {OccupationSearchEventException.DEFAULT_MESSAGE}")
  #     )
  #   actor_square = cast(Square, search_result.payload)
  #
  #   if event.subject.occupant is None:
  #     return TravelTransaction._switch_squares(op_result_id, event, actor_square)
  #
  #   actor = event.actor
  #   destination_occupant = event.subject.occupant
  #   if not actor.is_enemy(destination_occupant) or (
  #     actor.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
  #   ):
  #     return TravelTransaction._run_scan(
  #       op_result_id=op_result_id,
  #       directive=ScanDirective(
  #         actor=event.actor,
  #         occupation_id=event.id,
  #         scan_id=id_emitter.scan_id,
  #         subject=destination_occupant,
  #         destination_square=event.subject
  #       )
  #     )
  #
  #
  #   attack_validation = AttackValidator.validate(
  #     CaptureContext(piece=event.actor, enemy=destination_occupant, board=context.board)
  #   )
  #   if not attack_validation.is_success():
  #     return TransactionResult(op_result_id, event, attack_validation.exception)
  #
  #   enemy_combatant = cast(CombatantPiece, attack_validation.payload.enemy)
  #   return TravelTransaction._attack_enemy(
  #     op_result_id=op_result_id,
  #     directive=AttackDirective(
  #       board=context.board,
  #       actor=event.actor,
  #       enemy=enemy_combatant,
  #       occupation_id=event.id,
  #       attack_id=id_emitter.attack_id,
  #       actor_square=actor_square,
  #       destination_square=event.subject
  #     )
  #
  # @classmethod
  # @LoggingLevelRouter.monitor
  # def _search_board_for_square(cls, square: Square, board: Board) -> SearchResult[List[Square]]:
  #
  #
  # @staticmethod)
  # def _switch_squares(op_result_id: int, directive: TravelEvent, actor_square: Square) -> TransactionResult:
  #   """
  #   Transfers `Piece` occupying`actor_square` to `directive.subject_square` leaving `actor_square` empty.
  #   `Traveltransaction.execute` is the single entry point to `_switch_squares`. Before `_switch_squares`
  #   was called `execute_directive`: validated the parameters, handled exceptions, and confirmed
  #   `directive.subject_square` contained either
  #     * A friendly piece blocking `actor_candidate` from `subject_square`
  #     * An enemy king. Kings cannot be captured, only checked or checkmated.
  #
  #   Args:
  #     - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
  #     - `directive` (`OccupationDirective`): The `OccupationDirective` to be executed.
  #     - `actor_square` (`Square`): The `Square` occupied by `actor_candidate`.
  #
  #   Returns:
  #   `OccupationResult` containing:
  #     - On success: A new `OccupationDirective` with the updated squares and `piece`.
  #     - On failure: The original `OccupationDirective`or verifying any rollbacks succeeded and the err
  #       describing the failure.
  #
  #   Raises:
  #   Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
  #     -
  #
  #   Note:
  #   *  If the transaction fails, `OperationResult.was_rolled_back = True`
  #   """
  #   method = "OccupationExecutor._switch_squares"
  #
  #   directive.subject.occupant = directive.actor
  #   if not directive.subject.occupant == directive.actor:
  #     # Rollback all changes in reverse order
  #     directive.subject.occupant = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #     )
  #
  #   actor_square.occupant = None
  #   if actor_square.occupant == directive.actor:
  #     # Rollback all changes in reverse order
  #     actor_square.occupant = directive.actor
  #     directive.subject.occupant = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
  #     )
  #
  #   directive.actor.positions.push_coord(directive.subject.position)
  #   if not directive.actor.current_position == directive.subject.position:
  #     # Rollback all changes in reverse order
  #     directive.actor.positions.undo_push()
  #     actor_square.occupant = directive.actor
  #     directive.subject.occupant = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #     )
  #
  #   return TransactionResult(
  #     result_id=op_result_id,
  #     event=TravelEvent(id_emitter.event_id, directive.actor, directive.subject)
  #   )
  #
  #
  # @staticmethod
  # def _run_scan(op_result_id :int, directive: ScanDirective) -> TransactionResult:
  #   """
  #   Creates team new `Checker` object for directive.actor_candidate which is blocked from moving to
  #   `subject_square` by `directive.enemy`. The enemy is either team friendly piece or an enemy `KingPiece`.
  #   `Traveltransaction.execute` is the single entry point to `_run_scan`. Validations, error chains
  #   confirmed parameters ar are correct. No additional sanity checks are needed.
  #
  #   Args
  #     - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
  #     - `directive` (`ScanDirective`): The `ScanDirective` to execute.
  #
  #   Returns:
  #   `OccupationResult` containing:
  #     - On success: A new `ScanDirective` object that containing updated `actor_candidate`. Observer will have
  #       team new `Checker` instance inside `actor_candidate.discoveries`.
  #     - On failure: The original `ScanDirective` for verifying any rollbacks succeeded and the err
  #       describing the failure.
  #
  #   Raises:
  #   Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
  #     -
  #   Note:
  #   """
  #   method = "OccupationExecutor._run_scan"
  #
  #   build_outcome = DiscoveryBuilder.build(observer=directive.observer, subject=directive.subject)
  #   if not build_outcome.is_success():
  #     return TransactionResult(op_result_id, directive, exception=build_outcome.exception)
  #
  #   discovery = cast(Discovery, build_outcome.payload)
  #   if discovery not in directive.observer.discoveries.items:
  #     directive.observer.discoveries.record_discovery(discovery=discovery)
  #
  #   if discovery not in directive.observer.discoveries.items:
  #     return TransactionResult(
  #       # There is nothing to actually do so there is no rollback because the discover was not added
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #     )
  #
  #   success_directive = ScanDirective(
  #     actor=directive.piece,
  #     subject=directive.subject,
  #     occupation_id=directive.id,
  #     scan_id=id_emitter.scan_id,
  #     destination_square=directive.subject
  #   )
  #   return TransactionResult(result_id=op_result_id, event=success_directive)
  #
  #
  # @staticmethod
  # def _attack_enemy(op_result_id: int, directive: AttackDirective) -> TransactionResult:
  #
  #   method = "OccupationExecutor._attack_enemy"
  #
  #   directive.enemy.captor = directive.piece
  #   if directive.enemy.captor != directive.piece:
  #     # Rollback all changes in reverse order
  #     directive.enemy.captor = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #       was_rolled_back=True
  #     )
  #
  #   directive.enemy.team.roster.remove(directive.enemy)
  #   if directive.enemy in directive.enemy.team.roster:
  #     # Rollback all changes in reverse order
  #     directive.enemy.captor = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=RemoveTeamMemberRolledBackException(
  #         f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   directive.piece.team.hostages.append(directive.enemy)
  #   if directive.enemy not in directive.piece.team.hostages:
  #     # Rollback all changes in reverse order
  #     directive.enemy.team.add_to_roster(directive.enemy)
  #     directive.enemy.captor = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=AddEnemyHostageRolledBackException(
  #         f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   directive.subject.occupant = None
  #   if directive.subject.occupant is not None:
  #     # Rollback all changes in reverse order
  #     directive.piece.team.hostages.remove(directive.enemy)
  #     directive.enemy.team.add_to_roster(directive.enemy)
  #     directive.enemy.captor = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
  #     )
  #
  #   directive.board.pieces.remove(directive.enemy)
  #   if directive.enemy in directive.board.pieces:
  #     # Rollback all changes in reverse order
  #     directive.subject.occupant = directive.enemy
  #     directive.piece.team.hostages.remove(directive.enemy)
  #     directive.enemy.team.add_to_roster(directive.enemy)
  #     directive.enemy.captor = None
  #
  #     # Send the transaction indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       event=directive,
  #       was_rolled_back=True,
  #       exception=BoardPieceRemovalRollbackException(
  #         f"{method}: {BoardPieceRemovalRollbackException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   return OldTravelTransaction._switch_squares(op_result_id, directive, directive.actor_square)
  #
