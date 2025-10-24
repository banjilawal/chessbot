"""
Builder class responsible for safely constructing `KingCheckEvent` instances.

`AttackEventBuilder` ensures that `KingCheckEvent` objects are always created successfully by performing comprehensive validate
 checks during construction. This separates the responsibility of building from validating - `AttackEventBuilder`
 focuses on creation while `AttackEventValidator` is used for validating existing `KingCheckEvent` instances that are passed
 around the system.

The build runs through all validate checks individually to guarantee that any `KingCheckEvent` instance it produces
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
  `KingCheckEvent`: The data structure being constructed
  `AttackEventValidator`: Used for validating existing `KingCheckEvent` instances
  `BuildResult`: Return type containing the built `KingCheckEvent` or error information
"""
"""
Constructs team new `KingCheckEvent` instance with comprehensive checks on the parameters and states during the
build process.

Performs individual validate checks on each component to ensure the resulting `KingCheckEvent` meets all
specifications. If all checks are passed, team `KingCheckEvent` instance will be returned. It is not necessary to perform
any additional validate checks on the returned `KingCheckEvent` instance. This method guarantees if team `BuildResult`
with team successful status is returned, the contained `KingCheckEvent` is valid and ready for use.

Args:
  `event_id`(`int`): The unique id for the attackEvent. Must pass `IdValidator` checks.
  `actor_candidate`(`Piece`): Initiates attack after successful validate`.
  `enemy`(`Piece`): The `Piece` attackned by `actor_candidate`.
  `roster`(`ExecutionContext`): `roster.board_validator` verifies `actor_candidate` and `enemy` are on the board_validator.

Returns:
  BuildResult[KingCheckEvent]: A `BuildResult` containing either:
    - On success: A valid `KingCheckEvent` instance in the payload
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
  The build runs through all the checks on parameters and state to guarantee only team valid `KingCheckEvent` is
  created, while `AttackEventValidator` is used for validating `KingCheckEvent` instances that are passed around after
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

# @staticmethod
# def _switch_squares(op_result_id: int, travel: TravelEvent, actor_square: Square) -> TransactionResult:
#   """
#   Transfers `Piece` occupying`actor_square` to `travel.blocked_square` leaving `actor_square` empty.
#   `OccupationExecutor.execute_event` is the single entry point to `_switch_squares`. Before `_switch_squares`
#   was called `execute_event`: validated the parameters, handled exceptions, and confirmed
#   `travel.blocked_square` contained either
#     * A friendly piece blocking `actor_candidate` from `blocked_square`
#     * An enemy king. Kings cannot be captured, only checked or checkmated.
#
#   Args:
#     - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
#     - `travel` (`TravelEvent`): The `TravelEvent` to be executed.
#     - `actor_square` (`Square`): The `Square` occupied by `actor_candidate`.
#
#   Returns:
#   `OccupationResult` containing:
#     - On success: A new `TravelEvent` with the updated squares and `piece`.
#     - On failure: The original `TravelEvent`or verifying any rollbacks succeeded and the err
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
#   travel.friend.occupant = travel.traveler
#   if not travel.friend.occupant == travel.traveler:
#     # Rollback all changes in reverse order
#     travel.friend.occupant = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   actor_square.occupant = None
#   if actor_square.occupant == travel.traveler:
#     # Rollback all changes in reverse order
#     actor_square.occupant = travel.traveler
#     travel.friend.occupant = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
#     )
#
#   travel.traveler.positions.push_coord(travel.friend.position)
#   if not travel.traveler.current_position == travel.friend.position:
#     # Rollback all changes in reverse order
#     travel.traveler.positions.undo_push()
#     actor_square.occupant = travel.traveler
#     travel.friend.occupant = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   return TransactionResult(
#     result_id=op_result_id,
#     travel=TravelEvent(id_emitter.event_id, travel.traveler, travel.friend)
#   )

# @staticmethod
# def execute(travel: OccupationEvent) -> TransactionResult:
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
#   method = "AttackTransaction.execute"
#
#   validation = TransferEventValidator.validate(travel)
#   if not validation.is_success():
#     return TransactionResult(travel, validation.rollback_exception)
#
#   travel.enemy.captor = travel.traveler
#   if travel.enemy.captor != travel.traveler:
#     # Rollback all changes in reverse order
#     travel.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=SetCaptorRollBackException(
#         f"{method}: {SetCaptorRollBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   travel.enemy.team.roster.remove(travel.enemy)
#   if travel.enemy in travel.enemy.team.roster:
#     # Rollback all changes in reverse order
#     travel.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=RemoveTeamMemberRolledBackException(
#         f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   travel.traveler.team.hostages.append(travel.enemy)
#   if travel.enemy not in travel.traveler.team.hostages:
#     # Rollback all changes in reverse order
#     travel.enemy.team.add_to_roster(travel.enemy)
#     travel.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=AddEnemyHostageRolledBackException(
#         f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   travel.board.pieces.remove(travel.enemy)
#   if travel.enemy in travel.board.pieces:
#     # Rollback all changes in reverse order
#     travel.traveler.team.hostages.remove(travel.enemy)
#     travel.enemy.team.add_to_roster(travel.enemy)
#     travel.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=FailedPieceRemovalRolledBackException(
#         f"{method}: {FailedPieceRemovalRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   travel.enemy_square.occupant = None
#   if not travel.enemy_square.occupant is None:
#     # Rollback all changes in reverse order
#     travel.board.pieces.add(travel.enemy_square.occupant)
#     travel.traveler.team.hostages.remove(travel.enemy)
#     travel.enemy.team.add_to_roster(travel.enemy)
#     travel.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=EmptyDestinationSquareRolledBackException(
#         f"{method}: {EmptyDestinationSquareRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#
#   transfer_event = TransferEvent(
#     parent=travel,
#     traveler=travel.traveler,
#     event_id=id_emitter.attack_id,
#     actor_square=travel.actor_square
#   )
#   return Transfer
#   travel.friend.occupant = None
#   if travel.friend.occupant is not None:
#     # Rollback all changes in reverse order
#     travel.traveler.team.hostages.remove(travel.enemy)
#     travel.enemy.team.add_to_roster(travel.enemy)
#     travel.enemy.captor = None
#
#     # Send the notification indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
#     )
#
#
#
#   return OccupationTransaction._switch_squares(op_result_id, travel, travel.actor_square)
#   search_result = BoardSearch.square_by_coord(coord=travel.traveler.current_position, board=context.board)
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
#     return OccupationTransaction._switch_squares(op_result_id, travel, actor_square)
#
#   traveler = travel.traveler
#   destination_occupant = travel.friend.occupant
#
#
#
#   attack_validation = AttackValidator.validate(
#     CaptureContext(piece=travel.traveler, enemy=destination_occupant, board=context.board)
#   )
#   if not attack_validation.is_success():
#     return TransactionResult(op_result_id, travel, attack_validation.rollback_exception)
#
#   enemy_king = cast(CombatantPiece, attack_validation.payload.enemy)
#   return OccupationTransaction._attack_enemy(
#     op_result_id=op_result_id,
#     travel=AttackEvent(
#       board=context.board,
#       traveler=travel.traveler,
#       enemy=enemy_king,
#       occupation_id=travel.id,
#       attack_id=id_emitter.attack_id,
#       actor_square=actor_square,
#       enemy_square=travel.friend
#     )
#
#

#
#
# @staticmethod
# def _run_scan(op_result_id :int, travel: ScanEvent) -> TransactionResult:
#   """
#   Creates team new `Checker` object for travel.actor_candidate which is blocking from moving to
#   `blocked_square` by `travel.enemy`. The enemy is either team friendly piece or an enemy `KingPiece`.
#   `OccupationExecutor.execute_event` is the single entry point to `_run_scan`. Validations, error chains
#   confirmed parameters ar are correct. No additional sanity checks are needed.
#
#   Args
#     - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
#     - `travel` (`BlockingEvent`): The `BlockingEvent` to execute.
#
#   Returns:
#   `OccupationResult` containing:
#     - On success: A new `BlockingEvent` object that containing updated `actor_candidate`. Observer will have
#       team new `Checker` instance inside `actor_candidate.discoveries`.
#     - On failure: The original `BlockingEvent` for verifying any rollbacks succeeded and the err
#       describing the failure.
#
#   Raises:
#   Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
#     -
#   Note:
#   """
#   method = "OccupationExecutor._run_scan"
#
#   build_outcome = DiscoveryBuilder.build(observer=travel.observer, friend=travel.friend)
#   if not build_outcome.is_success():
#     return TransactionResult(op_result_id, travel, rollback_exception=build_outcome.rollback_exception)
#
#   discovery = cast(Discovery, build_outcome.payload)
#   if discovery not in travel.observer.discoveries.items:
#     travel.observer.discoveries.record_discovery(discovery=discovery)
#
#   if discovery not in travel.observer.discoveries.items:
#     return TransactionResult(
#       # There is nothing to actually do so there is no rollback because the discover was not added
#       result_id=op_result_id,
#       travel=travel,
#       was_rolled_back=True,
#       rollback_exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   success_event = ScanEvent(
#     traveler=travel.traveler,
#     friend=travel.friend,
#     occupation_id=travel.id,
#     scan_id=id_emitter.scan_id,
#     enemy_square=travel.friend
#   )
#   return TransactionResult(result_id=op_result_id, travel=success_event)
#
#
# @staticmethod
# def _attack_enemy(op_result_id: int, travel: AttackEvent) -> TransactionResult:
#
#

# src/chess/system/travel/rollback_exception.py

"""
Module: chess.system.travel.rollback_exception
Author: Banji Lawal
Created: 2025-10-09
version: 1.0.0

# SECTION 1 - Purpose:
This module provides:
  1. A satisfaction of the `ChessBot` integrity requirement.
  2. A satisfaction of the `ChessBot` reliability requirement.

# SECTION 2 - Scope:
The module's only covers exceptions raised by `IdValidator`;

# SECTION 3: Limitations
  1. Does not provide logic for fixing the errors or causing the rollback_exception being raised.
       `IdValidator` is responsible for the logic which raises these exceptions.

# SECTION 4 - Design Considerations and Themes:
The major theme influencing the modules design are
  1. Single responsibility.
  2. Discoverability.
  3. Encapsulations.

# SECTION 5- Features Supporting Requirements:
  1. The ability to handle errors without crashing the application is a reliability feature.


# SECTION 6 - Feature Delivery Mechanism:
1. Exceptions specific to verifying ids.

# SECTION 7 - Dependencies:
* From `chess.system`:
    `ChessException`, `ContextException`, `ResultException`

# SECTION 8 - Contains:
See the list of exceptions in the `__all__` list following (e.g., `EventException`,`TransactionException`).
"""

# src/chess/vector/rollback_exception.py

"""
Module: chess.vector.rollback_exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0

SCOPE:
-----
This module is exclusively for defining all custom **rollback_exception classes** that are specific to the
creation, validation, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each field and behavior in the `Vector` class has an rollback_exception specific to its possible
      state, outcome, or behavior.

PURPOSE:
-------
1. Centralized error dictionary for the `Vector` domain.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` domain.
4. Providing a clear distinction between errors related to `Vector` instances and
    errors from Python, the Operating System or elsewhere in the `ChessBot` application.

DEPENDENCIES:
------------
Requires base rollback_exception classes and constants from the core system:
From `chess.system`:
  * Exceptions: `ChessException`, `ValidationException`, `NullException`,
        `BuildFailedException`.

CONTAINS:
--------
See the list of exceptions in the `__all__` list following (e.g., `VectorException`,
`NullVectorException`, `InvalidVectorException`, ).
"""

# from chess.rollback_exception import RollbackException
# from chess.piece.travel import OccupationEventException
#
# __all__ = [
#   #=== SCAN_TRANSACTION EXCEPTIONS #======================#
#   'ScanTransactionException',
#   'NullScanTransactionException',
#
#   #=== SCAN_EVENT EXCEPTIONS #======================#
#   'ScanEventException',
#   'InvalidScanEventException',
#   'NullEncounterEventException',
#
#   #=== SCAN_EVENT BUILD EXCEPTIONS #======================#
#   'ScanEventBuilderException',
#   'ScanSubjectException',
# ]
#
#
# __all__ = [
#   'AttackEventException',
#
#   # Specific attack errors (no rollback)
#   'UnexpectedNullEnemyException',
#
#
#   # Rollback attack errors (dual inheritance)
#   'RosterRemovalRollbackException',
#   'HostageAdditionRollbackException',
#   'BoardPieceRemovalRollbackException',
#   'SquareOccupationRollbackException',
#   'SourceSquareRollbackException',
#   'PositionUpdateRollbackException',
# ]
#
# #=== SCAN TRANSACTION EXCEPTIONS #======================#
# class ScanTransactionException(TransactionException):
#   """
#   Wraps any ScanEventExceptions or other errors raised during
#   the blocking's lifecycle.
#   """
#   ERROR_CODE = "SCAN_TRANSACTION_ERROR"
#   DEFAULT_MESSAGE = "OccupationTransaction raised an rollback_exception."
#
#
#
# #=== SCAN_EVENT EXCEPTIONS #======================#
# class AttackEventException(OccupationEventException):
#   """
#   Base class for exceptions raised during attack/capture operations.
#
#   PURPOSE:
#     Used when an error occurs in the course of an attack or capture
#     (e.g., invalid target, rollback during capture, inconsistent board_validator state).
#   """
#   DEFAULT_CODE = "ATTACK_ERROR"
#   DEFAULT_MESSAGE = "An error occurred during an attack or capture notification."
#
#
#
# #=== ATTACK_EVENT VALIDATION EXCEPTIONS #======================#
# class NullAttackEventException(AttackEventException, NullException):
#   """Raised by methods, entities, and models that require team KingCheckEvent but receive team null."""
#   ERROR_CODE = "NULL_EVENT_ERROR"
#   DEFAULT_MESSAGE = "KingCheckEvent cannot be null"
#
# class InvalidAttackEventException(AttackEventException, ValidationException):
#   """Raised by ExchangeValidators if client fails validation."""
#   ERROR_CODE = "ATTACK_EVENT_VALIDATION_ERROR"
#   DEFAULT_MESSAGE = "KingCheckEvent failed validate"
#
#
# #=== ATTACK_EVENT BUILD EXCEPTIONS #======================#
# class AttackEventBuilderException(AttackEventException, BuilderException):
#   """
#   Indicates Coord could not be built. Wraps and re-raises errors that occurred
#   during build.
#   """
#   ERROR_CODE = "ATTACK_EVENT_BUILD_FAILED_ERROR"
#   DEFAULT_MESSAGE = "AttackEventBuilder failed to create team KingCheckEvent"
#
#
# #=== ATTACK_EVENT BUILD EXCEPTIONS #======================#
# class UnexpectedNullEnemyException(AttackEventException):
#   DEFAULT_CODE = "UNEXPECTED_NULL_ENEMY"
#   DEFAULT_MESSAGE = "Target actor_candidate is unexpectedly null during capture; this should not happen."
#
#
#
#
#
# # --- Rollback Attack Errors (Dual Inheritance) ---
# class SetCaptorRolledBackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
#   DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."
#
#
# class EmptyDestinationSquareRolledBackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "SET_CAPTOR_ERROR_ROLLED_BACK"
#   DEFAULT_MESSAGE = "Setting captor failed. Transaction rolled back performed."
#
#
# class RosterRemovalRollbackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "ROSTER_REMOVAL_ROLLBACK"
#   DEFAULT_MESSAGE = "Failed to remove actor_candidate from enemy roster after assigning captor; rollback performed."
#
#
# class HostageAdditionRollbackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "HOSTAGE_ADDITION_ROLLBACK"
#   DEFAULT_MESSAGE = "Failed to add captured actor_candidate to captor's hostage list; rollback performed."
#
#
# class BoardPieceRemovalRollbackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "BOARD_REMOVAL_ROLLBACK"
#   DEFAULT_MESSAGE = "Failed to remove captured actor_candidate from board_validator; rollback performed."
#
#
# class SquareOccupationRollbackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "SQUARE_OCCUPATION_ROLLBACK"
#   DEFAULT_MESSAGE = "Failed to occupation target square after capture; rollback executed."
#
#
# class SourceSquareRollbackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "SOURCE_SQUARE_ROLLBACK"
#   DEFAULT_MESSAGE = "Failed to clear attacker's source square; rollback executed."
#
#
# class PositionUpdateRollbackException(AttackEventException, RollbackException):
#   DEFAULT_CODE = "POSITION_UPDATE_ROLLBACK"
#   DEFAULT_MESSAGE = "Failed to update actor_candidate's position history after move; rollback executed."
