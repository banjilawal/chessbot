# src/chess/rank/spec/collision.py
"""
Module: chess.rank.spec.exception
Author: Banji Lawal
Created: 2025-07-26
version: 1.0.0
"""

from chess.system import ChessException, NullException


__all__ = [
    "RankSpecException",
    "NullRankSpecException",
]




# ======================# RANK_SPEC EXCEPTIONS #======================#
class RankSpecException(ChessException):
    """
    Super class of exceptions raised by RankSpec objects. Do not use directly.
    Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "RANK_SPEC_ERROR"
    DEFAULT_MESSAGE = "RankSpec raised an exception."


class NullRankSpecException(RankSpecException, NullException):
    """Raised if an entity, method, or operation requires RankSpec but gets validation instead."""
    ERROR_CODE = "NULL_RANK_SPEC_ERROR"
    DEFAULT_MESSAGE = "RankSpec cannot be validation."
