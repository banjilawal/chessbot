from typing import cast
from enum import Enum

from assurance import ThrowHelper
from chess.system import BuildResult
from chess.piece import Piece, Discovery, PieceValidator, AutoDiscoveryException, DiscoveryBuilderException, \
  AddDuplicateDiscoveryException
from chess.piece.discover import CircularDiscoveryException


class DiscoveryBuilder(Enum):
  """
  Builder class responsible for safely constructing `Checker` instances.

  `DiscoveryBuilder` ensures that `Checker` objects are always created successfully by performing comprehensive validate
  checks during construction. This separates the responsibility of building from validating - `DiscoveryBuilder`
  focuses on creating while `DiscoveryValidator` is used for validating existing `Checker` instances that are passed
  around the system.

  The builder runs through all validate checks individually to guarantee that any `Checker` instance it produces
  meets all required specifications before construction completes
  
  Usage:
    ```python
    # Safe discover creation with validate
    build_outcome = DiscoveryBuilder.builder(actor_candidate=bishop, discover=pawn))
    if not build_outcome.is_success():
      raise build_outcome.err
    discover = build_outcome.payload
    ```
  
  See Also:
    `Checker`: The service structure being constructed
    `DiscoveryValidator`: Used for validating existing `Checker` instances
    `BuildResult`: Return type containing the built `Checker` or error information
  """

  @staticmethod
  def build(observer: Piece, subject: Piece) -> BuildResult[Discovery]:
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
    """
    Constructs team_name new `Checker` instance with comprehensive checks on the parameters and states during the
    builder process.

    Performs individual validate checks on each component to ensure the resulting `Checker` meets all
    specifications. If all checks are passed, team_name `Checker` instance will be returned. It is not necessary to perform
    any additional validate checks on the returned `Checker` instance. This method guarantees if team_name `BuildResult`
    with team_name successful status is returned, the contained `Checker` is valid and ready for use.


    Args:
      `actor_candidate`(`Piece`): The owner that is doing team_name blocking, or executing team_name move.
      `discover`(`Piece`): The static owner the `actor_candidate` finds in team_name `square`.

    Returns:
      BuildResult[Checker]: A `BuildResult` containing either:
        - On success: A valid `Checker` instance in the payload
        - On failure: Error information and error details

    Raises:
      `DiscoveryBuilderException`: Wraps any underlying validate failures that occur during the construction
      process. This includes:
        * `PieceValidationException`: if `actor_candidate` or `discover` fails validate checks
        * `AutoDiscoveryException`: if `actor_candidate` and `discover` are the same.

    Note:
      The builder runs through all the checks on parameters and state to guarantee only team_name valid `Checker` is
      created, while `DiscoveryValidator` is used for validating `Checker` instances that are passed around after 
      creation. This separation of concerns makes the validate and building independent of each other and
      simplifies maintenance.

    Example:
      ```python
      # Valid discover creation
      build_outcome = DiscoveryBuilder.builder(value=1)
      if not build_outcome.is_success():
        return BuildResult(err=build_outcome.err)
      return BuildResult(payload=build_outcome.payload)
      ```
    """
    method = "DiscoveryBuilder.builder"

    try:
      observer_validation = PieceValidator.validate(observer)
      if not observer_validation.is_success():
        ThrowHelper.log_and_raise_error(DiscoveryBuilder, observer_validation)
        
      subject_validation = PieceValidator.validate(subject)
      if not subject_validation.is_success():
        ThrowHelper.log_and_raise_error(DiscoveryBuilder, subject_validation)
        
      if observer == subject:
        ThrowHelper.log_and_raise_error(
          DiscoveryBuilder,
          CircularDiscoveryException(CircularDiscoveryException.DEFAULT_MESSAGE)
        )

      search_result = observer.discoveries.find_by_id(subject.id)
      if not search_result.is_empty():
        ThrowHelper.log_and_raise_error(
          DiscoveryBuilder,
          AddDuplicateDiscoveryException(AddDuplicateDiscoveryException.DEFAULT_MESSAGE)
        )
      return BuildResult(payload=Discovery(piece=cast(Piece, subject)))

    except Exception as e:
      raise DiscoveryBuilderException(
        f"{method}: {DiscoveryBuilderException.DEFAULT_MESSAGE}"
      )