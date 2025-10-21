"""
Builder class responsible for safely constructing `CheckEvent` instances.

`AttackEventBuilder` ensures that `CheckEvent` objects are always created successfully by performing comprehensive validate
 checks during construction. This separates the responsibility of building from validating - `AttackEventBuilder`
 focuses on creation while `AttackEventValidator` is used for validating existing `CheckEvent` instances that are passed
 around the system.

The build runs through all validate checks individually to guarantee that any `CheckEvent` instance it produces
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
  `CheckEvent`: The data structure being constructed
  `AttackEventValidator`: Used for validating existing `CheckEvent` instances
  `BuildResult`: Return type containing the built `CheckEvent` or error information
"""
"""
Constructs team new `CheckEvent` instance with comprehensive checks on the parameters and states during the
build process.

Performs individual validate checks on each component to ensure the resulting `CheckEvent` meets all
specifications. If all checks are passed, team `CheckEvent` instance will be returned. It is not necessary to perform
any additional validate checks on the returned `CheckEvent` instance. This method guarantees if team `BuildResult`
with team successful status is returned, the contained `CheckEvent` is valid and ready for use.

Args:
  `event_id`(`int`): The unique id for the attackEvent. Must pass `IdValidator` checks.
  `actor_candidate`(`Piece`): Initiates attack after successful validate`.
  `enemy`(`Piece`): The `Piece` attackned by `actor_candidate`.
  `roster`(`ExecutionContext`): `roster.board_validator` verifies `actor_candidate` and `enemy` are on the board_validator.

Returns:
  BuildResult[CheckEvent]: A `BuildResult` containing either:
    - On success: A valid `CheckEvent` instance in the payload
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
  The build runs through all the checks on parameters and state to guarantee only team valid `CheckEvent` is
  created, while `AttackEventValidator` is used for validating `CheckEvent` instances that are passed around after
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
# def _switch_squares(op_result_id: int, event: TravelEvent, actor_square: Square) -> TransactionResult:
#   """
#   Transfers `Piece` occupying`actor_square` to `event.subject_square` leaving `actor_square` empty.
#   `OccupationExecutor.execute_event` is the single entry point to `_switch_squares`. Before `_switch_squares`
#   was called `execute_event`: validated the parameters, handled exceptions, and confirmed
#   `event.subject_square` contained either
#     * A friendly piece blocking `actor_candidate` from `subject_square`
#     * An enemy king. Kings cannot be captured, only checked or checkmated.
#
#   Args:
#     - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
#     - `event` (`TravelEvent`): The `TravelEvent` to be executed.
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
#   *  If the transaction fails, `OperationResult.was_rolled_back = True`
#   """
#   method = "OccupationExecutor._switch_squares"
#
#   event.subject.occupant = event.actor
#   if not event.subject.occupant == event.actor:
#     # Rollback all changes in reverse order
#     event.subject.occupant = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       event=event,
#       was_rolled_back=True,
#       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   actor_square.occupant = None
#   if actor_square.occupant == event.actor:
#     # Rollback all changes in reverse order
#     actor_square.occupant = event.actor
#     event.subject.occupant = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       event=event,
#       was_rolled_back=True,
#       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
#     )
#
#   event.actor.positions.push_coord(event.subject.position)
#   if not event.actor.current_position == event.subject.position:
#     # Rollback all changes in reverse order
#     event.actor.positions.undo_push()
#     actor_square.occupant = event.actor
#     event.subject.occupant = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       event=event,
#       was_rolled_back=True,
#       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   return TransactionResult(
#     result_id=op_result_id,
#     event=TravelEvent(id_emitter.event_id, event.actor, event.subject)
#   )

# @staticmethod
# def execute(event: OccupationEvent) -> TransactionResult:
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
#   method = "AttackTransaction.execute"
#
#   validation = TransferEventValidator.validate(event)
#   if not validation.is_success():
#     return TransactionResult(event, validation.exception)
#
#   event.enemy.captor = event.actor
#   if event.enemy.captor != event.actor:
#     # Rollback all changes in reverse order
#     event.enemy.captor = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       event=event,
#       was_rolled_back=True,
#       exception=SetCaptorRollBackException(
#         f"{method}: {SetCaptorRollBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   event.enemy.team.roster.remove(event.enemy)
#   if event.enemy in event.enemy.team.roster:
#     # Rollback all changes in reverse order
#     event.enemy.captor = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       event=event,
#       was_rolled_back=True,
#       exception=RemoveTeamMemberRolledBackException(
#         f"{method}: {RemoveTeamMemberRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   event.actor.team.hostages.append(event.enemy)
#   if event.enemy not in event.actor.team.hostages:
#     # Rollback all changes in reverse order
#     event.enemy.team.add_to_roster(event.enemy)
#     event.enemy.captor = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       event=event,
#       was_rolled_back=True,
#       exception=AddEnemyHostageRolledBackException(
#         f"{method}: {AddEnemyHostageRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   event.board.pieces.remove(event.enemy)
#   if event.enemy in event.board.pieces:
#     # Rollback all changes in reverse order
#     event.actor.team.hostages.remove(event.enemy)
#     event.enemy.team.add_to_roster(event.enemy)
#     event.enemy.captor = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       event=event,
#       was_rolled_back=True,
#       exception=FailedPieceRemovalRolledBackException(
#         f"{method}: {FailedPieceRemovalRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#   event.destination_square.occupant = None
#   if not event.destination_square.occupant is None:
#     # Rollback all changes in reverse order
#     event.board.pieces.add(event.destination_square.occupant)
#     event.actor.team.hostages.remove(event.enemy)
#     event.enemy.team.add_to_roster(event.enemy)
#     event.enemy.captor = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       event=event,
#       was_rolled_back=True,
#       exception=EmptyDestinationSquareRolledBackException(
#         f"{method}: {EmptyDestinationSquareRolledBackException.DEFAULT_MESSAGE}"
#       )
#     )
#
#
#   transfer_event = TransferEvent(
#     parent=event,
#     actor=event.actor,
#     event_id=id_emitter.attack_id,
#     actor_square=event.actor_square
#   )
#   return Transfer
#   event.subject.occupant = None
#   if event.subject.occupant is not None:
#     # Rollback all changes in reverse order
#     event.actor.team.hostages.remove(event.enemy)
#     event.enemy.team.add_to_roster(event.enemy)
#     event.enemy.captor = None
#
#     # Send the transaction indicating rollback
#     return TransactionResult(
#       result_id=op_result_id,
#       event=event,
#       was_rolled_back=True,
#       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}")
#     )
#
#
#
#   return OccupationTransaction._switch_squares(op_result_id, event, event.actor_square)
#   search_result = BoardSearch.square_by_coord(coord=event.actor.current_position, board=context.board)
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
#     return OccupationTransaction._switch_squares(op_result_id, event, actor_square)
#
#   actor = event.actor
#   destination_occupant = event.subject.occupant
#
#
#
#   attack_validation = AttackValidator.validate(
#     CaptureContext(piece=event.actor, enemy=destination_occupant, board=context.board)
#   )
#   if not attack_validation.is_success():
#     return TransactionResult(op_result_id, event, attack_validation.exception)
#
#   enemy_combatant = cast(CombatantPiece, attack_validation.payload.enemy)
#   return OccupationTransaction._attack_enemy(
#     op_result_id=op_result_id,
#     event=AttackEvent(
#       board=context.board,
#       actor=event.actor,
#       enemy=enemy_combatant,
#       occupation_id=event.id,
#       attack_id=id_emitter.attack_id,
#       actor_square=actor_square,
#       destination_square=event.subject
#     )
#
#

#
#
# @staticmethod
# def _run_scan(op_result_id :int, event: ScanEvent) -> TransactionResult:
#   """
#   Creates team new `Checker` object for event.actor_candidate which is blocked from moving to
#   `subject_square` by `event.enemy`. The enemy is either team friendly piece or an enemy `KingPiece`.
#   `OccupationExecutor.execute_event` is the single entry point to `_run_scan`. Validations, error chains
#   confirmed parameters ar are correct. No additional sanity checks are needed.
#
#   Args
#     - `op_result_id` (`int`): The `id` of the `OperationResult` passed to the caller.
#     - `event` (`EncounterEvent`): The `EncounterEvent` to execute.
#
#   Returns:
#   `OccupationResult` containing:
#     - On success: A new `EncounterEvent` object that containing updated `actor_candidate`. Observer will have
#       team new `Checker` instance inside `actor_candidate.discoveries`.
#     - On failure: The original `EncounterEvent` for verifying any rollbacks succeeded and the err
#       describing the failure.
#
#   Raises:
#   Errors raised will be about data and state inconsistencies OccupationException: Wraps any errors including:
#     -
#   Note:
#   """
#   method = "OccupationExecutor._run_scan"
#
#   build_outcome = DiscoveryBuilder.build(observer=event.observer, subject=event.subject)
#   if not build_outcome.is_success():
#     return TransactionResult(op_result_id, event, exception=build_outcome.exception)
#
#   discovery = cast(Discovery, build_outcome.payload)
#   if discovery not in event.observer.discoveries.items:
#     event.observer.discoveries.record_discovery(discovery=discovery)
#
#   if discovery not in event.observer.discoveries.items:
#     return TransactionResult(
#       # There is nothing to actually do so there is no rollback because the discover was not added
#       result_id=op_result_id,
#       event=event,
#       was_rolled_back=True,
#       exception=OccupationEventException(f"{method}: {OccupationEventException.DEFAULT_MESSAGE}"),
#     )
#
#   success_event = ScanEvent(
#     actor=event.actor,
#     subject=event.subject,
#     occupation_id=event.id,
#     scan_id=id_emitter.scan_id,
#     destination_square=event.subject
#   )
#   return TransactionResult(result_id=op_result_id, event=success_event)
#
#
# @staticmethod
# def _attack_enemy(op_result_id: int, event: AttackEvent) -> TransactionResult:
#
#
