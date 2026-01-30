# src/chess/token/database/exception/deletion/wrapper.py

"""
Module: chess.token.database.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# EXHAUSTIVE_TOKEN_DELETION_FAILURE EXCEPTION #======================#
    "ExhaustiveTokenDeletionFailedException",
]

from chess.token import TokenException
from chess.system import DeletionFailedException


# ======================# EXHAUSTIVE_TOKEN_DELETION_FAILURE EXCEPTION #======================#
class ExhaustiveTokenDeletionFailedException(TokenException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why deleting all occurrences of a occupant failed. deletion fails. The
        encapsulated exceptions create chain for tracing the source of the failure.

    # PARENT:
        *   TokenException
        *   DeletionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXHAUSTIVE_TOKEN_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Exhaustive occupant deletion failed."