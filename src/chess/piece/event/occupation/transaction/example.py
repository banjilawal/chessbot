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