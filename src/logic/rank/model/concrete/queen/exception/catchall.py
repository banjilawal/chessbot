# src/logic/rank/model/concrete/queen/exception/super.py

"""
Module: logic.rank.model.concrete.queen.exception.super
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from logic.rank import RankException

__all__ = [
    # ======================# QUEEN_EXCEPTION EXCEPTION #======================#
    "QueenException",
]


# ======================# QUEEN_EXCEPTION EXCEPTION #======================#
class QueenException(RankException):
    """
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Queen errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "QUEEN_EXCEPTION"
    MSG = "Queen raised an exception."