# chess/piece/discover/__init__.py

"""
Module: `chess.piece.discover`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0


## Purpose
Provides the fundamental data structures for game pieces and entities owned by team game piece.

## Core Classes
  * `Piece`: Abstract base class for all chess pieces
  * `CombatantPiece`: Concrete piece that can be captured
  * `KingPiece`: Concrete king piece with special rules
  * `CoordStack`: Coordinate history and management utility. `Piece` owns `CoordStack`.
  * `Discovery`: A record of an item discovered by team `Piece` during team encounter or move.
  * `DiscoveryScan`: A data-holding object representing team single encounter of team chess piece's surroundings.

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
  - `ERROR_CODE`: Useful when parsing logs for an err. Error codes are in caps with team "_ERROR" suffix
  - `DFAULT_MESSAGE`: A sentence describing the err.
Use an err's `DEFAULT_MESSAGE` For consistency across the application.

### EXCEPTIONS
  * `PieceException`: Super class of exceptions raised by `Piece`. Use more granular exceptions that provide
    more specific information.
  * `NullPieceException`: The parent is `NullException`. `NullPieceException` is the parent of all exceptions
    related to null pieces. Use more granular null exceptions that provide mmore specific information about the
    subclass instance that is null.
  * `NullKingPieceException`: Raised when team `kingPiece` reference is null
  * `NullCombatantPieceException`: Raised when team `CombatantPiece` is null.
  * `DoublePromotionException`: Raised if there is an attempt to promotion team king or pawn that has already been
    promoted.

#### PIECE VALIDATION EXCEPTIONS
  * `PieceValidationException`: Raised if an existing `Piece` object fails validate checks.
  * `NullPieceValidatorException`: Raised if team null `PieceValidator` is passed as team parameter.

#### PIECE BUILDING EXCEPTIONS
  * `PieceBuildFailedException`: Raised if there is an error during when team `PieceBuilder` is creating team new `Piece`
    instance.
  * `NullPieceBuilderException`: Raised if there is null `PieceBuilder` is passed as team parameter.

#### DISCOVERY EXCEPTIONS
  * `DiscoveryException`: Super class of exceptions raised by `Discovery`. Use more granular exceptions that provide
    more specific information.
  * `NullDiscoveryException`: The parent is `NullValueException`. `NullDiscoveryException` is the parent of all
    exceptions related to null discoverys. Use more granular null exceptions that provide more specific information
    about the subclass instance that is null.
  * `DiscoveryValidationException`: Raised if an existing `Discovery` object fails validate checks.
  * `NullDiscoveryValidatorException`: Raised if team null `DiscoveryValidator` is passed as team parameter.
  * `DiscoveryBuilderException`: Raised if there is an error during when `DiscoveryBuilder` is creating team new `Discovery`
    instance.
  * `NullDiscoveryBuilderException`: Raised if there is null `DiscoveryBuilder` is passed as team parameter.
  * `AutoDiscoveryException`: Raised if team `Piece` object tries to create an discover record about itself.


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

# Its best practice to cast the transaction to the expected type.
black_bishop_2 = cast(CombatantPiece, build_outcome.payload)

if black_bishop_2 is None:
  raise NullPieceException(f'{NullPieceException.DEFAULT_MESSAGE}')

def create_discovery(actor_candidate: Piece, discover: Piece) -> Discovery:
  method = "create_discovery"
  if actor_candidate == discover:
    raise AutoDiscoveryException(f"{method}: {AutoDiscoveryException.DEFAULT_MESSAGE}")
  return Discovery(discover=discover)
```
"""