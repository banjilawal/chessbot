# src/chess/rank/exception.py

"""
Module: chess.rank.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import ChessException, BuildFailedException, NullException

___all__ = [
    # ======================# RANK EXCEPTION #======================#
    "RankException",
]


# ======================# RANK EXCEPTION #======================#
class RankException(ChessException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Rank errors not covered by RankException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "RANK_ERROR"
    DEFAULT_MESSAGE = "Rank raised an exception."