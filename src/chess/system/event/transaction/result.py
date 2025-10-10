# src/chess/team/builder.py

"""
Module: chess.team.builder
Author: Banji Lawal
Created: 2025-10-08
version: 1.0.0

# SCOPE:
-------
***Limitation***: There is no guarantee properly created `Team` objects released by the module will satisfy
    client requirements. Clients are responsible for ensuring a `TeamBuilder` product will not fail when used.

**Related Features**:
    Authenticating existing teams -> See TeamValidator, module[chess.team.validator],
    Handling process and rolling back failures --> See `Transaction`, module[chess.system]

# THEME:
-------
* Data assurance, error prevention

**Design Concepts**:
    Separating object creation from object usage.
    Keeping constructors lightweight

# PURPOSE:
---------
1. Central, single producer of authenticated `Team` objects.
2. Putting all the steps and logging into one place makes modules using `Team` objects cleaner and easier to follow.

**Satisfies**: Reliability and performance contracts.

# DEPENDENCIES:
---------------
From `chess.system`:
    `BuildResult`, `Builder`, `LoggingLevelRouter`, `ChessException`, `NullException`, `BuildFailedException`
    `IdValidator`, `NameValidator`

From `chess.team`:
    `Team`, `NullTeam`, `TeamBuildFailedException`, `TeamSchema`

From `chess.commander`:
  `Commander`, `CommanderValidator`,

# CONTAINS:
----------
 * `TeamBuilder`
"""

class TeamBuilder(Builder[Team]):
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Team` instances.
  2. Create new `Team` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """


from typing import Optional

from chess.system import Result
from chess.transaction import Event

class TransactionResult:
  """
  # ROLE: Builder implementation

  # RESPONSIBILITIES:
  1. Process and validate parameters for creating `Team` instances.
  2. Create new `Team` objects if parameters meet specifications.
  2. Report errors and return `BuildResult` with error details.

  # PROVIDES:
  `BuildResult`: Return type containing the built `Team` or error information.

  # ATTRIBUTES:
  None
  """
  """
  Result of team transaction that changes an entity's state.

  Use factory methods to create instances:
  - TransactionResult.success()
  - TransactionResult.failed()
  - TransactionResult.rolled_back()

  Direct constructor usage is not recommended.
  """

  _event: Event
  _exception: Optional[Exception]
  _was_rolled_back: bool

  def __init__(
    self,
    event: Event,
    exception: Optional[Exception] = None,
    was_rolled_back: bool = False
  ):
    """INTERNAL: Use factory methods instead of direct constructor."""
    method = "TransactionResult.__init__"

    self._event = event
    self._exception = exception
    self._was_rolled_back = was_rolled_back


  @property
  def event(self) -> Optional[Event]:
    return self._event

  @property
  def exception(self) -> Optional[Exception]:
    return self._exception

  @property
  def was_rolled_back(self) -> bool:
    return self._was_rolled_back

  def is_success(self) -> bool:
    method = f"{self.__class__.__name__}.is_success"
    """True if transaction success condition was true after the state change"""

    return self._exception is None and not self._was_rolled_back

  #
  # def is_processing(self) -> bool:
  #   method = f"{self.__class__.__name__}.is_processing"
  #   """True if transaction still processing, has not changed state"""
  #
  #   return self._event is None and self._exception is None and not self._was_rolled_back
  #
  #
  # def is_failed(self) -> bool:
  #   method = f"{self.__class__.__name__}.is_failed"
  #   """True if raised an exception before the state changed"""
  #
  #   return not (self._exception is None and self._was_rolled_back)
  #
  #
  # @classmethod
  # def success(cls, outcome_id: int, request: Action, event: Event) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.success"
  #   """Create team successful outcome"""
  #
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=event,
  #     err=None,
  #     was_rolled_back=False
  #   )
  #
  #
  # @classmethod
  # def processing(cls, outcome_id: int, request: Action) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.processing"
  #
  #   """Create team processing outcome"""
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=None,
  #     err=None,
  #     was_rolled_back=False
  #   )
  #
  #
  # @classmethod
  # def failed(cls, outcome_id: int, request: Action, err: Exception) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.failed"
  #   """Create team failed outcome"""
  #
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=None,
  #     err=err,
  #     was_rolled_back=False
  #   )
  #
  #
  # @classmethod
  # def roll_back(cls, outcome_id: int, request: Action, event: Event) -> 'TransactionResult':
  #   method = f"{cls.__class__.__name__}.rolled_back"
  #   """Create team rolled back outcome"""
  #
  #   return cls(
  #     op_result_id=outcome_id,
  #     request=request,
  #     event=event,
  #     err=None,
  #     was_rolled_back=True
  #   )





