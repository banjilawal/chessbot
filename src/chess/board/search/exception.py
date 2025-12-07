# src/chess/board/searcher.__init__.py

"""
Module: chess.board.searcher.__init__
Author: Banji Lawal
Created: 2025-10-15
version: 1.0.0
"""

class CoordSearchInvariantBreachException(BoardException, InvariantBreachException):
  """Raised if searching the board for a Coord in the legal range produces either no or many results."""
  DEFAULT_CODE = "BOARD_COORD_INVARIANT_BREACH_ERROR"
  DEFAULT_MESSAGE = (
    "The Board's Coord invariant was breached, There may be a critical state inconsistency. or service loss."
  )


class SquareInvariantBreachException(BoardException, InvariantBreachException):
  """Raised if searching the board for a Board in the legal range produces either no or many results."""
  DEFAULT_CODE = "BOARD_SQUARE_INVARIANT_BREACH_ERROR"
  DEFAULT_MESSAGE = (
    "The Board's Square invariant was breached, There may be a critical state inconsistency. or service loss."
  )





