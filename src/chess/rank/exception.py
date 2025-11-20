# src/chess/rank/exception.py

"""
Module: chess.rank.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, BuildFailedException, NullException

__all__ = [
    "RankException",
    "NullRankException",
# ======================# RANK BUILD EXCEPTIONS #======================#
    "RankBuildFailedException",
    
# ======================# RANK MOVING EXCEPTIONS #======================#
    "MovingException",
    "KingMovingException",
    "PawnMovingException",
    "KnightMovingException",
    "BishopMovingException",
    "RookMovingException",
    "QueenMovingException"
]



class RankException(ChessException):
    """
    Super class of exceptions raised by Rank objects. Do not use directly.
    Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_ERROR"
    DEFAULT_MESSAGE = "Rank raised an exception."


class NullRankException(RankException, NullException):
    ERROR_CODE = "NULL_RANK_ERROR"
    DEFAULT_MESSAGE = "Rank cannot be null."


# ======================# RANK MOVING EXCEPTIONS #======================#
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
