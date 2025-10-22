#   """
#   ROLE:
#   ----
#   RESPONSIBILITIES:
#   ----------------
#   PROVIDES:
#   --------
#   ATTRIBUTES:
#   ----------
# """
"""
Builder class responsible for safely constructing `Team` instances.

`TeamBuilder` ensures that `Team` objects are always created successfully by performing comprehensive validate
 checks during construction. This separates the responsibility of building from validating - `TeamBuilder`
 focuses on creating while `TeamValidator` is used for validating existing `Team` instances that are passed
 around the system.

The build runs through all validate checks individually to guarantee that any `Team` instance it produces
meets all required specifications before construction completes

Usage:
  ```python
  # Safe team creation with validate
  build_result = TeamBuilder.build(team_id=1, commander=black_commander, schema=TeamProfile.BLACK)

  if build_result.is_success():
    team = build_result.payload
  ```

See Also:
  `Team`: The data structure being constructed
  `TeamValidator`: Used for validating existing `Team` instances
  `BuildResult`: Return type containing the built `Team` or error information
"""

#   """
# Action:
# Parameters:
#     * `param` (`DataType`):
# Returns:
#     `DataType` or `Void`
# Raises:
# MethodNameException wraps
#     *
# """
"""
Constructs team new `Team` instance with comprehensive checks on the parameters and states during the
build process.

Performs individual validate checks on each component to ensure the resulting `Team` meets all specifications.
If all checks are passed, team `Team` instance will be returned. It is not necessary to perform any additional
validate checks on the returned `Team` instance. This method guarantees if team `BuildResult` with team successful
status is returned, the contained `Team` is valid and ready for use.

Args:
  `team_id`(`int`): The unique id for the team. Must pass `IdValidator` checks.
  `commander`(`Commander`): The human or cybernetic moving pieces in `Team.roster`. The commander must pass
    `CommanderValidator` checks.must pass `CommanderValidator` checks.
  `schema`(`TeamProfile`): The schema defining team attributes and behaviors. Must not be None and be
    an instance of `TeamProfile`.

Returns:
  BuildResult[Team]: A `BuildResult` containing either:
    - On success: A valid `Team` instance in the payload
    - On failure: Error information and error details

Raises:
  `TeamBuildFailedException`: Wraps any underlying validate failures that occur during the construction process.
  This includes:
    * `InvalidIdException`: if `id` fails validate checks`
    * `InvalidCommanderException`: if `commander` fails validate checks
    * `NullTeamProfileException`: if `schema` is None
    * `TypeError`: if `schema` is not team `TeamProfile` instance
    * `RelationshipException`: if the bidirectional relationship between `Team` and `Commander` is broken

Note:
  The build runs through all the checks on parameters and state to guarantee only team valid `Team` is
  created, while `TeamValidator` is used for validating `Team` instances that are passed around after
  creation. This separation of concerns makes the validate and building independent of each other and
  simplifies maintenance.

Example:
  ```python
  # Valid team creation
  notification = TeamBuilder.build(team_id=1, commander=black-commander, schema=black_team_profile)
  if notification.is_success():
    team = cast(Team, notification.payload) # Guaranteed valid Team

  # Null commander will fail gracefully
  notification = TeamBuilder.build(team_id=1, commander=None, schema=black_team_profile)
  if not notification.is_success():
    # Handle construction failure
    pass
  ```
"""

"""
Validates existing `Team` instances that are passed around the system.

While `TeamBuilder` ensures valid Teams are created, `TeamValidator`
checks `Team` instances that already exist - whether they came from
deserialization, external sources, or need re-validate after modifications.

Usage:
  ```python
  # Validate an existing team
  team_validation = TeamValidator.validate(candidate)  
  if not team_validation.is_success():
    raise team_validation.err
  team = cast(Team, team_validation.payload)
  ```

Use `TeamBuilder` for construction, `TeamValidator` for verification.
"""