# src/logic/token/context/finder/exception/debug/dataset.py

"""
Module: logic.token.context.finder.exception.debug.dataset
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

__all__ = [
    "TokenSearchNullDatasetException",
]

from logic.token import Token
from logic.system import NullDatasetException


# ======================# TOKEN_NULL_DATASET EXCEPTION #======================#
class TokenSearchNullDatasetException(Token, NullDatasetException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That TokenFinder received null instead of a List[Token] collection.

    # PARENT:
        *   CollectionException
        *   NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_SEARCH_DATASET_NULL_EXCEPTION"
    MSG = "TokenSearch failed: Cannot run a search on a null dataset."