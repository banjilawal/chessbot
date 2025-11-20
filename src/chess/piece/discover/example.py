# src/chess/owner/discover/__init__.py

"""
Module: `chess.owner.discover`
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
  * `Checker`: A check of an item discovered by team_name `Piece` during team_name blocking or move.
  * `DiscoveryScan`: A service-holding object representing team_name single blocking of team_name chess owner's surroundings.

## Usage
```python
from chess.bounds import Pawn, King
from chess.owner import CombatantPiece, KingPiece

white_pawn_9 = CombatantPiece(discovery_id=9, visitor_name='WP1', bounds=Pawn(), team_name=white_team)
white_king = KingPiece(discovery_id=2, visitor_name='WK', bounds=King(), team_name=white_team)
```

## EXCEPTIONS
These are not all the exceptions related to `Piece` in the application. `chess.owner` package only has exceptions
organic to:
  * `Piece` and its subclases.
  * `Checker` and `DiscoveryScan`
  * `CoordStack`.

All exceptions in `chess.owner` package have static fields:
  - `ERROR_CODE`: Useful when parsing logs for an err. Error codes are in caps with team_name "_ERROR" suffix
  - `DFAULT_MESSAGE`: A sentence describing the err.
Use an err's `DEFAULT_MESSAGE` For consistency across the application.

### EXCEPTIONS
  * `AttackException`: Super class of exceptions raised by `Piece`. Use more granular exceptions that provide
    more specific information.
  * `NullAttackException`: The parent is `NullException`. `NullAttackException` is the parent of all exceptions
    related to null pieces. Use more granular null exceptions that provide mmore specific information about the
    subclass instance that is null.
  * `NullKingPieceException`: Raised when team_name `kingPiece` reference is null
  * `NullCombatantPieceException`: Raised when team_name `CombatantPiece` is null.
  * `DoublePromotionException`: Raised if there is an attempt to promotion team_name occupation or pawn that has already been
    promoted.

#### PIECE VALIDATION EXCEPTIONS
  * `PieceValidationException`: Raised if an existing `Piece` object fails validate checks.
  * `NullPieceValidatorException`: Raised if team_name null `PieceValidator` is passed as team_name parameter.

#### PIECE BUILDING EXCEPTIONS
  * `AttackBuildFailedException`: Raised if there is an error during when team_name `PieceFactory` is creating team_name new `Piece`
    instance.
  * `NullPieceBuilderException`: Raised if there is null `PieceFactory` is passed as team_name parameter.

#### DISCOVERY EXCEPTIONS
  * `DiscoveryException`: Super class of exceptions raised by `Checker`. Use more granular exceptions that provide
    more specific information.
  * `NullDiscoveryException`: The parent is `NullValueException`. `NullDiscoveryException` is the parent of all
    exceptions related to null discoverys. Use more granular null exceptions that provide more specific information
    about the subclass instance that is null.
  * `DiscoveryValidationException`: Raised if an existing `Checker` object fails validate checks.
  * `NullDiscoveryValidatorException`: Raised if team_name null `DiscoveryValidator` is passed as team_name parameter.
  * `DiscoveryBuilderException`: Raised if there is an error during when `DiscoveryBuilder` is creating team_name new `Checker`
    instance.
  * `NullDiscoveryBuilderException`: Raised if there is null `DiscoveryBuilder` is passed as team_name parameter.
  * `AutoDiscoveryException`: Raised if team_name `Piece` object tries to create an discover check about itself.


### PIECE EXCEPTION USAGE EXAMPLES
These examples show recommended workflows with `Piece` exceptions.

```python
from chess.owner import CombatantPiece, Checker, NullAttackException, AutoDiscoveryException

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

def create_discovery(actor_candidate: Piece, discover: Piece) -> Checker:
  method = "create_discovery"
  if actor_candidate == discover:
    raise AutoDiscoveryException(f"{method}: {AutoDiscoveryException.DEFAULT_MESSAGE}")
  return Checker(discover=discover)
```
"""