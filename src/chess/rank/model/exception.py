# src/chess/rank/exception.py

"""
Module: chess.rank.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException

___all__ = [
    # ======================# RANK EXCEPTION #======================#
    "RankException",
]


# ======================# RANK EXCEPTION #======================#
class RankException(ChessException):
    """
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Rank errors not covered by RankException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "RANK_ERROR"
    MSG = "Rank raised an exception."