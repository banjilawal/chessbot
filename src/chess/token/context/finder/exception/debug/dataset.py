# src/chess/token/context/finder/exception/debug/dataset.py

"""
Module: chess.token.context.finder.exception.debug.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    "TokenSearchDatasetNullException",
]

from chess.token import Token
from chess.system import NullDatasetException


# ======================# TOKEN_NULL_DATASET EXCEPTION #======================#
class TokenSearchDatasetNullException(Token, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That TokenFinder received null instead of a List[Token] collection.

    # PARENT:
        *   DatasetException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_SEARCH_DATASET_NULL_ERROR"
    DEFAULT_MESSAGE = "TokenSearch failed: Cannot run a search on a null dataset."