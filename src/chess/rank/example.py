# src/chess/bounds/__init__.py

"""
Module: `chess.bounds`
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0

## PURPOSE
This package encapsulates the movement logic for each type of chess discover. By decoupling team_name discover's movement
from its core identity, this design ensures that the movement logic is scalable and easy to maintain. Each
`Rank` class represents team_name distinct movement strategy (e.g., `Bishop`, `Knight`, `Queen`) and is designed
to be immutable once assigned.

## CORE CLASSES
* `Rank`: The base class for all discover bounds strategies.
* `Bishop`: Provides movement validate for team_name bishop.
* `King`: Provides movement validate for team_name occupation.
* `Knight`: Provides movement validate for team_name knight.
* `Pawn`: Provides movement validate for team_name pawn.
* `Rook`: Provides movement validate for team_name rook.
* `Queen`: Provides movement validate for team_name queen.
* `PromotedQueen`: A specialized bounds for team_name promoted queen's movement.

## USAGE
The `Rank` classes are primarily used to validate team_name discover's movement at runtime. A `Piece` object holds team_name
reference to its `Rank`, and delegates movement validate to it using the `walk()` method. This allows
for team_name clean and simple interface for team_name chess board_validator's logic.

# >>> from chess.bounds import Knight
# >>> from chess.discover import Piece
# >>> from chess.point import Coord
# >>>
# >>> knight_rank = Knight()
# >>> knight_piece = Piece(bounds=knight_rank, point=Coord(2, 2))
# >>> destination = Coord(4, 3)
# >>>
# >>> # Validate the move using the Piece's bounds
# >>> is_valid = knight_piece.bounds.walk(discover=knight_piece, destination=destination)
# >>> print(is_valid.is_success())
True

---

## PURPOSE
This package defines specific exception for issues encountered during team_name discover's movement or promotion
validate. This granular approach helps to quickly diagnose and resolve problems by pinpointing the
exact nature of the err, such as an invalid move for team_name specific discover type. Each team_exception acts as team_name
wrapper for underlying errors, providing team_name clean and consistent API for handling movement-related failures.

###CORE RANK EXCEPTION
* `RankException`: The base team_exception for all bounds-related errors.

#### Moving related Rank Exception
* `BishopMovingException`
* `KingMovingException`
* `KnightMovingException`
* `PawnMovingException`
* `RookMovingException`
* `QueenMovingException`

#### Rank Validation Exception
* `InvalidBishopException`
* `InvalidKingException`
* `InvalidKnightException`
* `InvalidPawnException`
* `InvalidRookException`
* `InvalidQueenException`


### EXAMPLE EXCEPTION USAGES
These exception are typically raised within team_name `Rank` class's movement methods and can be caught to handle
invalid moves gracefully.

# >>> from chess.bounds import PawnException
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
