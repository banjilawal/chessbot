# src/chess/rank/searcher/exception.py

"""
Module: chess.rank.searcher.exception
Author: Banji Lawal
Created: 2025-11-16
version: 1.0.0
"""

# src/rank/searcher/context/collision.py

"""
Module: chess.rank.searcher.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from chess.system import NullException, FinderException, ValidationException
from chess.rank import RankException

__all__ = [
    "RankFinderException",
    
    #========================= NULL RANK_SEARCH_CONTEXT EXCEPTION =========================#
    "NullRankSearchException",
    
    #========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTION =========================#
    "InvalidRankSearchException",
]


class RankFinderException(RankException, FinderException):
    """
    Super class of exception raised by RankSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext raised an exception."


#========================= NULL RANK_SEARCH_CONTEXT EXCEPTION =========================#
class NullRankSearchException(RankFinderException, NullException):
    """Raised if an entity, method, or operation requires Rank but gets null instead."""
    ERROR_CODE = "NULL_RANK_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext cannot be validation"


#========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTION =========================#
class InvalidRankSearchException(RankFinderException, ValidationException):
    """Catchall Exception for RankSearchContextValidator when a candidate fails a sanity check."""
    ERROR_CODE = "RANK_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext validation failed."