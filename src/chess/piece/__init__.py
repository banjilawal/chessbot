# chess/piece/__init__.py

"""
## Purpose
Provides the fundamental data structures for game pieces and entities owned by a game piece.

## Core Classes
* `Piece`: Abstract base class for all chess pieces
* `CombatantPiece`: Concrete piece that can be captured
* `KingPiece`: Concrete king piece with special rules
* `CoordStack`: Coordinate history and management utility. `Piece` owns `CoordStack`.
* `Encounter`: A record of an item discovered by a `Piece` during a scan or move.
* `EncounterScan`: A data-holding object representing a single scan of a chess piece's surroundings.

## Usage
```python
from chess.rank import Pawn, King
from chess.piece import CombatantPiece, KingPiece

white_pawn_9 = CombatantPiece(piece_id=9, name='WP1', rank=Pawn(), team=white_team)
white_king = KingPiece(piece_id=2, name='WK', rank=King(), team=white_team)
```

## EXCEPTIONS
These are not all the exceptions related to `Piece` in the application. `chess.piece` package only has exceptions
organic to:
* `Piece` and its subclases.
* `CoordStack`.
* `Encounter` and `EncounterScan`

All exceptions in `chess.piece` package have static fields:
- `ERROR_CODE`: Useful when parsing logs for an exception. Error codes are in caps with a "_ERROR" suffix
- `DFAULT_MESSAGE`: A sentence describing the exception. Use an exception's `DEFAULT_MESSAGE` for consistency
    across the application.

### Piece Exceptions
- `PieceException`: Super class of exceptions raised by `Piece`. Use more granular exceptions
    that provide more specific information.
- `NullPieceException`: The parent is `NullException`. `NullPieceException` is the parent of
    all exceptions related to null pieces. Use more granular null exceptions that provide
    more specific information about the subclass instance that is null.
- `NullKingPieceException`: Raised when a `kingPiece` reference is null
- `NullCombatantPieceException`: Raised when a `CombatantPiece` is null.
- `DoublePromotionException`: Raised if there is an attempt to promote a king or pawn that has alreay
    been promoted.

### Piece Validation Execeptions
- `PieceValidationException`: Raised if an existing `Piece` object fails validation checks.
- `NullPieceValidatorException`: Raised if a null `PieceValidator` is passed as a parameter.

### Piece Building Exceptions
- `PieceBuilderException`: Raised if there is an error during when a `PieceBuilder` is creating a
    new `Piece` instance.
- `NullPieceBuilderException`: Raised if there is null `PieceBuilder` is pased as a parameter.

### Encounter Exceptions
- `EncounterException`: Super class of exceptions raised by `Encounter`. Use more granular exceptions
    that provide more specific information.
- `NullEncounterException`: The parent is `NullValueException`. `NullEncounterException` is the parent of
    all exceptions related to null encounters. Use more granular null exceptions that provide
    more specific information about the subclass instance that is null.
- `EncounterValidationException`: Raised if an existing `Encounter` object fails validation checks.
- `NullEncounterValidatorException`: Raised if a null `EncounterValidator` is passed as a parameter.
- `EncounterBuilderException`: Raised if there is an error during when `EncounterBuilder` is creating
    a new `Encounter` instance.
- `NullEncounterBuilderException`: Raised if there is null `EncounterBuilder` is passed as a parameter.
- `AutoeEncounterException`: Raised if a `Piece` object tries to create an encouter record about itself.

### CoordStack Exceptions
- `CoordStackException`: Super class of exceptions raised by `CoordStack`.
- `CoordStackValidationException`: Raised if an existing `CoordStack` object fails validation.`
- `NullCoordStackException`: Raised if a null `CoordStackException` is passed as a parameter.


null or improperly referenced during chess operations.
AlreadyAtDestinationException: Move to current position

PrisonerEscapeException: Captured piece tries to move
PrisonerReleaseException: Error releasing prisoner
PieceCoordNullException: Piece coordinate is null
SetCaptorNullException: Setting null captor

### PIECE EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `Piece` exceptions.

```python
from chess.piece import NullPieceException, AutoEncounterException

build_outcome = PieceBuilder.build(
    piece_id=id_emitter.piece_id,
    name='BB2',
    rank=Bishop(),
    team=black_team
)

if not build_outcome.is_success():
    raise build_outcome.exception

# Its best practice to cast the result to the expected type.
black_bishop_2 = cast(CombatantPiece, build_outcome.payload)

if black_bishop_2 is None:
    raise NullPieceException(f'{NullPieceException.DEFAULT_MESSAGE}')

def create_encounter(observer: Piece, discovery: Piece) -> Encounter:
    method = "create_encounter"
    if observer == discovery:
        raise AutoEncounterException(f"{method}: {AutoEncounterException.DEFAULT_MESSAGE}")
    return Encounter(discovery=discovery)
```

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""

from .exception import *

from .piece import *
from .encounter import Encounter
from .piece_builder import PieceBuilder
from .piece_validator import PieceValidator
from .encounter_scan import EncounterScan
from .coord_stack_validator import CoordStackValidator
from .coord_stack_builder import CoordinateStackBuilder

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'piece'


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Piece',
    'KingPiece',
    'CombatantPiece',
    'PieceBuilder',
    'PieceValidator',
    'Encounter',
    'EncounterScan',
    'PieceBuilder',

    *exception.__all__,

    # Subpackages
    'exception',

    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info'
]

# Organic utility function for package info
def package_info() -> dict:
    """Return basic package information."""
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }


# chess/piece/__init__.py


