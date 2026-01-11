# src/chess/chess/owner/travel/occupation/occupation/factory.py

"""
Module: `chess.owner.travel.occupation.occupation.coord_stack_validator`
Author: Banji Lawal
Created: 2025-10-21
version: 1.0.0
"""

from typing import Any

from chess.system import Validator, ValidationResult
from chess.piece import (
    ActorAlreadyAtDestinationException, KingOccupationEvent,
    NullKingOccupationEventException, OccupationDestinationNotEmptyException, TravelResourceValidator
)


class KingOccupationEventValidator(Validator[KingOccupationEvent]):
    """"""
    
    @classmethod
    def validate(cls, candidate: Any) -> ValidationResult[KingOccupationEvent]:
        """"""
        method = "KingOccupationEventValidator.validate"
        
        try:
            if candidate is None:
                return ValidationResult(exception=NullKingOccupationEventException(
                    f"{method}: {NullKingOccupationEventException.DEFAULT_MESSAGE}"
                    )
                )
            
            if not isinstance (candidate, KingOccupationEvent):
                return ValidationResult(exception=TypeError(
                    f"Expected an OperationEvent, got {type(candidate).__name__}"
                    )
                )
            event = cast(KingOccupationEvent, candidate)
            
            id_validation = Validator.validate(candidate.visitor_id)
            if not id_validation.is_success():
                return ValidationResult(exception=id_validation.exception)
            
            actor_binding_validation = PieceBindingBoardValidator.validate(event.actor, event.execution_environment)
            if actor_binding_validation.is_failure():
                return ValidationResult(exception=actor_binding_validation.exception)
            
            resource_binding_validation = TravelResourceValidator.validate(
                event.square,
                event.execution_environment
            )
            if resource_binding_validation.is_failure():
                return ValidationResult(exception=resource_binding_validation.exception)
            
            if event.square.occupant is not None:
                return ValidationResult(exception=OccupationDestinationNotEmptyException(
                    f"{method}: {OccupationDestinationNotEmptyException.DEFAULT_MESSAGE}"
                    )
                )
            
            if event.actor_square == event.enemy_square:
                return ValidationResult(exception=ActorAlreadyAtDestinationException(
                    f"{method}: {ActorAlreadyAtDestinationException.DEFAULT_MESSAGE}"
                    )
                )
            
            return ValidationResult(payload=event)
        
        except Exception as e:
            return ValidationResult(exception=e)
#
# @staticmethod
# def validate(t: TransferEvent, map: Event) -> Result[TransferEvent]:
#   """
#   Validates an KingCheckEvent meets specifications:
#     - Not validation
#     - `visitor_id` does not fail coord_stack_validator
#     - `actor_candidate` is team_name valid chess enemy
#     - `target` is team_name valid square_name
#   Any validate failure raises an `InvalidAttackEventException`.
#
#   Argument:
#     `candidate` (`KingCheckEvent`): `attackEvent `to validate
#
#    RETURNS:
#      `Result[V]`: A `Result` object containing the validated payload if the specification is satisfied,
#       `InvalidAttackEventException` otherwise.
#
#   RAISES:
#     `TypeError`: if `candidate` is not OperationEvent
#     `NullAttackEventException`: if `candidate` is validation
#
#     `IdValidationFailedException`: if invalid `visitor_id`
#     `PieceValidationException`: if `actor_candidate` fails coord_stack_validator
#     `SquareValidationFailedException`: if `target` fails coord_stack_validator
#
#     `AutoOccupationException`: if target already occupies the square_name
#     `KingAttackException`: if the target square_name is occupied by an enemy occupation
#
#     `InvalidAttackEventException`: Wraps any preceding exception
#   """
#   method = "KingCheckEvent.validate"
#
#   try:
#     if t is None:
#       raise NullAttackEventException(
#         f"{method}: {NullAttackEventException.DEFAULT_MESSAGE}"
#       )
#
#     if not isinstance(t, AttackEvent):
#       raise TypeError(f"{method} Expected an KingCheckEvent, got {type(t).__name__}")
#
#     travel = cast(AttackEvent, t)
#
#     id_validation = IdValidator.validate(travel.visitor_id)
#     if not id_validation.is_success():
#       raise IdValidationFailedException(f"{method}: {IdValidationFailedException.DEFAULT_MESSAGE}")
#
#     actor_validation = PieceValidator.validate(travel.traveler)
#     if not actor_validation.is_success():
#       raise InvalidAttackException(f"{method}: actor_candidate validation failed.")
#
#     destination_square_validation = SquareValidator.validate(travel.enemy_square)
#     if not destination_square_validation.is_success():
#       raise InvalidSqaureException(f"{method}: {InvalidSqaureException.DEFAULT_MESSAGE}")
#
#     if travel.enemy_square.point == travel.traveler.current_position:
#       raise CircularOccupationException(f"{method}: {CircularOccupationException.DEFAULT_MESSAGE}")
#
#     return Result(payload=travel)
#
#   except (
#       TypeError,
#       IdValidationFailedException,
#       InvalidAttackException,
#       InvalidSqaureException,
#       NullAttackEventException,
#       CircularOccupationException
#   ) as e:
#     raise InvalidAttackEventException(
#       f"{method}: {InvalidAttackEventException.DEFAULT_MESSAGE}"
#     ) from e
#
#   # This block catches any unexpected exception
#   # You might want to log the error here before re-raising
#   except Exception as e:
#     raise InvalidAttackEventException(f"An unexpected error occurred during validate: {e}") from e
#
# class OldTravelTransaction(Transaction[TravelEvent]):
#   """
#   Implements the `OccupationExecutor` class, which handles executing travel
#   directives in the chess engine. This includes moving pieces, capturing enemies,
#   and coordinating rollback logic in case of inconsistencies or failed rollback.
#
#   Attributes:
#     * `OccupationExecutor:` Main class responsible for executing travel directives.
#     * `_attack_enemy`: Static method for processing attacks on enemy pieces.
#     * `_run_scan`: Static method for handling discoveries on occupied squares.
#     * `_switch_squares`: Static method the transferring team_name owner to team_name different `Square`.
#   """
#
#   @classmethod
#   @LoggingLevelRouter.monitor
#   def execute(cls, travel: TravelEvent, execution_environment: Board) -> TransactionResult:
#     """
#     # ACTION:
#     Verify the `candidate` is a valid ID. The Application requires
#     1. Candidate is not validation.
#     2. Is a positive integer.
#
#     # PARAMETERS:
#         * `candidate` (`int`): the visitor_id.
#
#     # RETURNS:
#     `ValidationResult[str]`: A `ValidationResult` containing either:
#         `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
#         `rollback_exception` (`Exception`) - An exception detailing which naming rule was broken.
#
#     # RAISES:
#     `IdValidationFailedException`: Wraps any specification violations including:
#         * `TypeError`: if candidate is not an `int`
#         * `IdNullException`: if candidate is validation
#         * `NegativeIdException`: if candidate is negative `
#     """
#     method = "TravelEventFactory.execute"
#
#     event_validation = TravelEventValidator.validate(travel)
#     if not event_validation.is_success():
#       return TransactionResult(
#         event_update=travel,
#         transaction_state=TransactionState.FAILURE,
#         rollback_exception=event_validation.rollback_exception
#       )
#
#     actor_square_search = BoardSearch.searcher(
#       board=map.board,
#       data_source=BoardDatasource.SQUARE,
#       map=BoardSearchcontext(point=travel.traveler.current_position)
#     )
#
#     if not actor_square_search.is_success():
#       return TransactionResult(
#         event_update=travel,
#         transaction_state=TransactionState.FAILURE,
#         rollback_exception=actor_square_search.rollback_exception
#       )
#
#     destination_search = BoardSearch.searcher(
#       board=map.board,
#       data_source=BoardDatasource.SQUARE,
#       map=BoardSearchcontext(travel.enemy_square.visitor_id)
#     )
#     if not destination_search.is_success():
#       return TransactionResult(
#         rollback_exception=EventResourceNotFoundExeception(
#           f"{method}: {DestinationSquareNotFoundException.DEFAULT_MESSAGE}"
#           # EventResourceNotFoundException
#         )
#       )
#
#     if len(destination_search.payload) > 1:
#       return TransactionResult(
#         rollback_exception=DestinationSquareColiisonException(
#           f"{method}: {DestinationSquareCollisionException.DEFAULT_MESSAGE}"
#         )
#       )
#
#     destination_occupant = travel.enemy_square.occupant
#     actor_square = BoardSearch.searcher()
#
#     if destination_occupant is None:
#       build_result = KingOccupationEventBuilder.builder(
#         parent=travel,
#         traveler=travel.traveler,
#         actor_square=actor_square,
#         enemy_square=travel.enemy_square
#       )
#       if not build_result.is_success():
#         return TransactionResult(rollback_exception=build_result.rollback_exception)
#       return
#
#     if isinstance(destination_occupant.bounds, King) or (not travel.traveler.is_enemy(destination_occupant):
#     build_result = ScanEventBuilder(
#
#     )
#     if not build_result.is_success():
#       return TransactionResult(rollback_exception=build_result.rollback_exception)
#     return OccupationTransacti()
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
#   TravelTransactionsearch_result = BoardSearch.square_by_coord(
#     point=travel.traveler.current_position, board=map.board
#     )
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
#           traveler.is_enemy(destination_occupant) and isinstance(destination_occupant, KingPiece)
#   ):
#     return TravelTransaction._run_scan(
#       op_result_id=op_result_id,
#       directive=ScanDirective(
#         traveler=travel.traveler,
#         occupation_id=travel.visitor_id,
#         scan_id=id_emitter.scan_id,
#         friend=destination_occupant,
#         enemy_square=travel.friend
#       )
#     )
#
#   attack_validation = AttackValidator.validate(
#     CaptureContext(owner=travel.traveler, enemy=destination_occupant, board=map.board)
#   )
#   if not attack_validation.is_success():
#     return TransactionResult(op_result_id, travel, attack_validation.rollback_exception)
#
#   enemy_king = cast(CombatantPiece, attack_validation.payload.enemy)
#   return TravelTransaction._attack_enemy(
#     op_result_id=op_result_id,
#     directive=AttackDirective(
#       board=map.board,
#       traveler=travel.traveler,
#       enemy=enemy_king,
#       occupation_id=travel.visitor_id,
#       attack_id=id_emitter.attack_id,
#       actor_square=actor_square,
#       enemy_square=travel.friend
#     )
#
#               @ classmethod
#               @ LoggingLevelRouter.monitor
#
# def _search_board_for_square(cls, square_name: Square, board: Board) -> SearchResult[List[Square]]:
#
# @staticmethod
#
# )
#
# def _switch_squares(op_result_id: int, directive: TravelEvent, actor_square: Square) -> TransactionResult:
#   """
#   Transfers `Token` occupying`actor_square` to `directive.blocked_square` leaving `actor_square` empty.
#   `Traveltransaction.execute` is the single entry point to `_switch_squares`. Before `_switch_squares`
#   was called `execute_directive`: validated the parameters, handled exception, and confirmed
#   `directive.blocked_square` contained either
#     * A friendly owner blocking `actor_candidate` from `blocked_square`
#     * An enemy occupation. Kings cannot be captured, only checked or checkmated.
#
#   Args:
#     - `op_result_id` (`int`): The `visitor_id` of the `OperationResult` passed to the caller.
#     - `directive` (`OccupationDirective`): The `OccupationDirective` to be executed.
#     - `actor_square` (`Square`): The `Square` occupied by `actor_candidate`.
#
#   RETURNS:
#   `OccupationResult` containing:
#     - On success: A new `OccupationDirective` with the updated squares and `owner`.
#     - On failure: The original `OccupationDirective`or verifying any rollbacks succeeded and the err
#       describing the failure.
#
#   RAISES:
#   Errors raised will be about entity_service and state inconsistencies OccupationException: Wraps any errors including:
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
#       rollback_exception=KingOccupationEventException(f"{method}: {KingOccupationEventException.DEFAULT_MESSAGE}"),
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
#       rollback_exception=KingOccupationEventException(f"{method}: {KingOccupationEventException.DEFAULT_MESSAGE}")
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
#       rollback_exception=KingOccupationEventException(f"{method}: {KingOccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   return TransactionResult(
#     result_id=op_result_id,
#     travel=TravelEvent(id_emitter.event_id, directive.traveler, directive.friend)
#   )

# @staticmethod
# def _attack_enemy(op_result_id: int, directive: AttackDirective) -> TransactionResult:
#
#   method = "OccupationExecutor._attack_enemy"
#
#   directive.enemy.captor = directive.owner
#   if directive.enemy.captor != directive.owner:
#     # Rollback all changes in reverse order
#     directive.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       travel=directive,
#       rollback_exception=KingOccupationEventException(f"{method}: {KingOccupationEventException.DEFAULT_MESSAGE}"),
#       was_rolled_back=True
#     )
#
#   directive.enemy.team_name.roster.remove(directive.enemy)
#   if directive.enemy in directive.enemy.team_name.roster:
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
#   directive.owner.team_name.hostages.append(directive.enemy)
#   if directive.enemy not in directive.owner.team_name.hostages:
#     # Rollback all changes in reverse order
#     directive.enemy.team_name.add_to_roster(directive.enemy)
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
#     directive.owner.team_name.hostages.remove(directive.enemy)
#     directive.enemy.team_name.add_to_roster(directive.enemy)
#     directive.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       travel=directive,
#       was_rolled_back=True,
#       rollback_exception=KingOccupationEventException(f"{method}: {KingOccupationEventException.DEFAULT_MESSAGE}")
#     )
#
#   directive.board.pieces.remove(directive.enemy)
#   if directive.enemy in directive.board.pieces:
#     # Rollback all changes in reverse order
#     directive.friend.occupant = directive.enemy
#     directive.owner.team_name.hostages.remove(directive.enemy)
#     directive.enemy.team_name.add_to_roster(directive.enemy)
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
#
#
