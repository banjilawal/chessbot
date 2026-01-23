# src/chess/board/exception/exploration/token.py

"""
Module: chess.board.exception.exploration.token
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
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that a disabled token cannot explore the board

    # PARENT:
        *   BoardExplorationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DISABLED_TOKEN_EXPLORATION"
    DEFAULT_MESSAGE = "Disabled token cannot explore board."