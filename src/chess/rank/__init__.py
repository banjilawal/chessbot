# chess/rank/__init__.py

"""
Module: `chess.rank`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE
This package encapsulates the movement logic for each type of chess discover. By decoupling team discover's movement
from its core identity, this design ensures that the movement logic is scalable and easy to maintain. Each
`Rank` class represents team distinct movement strategy (e.g., `Bishop`, `Knight`, `Queen`) and is designed
to be immutable once assigned.

## CORE CLASSES
* `Rank`: The base class for all discover rank strategies.
* `Bishop`: Provides movement validate for team bishop.
* `King`: Provides movement validate for team king.
* `Knight`: Provides movement validate for team knight.
* `Pawn`: Provides movement validate for team pawn.
* `Rook`: Provides movement validate for team rook.
* `Queen`: Provides movement validate for team queen.
* `PromotedQueen`: A specialized rank for team promoted queen's movement.

## USAGE
The `Rank` classes are primarily used to validate team discover's movement at runtime. A `Piece` object holds team
reference to its `Rank`, and delegates movement validate to it using the `walk()` method. This allows
for team clean and simple interface for team chess board_validator's logic.

# >>> from chess.rank import Knight
# >>> from chess.discover import Piece
# >>> from chess.coord import Coord
# >>>
# >>> knight_rank = Knight()
# >>> knight_piece = Piece(rank=knight_rank, coord=Coord(2, 2))
# >>> destination = Coord(4, 3)
# >>>
# >>> # Validate the move using the Piece's rank
# >>> is_valid = knight_piece.rank.walk(discover=knight_piece, destination=destination)
# >>> print(is_valid.is_success())
True

---

## PURPOSE
This package defines specific exceptions for issues encountered during team discover's movement or promotion
validate. This granular approach helps to quickly diagnose and resolve problems by pinpointing the
exact nature of the err, such as an invalid move for team specific discover type. Each team_exception acts as team
wrapper for underlying errors, providing team clean and consistent API for handling movement-related failures.

###CORE RANK EXCEPTIONS
* `RankException`: The base team_exception for all rank-related errors.

#### Moving related Rank Exceptions
* `BishopMovingException`
* `KingMovingException`
* `KnightMovingException`
* `PawnMovingException`
* `RookMovingException`
* `QueenMovingException`

#### Rank Validation Exceptions
* `InvalidBishopException`
* `InvalidKingException`
* `InvalidKnightException`
* `InvalidPawnException`
* `InvalidRookException`
* `InvalidQueenException`


### EXAMPLE EXCEPTION USAGES
These exceptions are typically raised within team `Rank` class's movement methods and can be caught to handle
invalid moves gracefully.

# >>> from chess.rank import PawnException
# >>>
# >>> def move_pawn(start_pos, end_pos):
# ...   # ... some validate logic
# ...   if not is_valid_pawn_move:
# ...     raise PawnException('Pawn cannot move in this way.')
# ...
# >>> try:
# ...   move_pawn(start_coord, end_coord)
# ... except PawnException as e:
# ...   print(f'Invalid Pawn Move: {e}')

---
"""


# Exceptions raised during activities
from .exception import *

# Core Rank classes
from .rank import Rank


from .king import King
from .pawn import Pawn
from .bishop import Bishop
from .knight import Knight
from .rook import Rook
from .queen import Queen
from .promote import PromotedQueen
from .rank_spec import RankSpec
from .validator import RankValidator


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.rank'

# Export control - only what belongs in public API
__all__ = [
  # Core classes
  'Rank',
  'King',
  'Pawn',
  'Bishop',
  'Knight',
  'Rook',
  'Queen',
  'RankSpec',
  'RankValidator',

  *exception.__all__,

  # Package metadata and utilities
  '__version__',
  '__author__',
  'package_info',
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