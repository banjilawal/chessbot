# src/chess/token/finder/exception/wrapper.py

"""
Module: chess.token.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_SEARCH_FAILURE EXCEPTION #======================#
    "TokenSearchFailedException",
]

from chess.system import SearchFailedException
from chess.token import TokenException


# ======================# TOKEN_SEARCH_FAILURE EXCEPTION #======================#
class TokenSearchFailedException(TokenException, SearchFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TokenFinder objects.
    2.  Wrap an exception that hits the try-finally block of an TokenFinder method.

    # PARENT:
        *   FinderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SEARCH_FAILURE_ERROR"
    DEFAULT_MESSAGE = "TokenSearch failed."