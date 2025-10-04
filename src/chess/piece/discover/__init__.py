# chess/piece/discover/__init__.py

"""
Module: `chess.piece.discover`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0


## Purpose
Provides the fundamental data structures for game pieces and entities owned by a game piece.

## Core Classes
    * `Piece`: Abstract base class for all chess pieces
    * `CombatantPiece`: Concrete piece that can be captured
    * `KingPiece`: Concrete king piece with special rules
    * `CoordStack`: Coordinate history and management utility. `Piece` owns `CoordStack`.
    * `Discovery`: A record of an item discovered by a `Piece` during a scan or move.
    * `DiscoveryScan`: A data-holding object representing a single scan of a chess piece's surroundings.

## Usage
```python
from chess.rank import Pawn, King
from chess.piece import CombatantPiece, KingPiece

white_pawn_9 = CombatantPiece(discovery_id=9, name='WP1', rank=Pawn(), team=white_team)
white_king = KingPiece(discovery_id=2, name='WK', rank=King(), team=white_team)
```

## EXCEPTIONS
These are not all the exceptions related to `Piece` in the application. `chess.piece` package only has exceptions
organic to:
    * `Piece` and its subclases.
    * `Discovery` and `DiscoveryScan`
    * `CoordStack`.

All exceptions in `chess.piece` package have static fields:
    - `ERROR_CODE`: Useful when parsing logs for an err. Error codes are in caps with a "_ERROR" suffix
    - `DFAULT_MESSAGE`: A sentence describing the err.
Use an err's `DEFAULT_MESSAGE` For consistency across the application.

### EXCEPTIONS
    * `PieceException`: Super class of exceptions raised by `Piece`. Use more granular exceptions that provide
        more specific information.
    * `NullPieceException`: The parent is `NullException`. `NullPieceException` is the parent of all exceptions
        related to null pieces. Use more granular null exceptions that provide mmore specific information about the
        subclass instance that is null.
    * `NullKingPieceException`: Raised when a `kingPiece` reference is null
    * `NullCombatantPieceException`: Raised when a `CombatantPiece` is null.
    * `DoublePromotionException`: Raised if there is an attempt to promote a king or pawn that has already been
        promoted.

#### PIECE VALIDATION EXCEPTIONS
    * `PieceValidationException`: Raised if an existing `Piece` object fails validate checks.
    * `NullPieceValidatorException`: Raised if a null `PieceValidator` is passed as a parameter.

#### PIECE BUILDING EXCEPTIONS
    * `PieceBuilderException`: Raised if there is an err during when a `PieceBuilder` is creating a new `Piece`
        instance.
    * `NullPieceBuilderException`: Raised if there is null `PieceBuilder` is passed as a parameter.

#### DISCOVERY EXCEPTIONS
    * `DiscoveryException`: Super class of exceptions raised by `Discovery`. Use more granular exceptions that provide
        more specific information.
    * `NullDiscoveryException`: The parent is `NullValueException`. `NullDiscoveryException` is the parent of all
        exceptions related to null discoverys. Use more granular null exceptions that provide more specific information
        about the subclass instance that is null.
    * `DiscoveryValidationException`: Raised if an existing `Discovery` object fails validate checks.
    * `NullDiscoveryValidatorException`: Raised if a null `DiscoveryValidator` is passed as a parameter.
    * `DiscoveryBuilderException`: Raised if there is an err during when `DiscoveryBuilder` is creating a new `Discovery`
        instance.
    * `NullDiscoveryBuilderException`: Raised if there is null `DiscoveryBuilder` is passed as a parameter.
    * `AutoDiscoveryException`: Raised if a `Piece` object tries to create an discover record about itself.


### PIECE EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `Piece` exceptions.

```python
from chess.piece import CombatantPiece, Discovery, NullPieceException, AutoDiscoveryException

build_outcome = PieceBuilder.build(
    discovery_id=id_emitter.discovery_id,
    name='BB2',
    rank=Bishop(),
    team=black_team
)

if not build_outcome.is_success():
    raise build_outcome.err

# Its best practice to cast the result to the expected type.
black_bishop_2 = cast(CombatantPiece, build_outcome.payload)

if black_bishop_2 is None:
    raise NullPieceException(f'{NullPieceException.DEFAULT_MESSAGE}')

def create_discovery(actor: Piece, discover: Piece) -> Discovery:
    method = "create_discovery"
    if actor == discover:
        raise AutoDiscoveryException(f"{method}: {AutoDiscoveryException.DEFAULT_MESSAGE}")
    return Discovery(discover=discover)
```
"""

from .exception import *

from .discovery import Discovery
from .discoveries import Discoveries
from .builder import DiscoveryBuilder

# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.piece.discover'


# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Discovery',
    'Discoveries',
    'DiscoveryBuilder',

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


