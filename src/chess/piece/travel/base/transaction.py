# src/chess/piece/travel/base/transaction.py

"""
Module: chess.piece.travel.base.transaction
Author: Banji Lawal
Created: 2025-09-28
"""

from abc import abstractmethod

from chess.piece import TravelEvent
from chess.system import LoggingLevelRouter, Transaction, TransactionResult


class TravelTransaction(Transaction[TravelEvent]):
  _event = TravelEvent

  def __init__(self, event: TravelEvent):
    super().__init__(event)

  @abstractmethod
  @LoggingLevelRouter.monitor
  def execute(self, event: TravelEvent) -> TransactionResult:
    pass
  # """
  # Implements the `OccupationExecutor` class, which handles executing travel
  # directives in the chess engine. This includes moving pieces, capturing enemies,
  # and coordinating rollback logic in case of inconsistencies or failed operations.
  #
  # Attributes:
  #   * `OccupationExecutor:` Main class responsible for executing travel directives.
  #   * `_attack_enemy`: Static method for processing attacks on enemy pieces.
  #   * `_run_scan`: Static method for handling discoveries on occupied squares.
  #   * `_switch_squares`: Static method the transferring team piece to team different `Square`.
  # """
  # @classmethod
  # @LoggingLevelRouter.monitor
  # def execute(cls, travel: TravelEvent, execution_environment: Board) -> TransactionResult:
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
  #       `rollback_exception` (`Exception`) - An rollback_exception detailing which naming rule was broken.
  #
  #   # RAISES:
  #   `InvalidIdException`: Wraps any specification violations including:
  #       * `TypeError`: if candidate is not an `int`
  #       * `IdNullException`: if candidate is null
  #       * `NegativeIdException`: if candidate is negative `
  #   """
  #   method = "TravelEventFactory.execute"
  #
  #   event_validation = TravelEventValidator.validate(travel)
  #   if not event_validation.is_success():
  #     return TransactionResult(
  #       event_update=travel,
  #       transaction_state=TransactionState.FAILURE,
  #       rollback_exception=event_validation.rollback_exception
  #     )
  #
  #   actor_square_search = BoardSearch.search(
  #     board=context.board,
  #     data_source=BoardDatasource.SQUARE,
  #     context=BoardSearchcontext(coord=travel.traveler.current_position)
  #   )
  #
  #   if not actor_square_search.is_success():
  #     return TransactionResult(
  #       event_update=travel,
  #       transaction_state=TransactionState.FAILURE,
  #       rollback_exception=actor_square_search.rollback_exception
  #     )
  #
  #   destination_search = BoardSearch.search(
  #     board=context.board,
  #     data_source=BoardDatasource.SQUARE,
  #     context=BoardSearchcontext(travel.enemy_square.id)
  #   )
  #   if not destination_search.is_success():
  #     return TransactionResult(rollback_exception=EventResourceNotFoundExeception(
  #         f"{method}: {DestinationSquareNotFoundException.DEFAULT_MESSAGE}"
  #       # EventResourceNotFoundException
  #       )
  #     )
  #
  #   if len(destination_search.payload) > 1:
  #     return TransactionResult(rollback_exception=DestinationSquareColiisonException(
  #         f"{method}: {DestinationSquareCollisionException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   destination_occupant = travel.enemy_square.occupant
  #   actor_square = BoardSearch.search()
  #
  #   if destination_occupant is None:
  #     build_result = OccupationEventBuilder.build(
  #       parent=travel,
  #       traveler=travel.traveler,
  #       actor_square=actor_square,
  #       enemy_square=travel.enemy_square
  #     )
  #     if not build_result.is_success():
  #       return TransactionResult(rollback_exception=build_result.rollback_exception)
  #     return
  #
  #   if isinstance(destination_occupant.rank, King) or (not travel.traveler.is_enemy(destination_occupant):
  #     build_result = ScanEventBuilder(
  #
  #     )
  #     if not build_result.is_success():
  #       return TransactionResult(rollback_exception=build_result.rollback_exception)
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
  #   TravelTransactionsearch_result = BoardSearch.square_by_coord(coord=travel.traveler.current_position, board=context.board)
  #   if search_result.rollback_exception is not None:
  #     return TransactionResult(op_result_id, travel, search_result.rollback_exception)
  #
  #   if search_result.is_empty():
  #     return TransactionResult(
  #       op_result_id,
  #       travel,
  #       OccupationSearchEventException(f"{method}: {OccupationSearchEventException.DEFAULT_MESSAGE}")
  #     )
  #   actor_square = cast(Square, search_result.payload)
  #
  #   if travel.friend.occupant is None:
  #     return TravelTransaction._switch_squares(op_result_id, travel, actor_square)
  #
  #   traveler = travel.traveler
  #   destination_occupant = travel.friend.occupant
  #   if not traveler.is_enemy(destination_occupant) or (
  #     traveler.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
  #   ):
  #     return TravelTransaction._run_scan(
  #       op_result_id=op_result_id,
  #       directive=ScanDirective(
  #         traveler=travel.traveler,
  #         occupation_id=travel.id,
  #         scan_id=id_emitter.scan_id,
  #         friend=destination_occupant,
  #         enemy_square=travel.friend
  #       )
  #     )
  #
  #
  #   attack_validation = AttackValidator.validate(
  #     CaptureContext(piece=travel.traveler, enemy=destination_occupant, board=context.board)
  #   )
  #   if not attack_validation.is_success():
  #     return TransactionResult(op_result_id, travel, attack_validation.rollback_exception)
  #
  #   enemy_king = cast(CombatantPiece, attack_validation.payload.enemy)
  #   return TravelTransaction._attack_enemy(
  #     op_result_id=op_result_id,
  #     directive=AttackDirective(
  #       board=context.board,
  #       traveler=travel.traveler,
  #       enemy=enemy_king,
  #       occupation_id=travel.id,
  #       attack_id=id_emitter.attack_id,
  #       actor_square=actor_square,
  #       enemy_square=travel.friend
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
  #   Transfers `Piece` occupying`actor_square` to `directive.blocked_square` leaving `actor_square` empty.
  #   `Traveltransaction.execute` is the single entry point to `_switch_squares`. Before `_switch_squares`
  #   was called `execute_directive`: validated the parameters, handled exceptions, and confirmed
  #   `directive.blocked_square` contained either
  #     * A friendly piece blocking `actor_candidate` from `blocked_square`
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
  #   *  If the notification fails, `OperationResult.was_rolled_back = True`
  #   """
  #   method = "OccupationExecutor._switch_squares"
  #
  #   directive.friend.occupant = directive.traveler
  #   if not directive.friend.occupant == directive.traveler:
  #     # Rollback all changes in reverse order
  #     directive.friend.occupant = None
  #
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #     )
  #
  #   actor_square.occupant = None
  #   if actor_square.occupant == directive.traveler:
  #     # Rollback all changes in reverse order
  #     actor_square.occupant = directive.traveler
  #     directive.friend.occupant = None
  #
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
  #     )
  #
  #   directive.traveler.positions.push_coord(directive.friend.position)
  #   if not directive.traveler.current_position == directive.friend.position:
  #     # Rollback all changes in reverse order
  #     directive.traveler.positions.undo_push()
  #     actor_square.occupant = directive.traveler
  #     directive.friend.occupant = None
  #
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #     )
  #
  #   return TransactionResult(
  #     result_id=op_result_id,
  #     travel=TravelEvent(id_emitter.event_id, directive.traveler, directive.friend)
  #   )
  #
  #
  # @staticmethod
  # def _run_scan(op_result_id :int, directive: ScanDirective) -> TransactionResult:
  #   """
  #   Creates team new `Checker` object for directive.actor_candidate which is blocking from moving to
  #   `blocked_square` by `directive.enemy`. The enemy is either team friendly piece or an enemy `KingPiece`.
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
  #   build_outcome = DiscoveryBuilder.build(observer=directive.observer, friend=directive.friend)
  #   if not build_outcome.is_success():
  #     return TransactionResult(op_result_id, directive, rollback_exception=build_outcome.rollback_exception)
  #
  #   discovery = cast(Discovery, build_outcome.payload)
  #   if discovery not in directive.observer.discoveries.items:
  #     directive.observer.discoveries.record_discovery(discovery=discovery)
  #
  #   if discovery not in directive.observer.discoveries.items:
  #     return TransactionResult(
  #       # There is nothing to actually do so there is no rollback because the discover was not added
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #     )
  #
  #   success_directive = ScanDirective(
  #     traveler=directive.piece,
  #     friend=directive.friend,
  #     occupation_id=directive.id,
  #     scan_id=id_emitter.scan_id,
  #     enemy_square=directive.friend
  #   )
  #   return TransactionResult(result_id=op_result_id, travel=success_directive)
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
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
  #       was_rolled_back=True
  #     )
  #
  #   directive.enemy.team.roster.remove(directive.enemy)
  #   if directive.enemy in directive.enemy.team.roster:
  #     # Rollback all changes in reverse order
  #     directive.enemy.captor = None
  #
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=RemoveTeamMemberRolledBackException(
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
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=AddEnemyHostageRolledBackException(
  #         f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   directive.friend.occupant = None
  #   if directive.friend.occupant is not None:
  #     # Rollback all changes in reverse order
  #     directive.piece.team.hostages.remove(directive.enemy)
  #     directive.enemy.team.add_to_roster(directive.enemy)
  #     directive.enemy.captor = None
  #
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
  #     )
  #
  #   directive.board.pieces.remove(directive.enemy)
  #   if directive.enemy in directive.board.pieces:
  #     # Rollback all changes in reverse order
  #     directive.friend.occupant = directive.enemy
  #     directive.piece.team.hostages.remove(directive.enemy)
  #     directive.enemy.team.add_to_roster(directive.enemy)
  #     directive.enemy.captor = None
  #
  #     # Send the notification indicating rollback
  #     return TransactionResult(
  #       result_id=op_result_id,
  #       travel=directive,
  #       was_rolled_back=True,
  #       rollback_exception=BoardPieceRemovalRollbackException(
  #         f"{method}: {BoardPieceRemovalRollbackException.DEFAULT_MESSAGE}"
  #       )
  #     )
  #
  #   return OldTravelTransaction._switch_squares(op_result_id, directive, directive.actor_square)
  #
