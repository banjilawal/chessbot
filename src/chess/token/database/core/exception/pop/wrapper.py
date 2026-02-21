# src/chess/token/database/core/exception/deletion/wrapper.py

"""
Module: chess.token.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_DELETION_FAILURE EXCEPTION #======================#
    "PoppingTokenException",
]

from chess.token import TokenException
from chess.system import DeletionFailedException


# ======================# TOKEN_DELETION_FAILURE EXCEPTION #======================#
class PoppingTokenException(TokenException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a TokenStack deletion fails. The encapsulated exceptions create
        chain for tracing the source of the failure.

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
    ERROR_CODE = "TOKEN_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Token deletion failed."