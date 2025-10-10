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


class State(Enum):
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
  TIMED_OUT = auto()
  ROLLED_BACK = auto()
  SUCCESS = auto()

class Transaction(ABC, Generic[T]):
  """Base class for transaction execution handlers"""

  @classmethod
  @abstractmethod
  def execute(cls, event: T, context: ExecutionContext) -> TransactionResult:
    pass
