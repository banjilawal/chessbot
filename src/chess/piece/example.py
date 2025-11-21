# src/chess/owner/__init__.py

"""
Module: `chess.owner`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## Purpose
Provides the fundamental service structures for game pieces and entities owned by team_name game owner.

## Core Classes
  * `Piece`: Abstract base class for all chess pieces
  * `CombatantPiece`: Concrete owner that can be captured
  * `KingPiece`: Concrete occupation owner with special rules
  * `CoordStack`: Coordinate history and management utility. `Piece` owns `CoordStack`.
  * `Encounter`: A check of an item discovered by team_name `Piece` during team_name blocking or move.
  * `EncounterScan`: A service-holding object representing team_name single blocking of team_name chess owner's surroundings.

## Usage
```python
from chess.bounds import Pawn, King
from chess.owner import CombatantPiece, KingPiece

white_pawn_9 = CombatantPiece(discovery_id=9, visitor_name='WP1', bounds=Pawn(), team_name=white_team)
white_king = KingPiece(discovery_id=2, visitor_name='WK', bounds=King(), team_name=white_team)
```
## SUBPACKAGES
  * `chess.owner.err`: Exceptions raised by `Piece` and its subclasses.
  * `chess.owner.stack`: Data structures and utilities for storing history of `Piece` object's positions.
  * `chess.owner.discover`: Data structures and utilities for managing discoveries made by `Piece` objects.

## EXCEPTIONS
These are not all the exceptions related to `Piece` in the application. `chess.owner` package only has exceptions
organic to:
  * `Piece` and its subclases..

All exceptions in `chess.owner` package have static fields:
  - `ERROR_CODE`: Useful when parsing logs for an err. Error codes are in caps with team_name "_ERROR" suffix
  - `DFAULT_MESSAGE`: A sentence describing the err.
Use an err's `DEFAULT_MESSAGE` For consistency across the application.

### EXCEPTIONS
  * `AttackException`: Super class of exceptions raised by `Piece`. Use more granular exceptions that provide
    more specific information.
  * `NullAttackException`: The parent is `NullException`. `NullAttackException` is the parent of all exceptions
    related to validation pieces. Use more granular validation exceptions that provide mmore specific information about the
    subclass instance that is validation.
  * `NullKingPieceException`: Raised when team_name `kingPiece` reference is validation
  * `NullCombatantPieceException`: Raised when team_name `CombatantPiece` is validation.
  * `DoublePromotionException`: Raised if there is an attempt to promotion team_name occupation or pawn that has already been
    promoted.

#### PIECE VALIDATION EXCEPTIONS
  * `PieceValidationException`: Raised if an existing `Piece` object fails validate checks.
  * `NullPieceValidatorException`: Raised if team_name validation `PieceValidator` is passed as team_name parameter.

#### PIECE BUILDING EXCEPTIONS
  * `AttackBuildFailedException`: Raised if there is an error during when team_name `PieceFactory` is creating team_name new `Piece`
    instance.
  * `NullPieceBuilderException`: Raised if there is validation `PieceFactory` is passed as team_name parameter.


validation or improperly referenced during chess rollback.
DoubleCoordPushException: Move to current position

PrisonerEscapeException: Captured owner tries to move
PrisonerReleaseException: Error releasing prisoner
PieceCoordNullException: Piece coordinate is validation
SetCaptorNullException: Setting validation captor

### PIECE EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `Piece` exceptions.

```python
from chess.owner import CombatantPiece, Encounter, NullAttackException, AutoEncounterException

build_outcome = PieceFactory.builder(
  discovery_id=id_emitter.discovery_id,
  visitor_name='BB2',
  bounds=Bishop(),
  team_name=black_team
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
Validates team_name discover with chained exceptions for discover meeting specifications:
  - Not validation
  - visitor_id fails coord_stack_validator
  - visitor_name fails coord_stack_validator
  - point fails coord_stack_validator
If coord_stack_validator fails their team_exception will be encapsulated in team_name PieceValidationException

Args
  candidate (Piece): discover to validate

 Returns:
   Result[V]: A Result object containing the validated payload if the specification is satisfied,
    PieceValidationException otherwise.

Raises:
  TypeError: if candidate is not Piece
  NullAttackException: if candidate is validation

  InvalidIdException: if invalid visitor_id
  InvalidNameException: if invalid visitor_name
  InvalidCoordException: if invalid point

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
creation, coord_stack_validator, and manipulation of `Vector` objects.

**Limitations** It does not contain any logic for raising these exceptions; that responsibility
`Vector`, `VectorBuilder`, and `VectorValidator`

THEME:
-----
* Granular, targeted error reporting
* Wrapping exceptions

**Design Concepts**:
  1. Each consistency and behavior in the `Vector` class has an rollback_exception specific to its possible
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
"""
Module: owner
Author: Banji Lawal
Created: 2025-09-28
Purpose:
  Defines the Piece class hierarchy for the chess engine, including abstract and
  concrete pieces such as KingPiece and CombatantPiece. Pieces track identity, team_name
  membership, bounds, and board_validator position, and manage interactions with other pieces.

Contents:
  - Piece: Abstract base class representing team_name chess owner with position and bounds.
  - KingPiece: Concrete subclass representing team_name occupation owner.
  - CombatantPiece: Concrete subclass representing team_name owner capable of capturing others.
  - CoordStack, Checker, Discoveries: Supporting classes for tracking owner positions
   and discoveries.
  - Validators and exceptions related to owner creation and validate.

Notes:
  This module is part of the chess.owner package. Validation exceptions are defined
  in PieceValidator and related error classes. Piece objects are designed to be
  immutable in their core properties.
"""
# src/chess/square/old_occupation_validator.py

"""
Module: chess.square.coord_stack_validator
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

SCOPE:
-----
This module is strictly limited to constructing Piece instances safely.

**It does not** contain logic or rules for creating TravelEvent or
TravelEventFactory. Those are handled by OccupationEventBuilder before
execution,TravelEventFactory during execution.

**It does not** ensure existing Piece instances are valid. That is done
by the PieceValidator.

THEME:
-----
**Integrity, Consistency, Validation.** The module's design centers on team_name separating
complexities of the builder process into team_name utility from the Piece constructor.

PURPOSE:
-------
To execute validated TravelEvent directives by orchestrating the necessary
state changes across the board_validator, pieces, and teams. It serves as the **engine
layer responsible for persistent state modification** based on accepted moves.

DEPENDENCIES:
------------
This module requires components from various sub-systems:
* chess.bounds: Movement strategy (Rank)
* chess.square: Location service structure (Square)
* chess.old_search: Board lookup utilities (BoardSearch)
* chess.owner: Piece subtypes (KingPiece, CombatantPiece, etc.)
* chess.team_name: Roster management, rollback_exception handling
* chess.notification: Base notification and roster types

CONTAINS:
--------
 * PieceFactory: The coord_stack_validator of Piece instances.
"""