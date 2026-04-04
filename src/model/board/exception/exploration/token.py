# src/logic/board/exception/exploration/occupant.py

"""
Module: logic.board.exception.exploration.occupant
Author: Banji Lawal
Created: 2026-01-23
version: 1.0.0
"""

__all__ = [
    # ======================# DISABLED_TOKEN_CANNOT_EXPLORE_BOARD EXCEPTION #======================#
    "DisabledTokenCannotExploreException",
]



# ======================# DISABLED_TOKEN_CANNOT_EXPLORE_BOARD EXCEPTION #======================#

class DisabledTokenCannotExploreException(ExplorationException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that a disabled occupant cannot explore the board

    Super Class:
        *   BoardExplorationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "DISABLED_TOKEN_EXPLORATION"
    MSG = "Disabled occupant cannot explore board."