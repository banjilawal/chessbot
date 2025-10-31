# chess/piece/__init__.py

"""
Module: `chess.piece`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## Purpose
Provides the fundamental service structures for game pieces and entities owned by team game piece.

## Core Classes
  * `Piece`: Abstract base class for all chess pieces
  * `CombatantPiece`: Concrete piece that can be captured
  * `KingPiece`: Concrete occupation piece with special rules
  * `CoordStack`: Coordinate history and management utility. `Piece` owns `CoordStack`.
  * `Encounter`: A check of an item discovered by team `Piece` during team blocking or move.
  * `EncounterScan`: A service-holding object representing team single blocking of team chess piece's surroundings.

## Usage
```python
from chess.rank import Pawn, King
from chess.piece import CombatantPiece, KingPiece

white_pawn_9 = CombatantPiece(discovery_id=9, name='WP1', rank=Pawn(), team=white_team)
white_king = KingPiece(discovery_id=2, name='WK', rank=King(), team=white_team)
```
## SUBPACKAGES
  * `chess.piece.err`: Exceptions raised by `Piece` and its subclasses.
  * `chess.piece.coord_stack`: Data structures and utilities for storing history of `Piece` object's positions.
  * `chess.piece.discover`: Data structures and utilities for managing discoveries made by `Piece` objects.

## EXCEPTIONS
These are not all the exceptions related to `Piece` in the application. `chess.piece` package only has exceptions
organic to:
  * `Piece` and its subclases..

All exceptions in `chess.piece` package have static fields:
  - `ERROR_CODE`: Useful when parsing logs for an err. Error codes are in caps with team "_ERROR" suffix
  - `DFAULT_MESSAGE`: A sentence describing the err.
Use an err's `DEFAULT_MESSAGE` For consistency across the application.

### EXCEPTIONS
  * `AttackException`: Super class of exceptions raised by `Piece`. Use more granular exceptions that provide
    more specific information.
  * `NullAttackException`: The parent is `NullException`. `NullAttackException` is the parent of all exceptions
    related to null pieces. Use more granular null exceptions that provide mmore specific information about the
    subclass instance that is null.
  * `NullKingPieceException`: Raised when team `kingPiece` reference is null
  * `NullCombatantPieceException`: Raised when team `CombatantPiece` is null.
  * `DoublePromotionException`: Raised if there is an attempt to promotion team occupation or pawn that has already been
    promoted.

#### PIECE VALIDATION EXCEPTIONS
  * `PieceValidationException`: Raised if an existing `Piece` object fails validate checks.
  * `NullPieceValidatorException`: Raised if team null `PieceValidator` is passed as team parameter.

#### PIECE BUILDING EXCEPTIONS
  * `AttackBuildFailedException`: Raised if there is an error during when team `PieceBuilder` is creating team new `Piece`
    instance.
  * `NullPieceBuilderException`: Raised if there is null `PieceBuilder` is passed as team parameter.


null or improperly referenced during chess operations.
DoubleCoordPushException: Move to current position

PrisonerEscapeException: Captured piece tries to move
PrisonerReleaseException: Error releasing prisoner
PieceCoordNullException: Piece coordinate is null
SetCaptorNullException: Setting null captor

### PIECE EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `Piece` exceptions.

```python
from chess.piece import CombatantPiece, Encounter, NullAttackException, AutoEncounterException

build_outcome = PieceBuilder.build(
  discovery_id=id_emitter.discovery_id,
  name='BB2',
  rank=Bishop(),
  team=black_team
)

if not build_outcome.is_success():
  raise build_outcome.err

# Its best practice to cast the notification to the expected type.
black_bishop_2 = cast(CombatantPiece, build_outcome.payload)

if black_bishop_2 is None:
  raise NullAttackException(f'{NullAttackException.DEFAULT_MESSAGE}')

def create_encounter(actor_candidate: Piece, discover: Piece) -> Encounter:
  method = "create_encounter"
  if actor_candidate == discover:
    raise AutoEncounterException(f"{method}: {AutoEncounterException.DEFAULT_MESSAGE}")
  return Encounter(discover=discover)
```
"""

"""
Validates team discover with chained exceptions for discover meeting specifications:
  - Not null
  - id fails validator
  - name fails validator
  - coord fails validator
If validator fails their team_exception will be encapsulated in team PieceValidationException

Args
  candidate (Piece): discover to validate

 Returns:
   Result[T]: A Result object containing the validated payload if the specification is satisfied,
    PieceValidationException otherwise.

Raises:
  TypeError: if candidate is not Piece
  NullAttackException: if candidate is null

  InvalidIdException: if invalid id
  InvalidNameException: if invalid name
  InvalidCoordException: if invalid coord

  PieceValidationException: Wraps any preceding exceptions
"""
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
creation, validator, and manipulation of `Vector` objects.

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
1. Centralized error dictionary for the `Vector` graph.
2. Fast debugging using highly granular rollback_exception messages and naming to
    find the source.
3. Providing understandable, consistent information about failures originating from
    the `Vector` graph.
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