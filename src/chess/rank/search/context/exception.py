# src/rank/searcher/exception.py

"""
Module: chess.rank.searcher.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildException, ValidationException,
)

__all__ = [
    "RankSearchContextException",
    
#========================= NULL RANK_SEARCH_CONTEXT EXCEPTION =========================#
    "NullRankSearchContextException",
    
#========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTION =========================#
    "InvalidRankSearchContextException",
    "NoRankSearchOptionSelectedException",
    "MoreThanOneRankSearchOptionPickedException",
    
#========================= RANK_SEARCH_CONTEXT BUILD EXCEPTION =========================#
    "RankSearchContextBuildException",
]


class RankSearchContextException(ContextException):
    """
    Super class of exception raised by RankSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERR_CODE = "SEARCH_CONTEXT_EXCEPTION"
    MSG = "RankSearchContext raised an exception."


#========================= NULL RANK_SEARCH_CONTEXT EXCEPTION =========================#
class NullRankSearchContextException(RankSearchContextException, NullException):
    """Raised if an entity, method, or operation requires Rank but gets null instead."""
    ERR_CODE = "NULL_RANK_SEARCH_CONTEXT_EXCEPTION"
    MSG = "RankSearchContext cannot be validation"


#========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTION =========================#
class InvalidRankSearchContextException(RankSearchContextException, ValidationException):
    """Super Exception for RankSearchContextValidator when a candidate fails a sanity check."""
    ERR_CODE = "RANK_SEARCH_CONTEXT_VALIDATION_EXCEPTION"
    MSG = "RankSearchContext validation failed."


class NoRankSearchOptionSelectedException(RankSearchContextException, NoBuildOptionSelectedException):
    """"""
    ERR_CODE = "NO_RANK_SEARCH_OPTION_SELECTED_EXCEPTION"
    MSG = "None of the RankSearchContext options wre selected. An option must be picked."


class MoreThanOneRankSearchOptionPickedException(
    RankSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """"""
    ERR_CODE = "TOO_MANY_RANK_SEARCH_OPTIONS_EXCEPTION"
    MSG = "Only one RankSearchContext option can be selected."


#========================= RANK_SEARCH_CONTEXT BUILD EXCEPTION =========================#
class RankSearchContextBuildException(RankSearchContextException, BuildException):
    """
    Super Exception for RankSearchContextBuilder when it encounters an error building
    a RankSearchContext.
    """
    ERR_CODE = "RANK_SEARCH_CONTEXT_BUILD_FAILED"
    MSG = "RankSearchContext build failed."