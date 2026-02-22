# src/chess/token/database/core/exception/deletion/wrapper.py

"""
Module: chess.token.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_TOKEN_FAILURE #======================#
    "PoppingTokenException",
]

from chess.system import DeletionException
from chess.token import TokenException


# ======================# POPPING_TOKEN_FAILURE #======================#
class PoppingTokenException(TokenException, DeletionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why popping a token failed. The exception chain
        traces the ultimate source of failure.

    # PARENT:
        *   TokenException
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_TOKEN_FAILURE"
    DEFAULT_MESSAGE = "Popping token failed."