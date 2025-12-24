
  """
  Builder class responsible for safely constructing `BlockingEvent` instances.

  `EncounterEventBuilder` ensures that `BlockingEvent` objects are always created successfully by performing comprehensive validate
   checks during construction. This separates the responsibility of building from validating - `EncounterEventBuilder`
   focuses on creation while `ScanEventValidator` is used for validating existing `BlockingEvent` instances that are passed
   around the system.

  The builder runs through all validate checks individually to guarantee that any `BlockingEvent` instance it produces
  meets all required specifications before construction completes

  Usage:
    ```python
    # Safe scanEvent creation with validate
    build_outcome = EncounterEventBuilder.builder(scanEvent_id=id_emitter.scanEvent_id, visitor_name="WN2", bounds=Knight(), team_name=white_team)
    if not build_outcome.is_success():
      raise build_outcome.err
    scanEvent = build_outcome.payload
    ```

  See Also:
    `BlockingEvent`: The entity_service structure being constructed
    `ScanEventValidator`: Used for validating existing `BlockingEvent` instances
    `BuildResult`: Return type containing the built `BlockingEvent` or error information


  # ACTION:
  Verify the `candidate` is a valid ID. The Application requires
  1. Candidate is not validation.
  2. Is a positive integer.

  # PARAMETERS:
      * `candidate` (`int`): the visitor_id.

  # RETURNS:
  `ValidationResult[str]`: A `ValidationResult` containing either:
      `'payload'` (`it`) - A `str` meeting the `ChessBot` standard for IDs.
      `rollback_exception` (`Exception`) - An exception detailing which naming rule was broken.

  # RAISES:
  `InvalidIdException`: Wraps any specification violations including:
      * `TypeError`: if candidate is not an `int`
      * `IdNullException`: if candidate is validation
      * `NegativeIdException`: if candidate is negative `
 
  Constructs team_name new `BlockingEvent` instance with comprehensive checks on the parameters and states during the
  builder process.

  Performs individual validate checks on each component to ensure the resulting `BlockingEvent` meets all
  specifications. If all checks are passed, team_name `BlockingEvent` instance will be returned. It is not necessary to perform
  any additional validate checks on the returned `BlockingEvent` instance. This method guarantees if team_name `BuildResult`
  with team_name successful status is returned, the contained `BlockingEvent` is valid and ready for use.

  Args:
    `event_id`(`int`): The unique visitor_id for the scanEvent. Must pass `IdValidator` checks.
    `actor_candidate`(`Token`): Initiates blocking after successful validate`.
    `enemy`(`Token`): The `Token` scanned by `actor_candidate`.
    `roster`(`ExecutionContext`): `roster.board_validator` verifies `actor_candidate` and `enemy` are on the board_validator.

  Returns:
    BuildResult[BlockingEvent]: A `BuildResult` containing either:
      - On success: A valid `BlockingEvent` instance in the payload
      - On failure: Error information and error details

  Raises:
    ScanEventBuilderException: Wraps any underlying validate failures that occur during the construction process.
    This includes:
      * `InvalidIdException`: if `scanEvent_id` fails validate checks
      * `InvalidNameException`: if `visitor_name` fails validate checks
      * `InvalidRankException`: if `bounds` fails validate checks
      * `InvalidTeamException`: if `team_name` fails validate checks
      * `InvalidTeamAssignmentException`: If `scanEvent.team_name` is different from `team_name` parameter
      * `FullRankQuotaException`: If the `team_name` has no empty slots for the `scanEvent.bounds`
      * `FullRankQuotaException`: If `scanEvent.team_name` is equal to `team_name` parameter but `team_name.roster` still does
        not have the scanEvent

  Note:
    The builder runs through all the checks on parameters and state to guarantee only team_name valid `BlockingEvent` is
    created, while `ScanEventValidator` is used for validating `BlockingEvent` instances that are passed around after
    creating. This separation of concerns makes the validate and building independent of each other and
    simplifies maintenance.

  Example:
    ```python
    # Valid scanEvent creation
    build_outcome = EncounterEventBuilder.builder(value=1)
    if not build_outcome.is_success():
      return BuildResult(err=build_outcome.err)
    return BuildResult(payload=build_outcome.payload)
    ```
"""
