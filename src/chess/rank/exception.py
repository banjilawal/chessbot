# src/chess/rank_name/exception.py

"""
Module: chess.rank_name.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, BuildFailedException

__all__ = [
  "RankException",

#======================# RANK BUILD EXCEPTIONS #======================#  
  "RankBuildFailedException",

#======================# RANK MOVING EXCEPTIONS #======================#  
  "MovingException",
  "KingMovingException",
  "PawnMovingException",
  "KnightMovingException",
  "BishopMovingException",
  "RookMovingException",
  "QueenMovingException"
]

class RankException(ChessException):
  ERROR_CODE = "RANK_ERROR"
  DEFAULT_MESSAGE = "Rank raised an rollback_exception."


# ======================# SQUARE BUILD EXCEPTIONS #======================# 
class RankBuildFailedException(RankException, BuildFailedException):
  """
  Raised when RankBuilder encounters an error building a `Rank`. Exists primarily
  to catch all exceptions raised creating new `Rank`.
  """
  ERROR_CODE = "RANK_BUILD_FAILED_ERROR"
  DEFAULT_MESSAGE = "Rank build failed." 


#======================# RANK MOVING EXCEPTIONS #======================#  
class MovingException(RankException):
  ERROR_CODE = "RANK_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid move."

class BishopMovingException(RankException):
  ERROR_CODE = "BISHOP_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid bishop move"

class KingMovingException(RankException):
  ERROR_CODE = "KING_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid occupation move"

class KnightMovingException(RankException):
  ERROR_CODE = "KNIGHT_MOVING_ERROR"
  DEFAULT_MESSAGE = "Invalid knight move"

class PawnMovingException(RankException):
    ERROR_CODE = "PAWN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid pawn move"

class QueenMovingException(RankException):
    ERROR_CODE = "QUEEN_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid queen move"

class RookMovingException(RankException):
    ERROR_CODE = "ROOK_MOVING_ERROR"
    DEFAULT_MESSAGE = "Invalid rook move"




