# src/logic/token/database/core/exception/query/exist.py

"""
Module: logic.token.database.core.exception.query.exist
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# TOKEN_NOT_FOUND EXCEPTION #======================#
    "TokenNotFoundException",
]

from logic.token import TokenDebugException


# ======================# TOKEN_NOT_FOUND EXCEPTION #======================#
class TokenNotFoundException(TokenDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   NullException
        *   TokenStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_NOT_FOUND_EXCEPTION"
    MSG = "Token deletion failed: The item was not found in the dataset. Nothing to remove."