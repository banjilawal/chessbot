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
from abc import ABC, abstractmethod
from enum import auto

from chess.system import Event, ExecutionContext, TransactionResult


class TransactionState:
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
  RUNNING = auto()
  SUCCESS = auto()
  FAILURE = auto()
  TIMED_OUT = auto()
  ROLLED_BACK = auto()


class Transaction(ABC):
  """Base class for transaction execution handlers"""
  _event: Event
  _state: TransactionState
  _context: ExecutionContext


  def __init__(self, event: Event, context: ExecutionContext):
    self._event = event
    self._context = context
    self._state = TransactionState.RUNNING



  @property
  def event(self) -> Event:
    return self._event

  @property
  def context(self) -> ExecutionContext:
    return self._context

  @property
  def state(self) -> TransactionState:
    return self._state


  @abstractmethod
  def execute(self) -> TransactionResult:
    pass
