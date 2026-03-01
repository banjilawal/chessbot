# src/logic/rank/model/concrete/rook/exception/super.py

"""
Module: logic.rank.model.concrete.rook.exception.super
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from logic.rank import RankException

__all__ = [
    # ======================# ROOK_EXCEPTION EXCEPTION #======================#
    "RookException",
]

# ======================# ROOK_EXCEPTION EXCEPTION #======================#
class RookException(RankException):
    """
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Rook errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "ROOK_EXCEPTION"
    MSG = "Rook raised an exception."