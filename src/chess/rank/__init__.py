# chess/rank/__init__.py

"""
A package providing an immutable hierarchy for chess piece movement.

## PURPOSE
This package encapsulates the movement logic for each type of chess piece. By decoupling a piece's movement
from its core identity, this design ensures that the movement logic is scalable and easy to maintain. Each
`Rank` class represents a distinct movement strategy (e.g., `Bishop`, `Knight`, `Queen`) and is designed
to be immutable once assigned.

## CORE CLASSES
* `Rank`: The base class for all piece rank strategies.
* `Bishop`: Provides movement validation for a bishop.
* `King`: Provides movement validation for a king.
* `Knight`: Provides movement validation for a knight.
* `Pawn`: Provides movement validation for a pawn.
* `Rook`: Provides movement validation for a rook.
* `Queen`: Provides movement validation for a queen.
* `PromotedQueen`: A specialized rank for a promoted queen's movement.

## USAGE
The `Rank` classes are primarily used to validate a piece's movement at runtime. A `Piece` object holds a
reference to its `Rank`, and delegates movement validation to it using the `walk()` method. This allows
for a clean and simple interface for a chess board's logic.

>>> from chess.rank import Knight
>>> from chess.piece import Piece
>>> from chess.coord import Coord
>>>
>>> knight_rank = Knight()
>>> knight_piece = Piece(rank=knight_rank, coord=Coord(2, 2))
>>> destination = Coord(4, 3)
>>>
>>> # Validate the move using the Piece's rank
>>> is_valid = knight_piece.rank.walk(piece=knight_piece, destination=destination)
>>> print(is_valid.is_success())
True

---

## RANK PURPOSE
This package defines specific exceptions for issues encountered during a piece's movement or promotion
validation. This granular approach helps to quickly diagnose and resolve problems by pinpointing the
exact nature of the error, such as an invalid move for a specific piece type. Each team_exception acts as a
wrapper for underlying errors, providing a clean and consistent API for handling movement-related failures.

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
* `BishopValidationException`
* `KingValidationException`
* `KnightValidationException`
* `PawnValidationException`
* `RookValidationException`
* `QueenValidationException`


### EXAMPLE EXCEPTION USAGES
These exceptions are typically raised within a `Rank` class's movement methods and can be caught to handle
invalid moves gracefully.

>>> from chess.rank.team_exception import PawnException
>>>
>>> def move_pawn(start_pos, end_pos):
...     # ... some validation logic
...     if not is_valid_pawn_move:
...         raise PawnException('Pawn cannot move in this way.')
...
>>> try:
...     move_pawn(start_coord, end_coord)
... except PawnException as e:
...     print(f'Invalid Pawn Move: {e}')

---

VERSION: 1.0.0
AUTHOR: Banji Lawal
"""


# Exceptions raised during activities
from .exception import *

# Core Rank classes
from .rank import Rank
from .bishop import Bishop
from .rook import Rook  # Note: Usually called 'Rook' in chess
from .king import King
from .knight import Knight
from .pawn import Pawn
from .queen import Queen
from .promote import PromotedQueen
from .profile import RankProfile


# Package metadata (organic to __init__.py)
__version__ = '1.0.0'
__author__ = 'Banji Lawal'
__package_name__ = 'chess.rank'

# Export control - only what belongs in public API
__all__ = [
    # Core classes
    'Rank',
    'Bishop',
    'Knight',
    'Pawn',
    'Rook',
    'King',
    'Queen',
    'RankProfile',

    *exception.__all__,

    # Package metadata and utilities
    '__version__',
    '__author__',
    'package_info',
]

# Organic utility function for package info
def package_info() -> dict:
    '''Return basic package information.'''
    return {
        'name': __package_name__,
        'version': __version__,
        'author': __author__,
        'exports': __all__
    }