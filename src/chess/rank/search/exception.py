# src/chess/rank/search/exception.py

"""
Module: chess.rank.search.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

# src/rank/search/context/exception.py

"""
Module: chess.rank.search.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "RankSearchException",
    
    # ========================= NULL RANK_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullRankSearchException",
    
    # ========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidRankSearchException",
]


class RankSearchException(ContextException):
    """
    Super class of exceptions raised by RankSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext raised an exception."


# ========================= NULL RANK_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullRankSearchException(RankSearchException, NullException):
    """Raised if an entity, method, or operation requires Rank but gets null instead."""
    ERROR_CODE = "NULL_RANK_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext cannot be null"


# ========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidRankSearchException(RankSearchException, ValidationException):
    """Catchall Exception for RankSearchContextValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "RANK_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext validation failed."