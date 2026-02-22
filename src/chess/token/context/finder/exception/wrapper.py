# src/chess/token/finder/exception/wrapper.py

"""
Module: chess.token.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_SEARCH_FAILURE #======================#
    "TokenSearchException",
]

from chess.system import SearchException
from chess.token import TokenException


# ======================# TOKEN_SEARCH_FAILURE #======================#
class TokenSearchException(TokenException, SearchException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions indicating why a token search operation failed. The exception chain
        traces the ultimate source of failure..

    # PARENT:
        *   FinderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "TokenSearch failed."