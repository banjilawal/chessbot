# src/rank/searcher/context/exception.py

"""
Module: chess.rank.searcher.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "RankSearchContextException",
    
#========================= NULL RANK_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullRankSearchContextException",
    
#========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidRankSearchContextException",
    "NoRankSearchOptionSelectedException",
    "MoreThanOneRankSearchOptionPickedException",
    
#========================= RANK_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
    "RankSearchContextBuildFailedException",
]


class RankSearchContextException(ContextException):
    """
    Super class of exceptions raised by RankSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext raised an exception."


#========================= NULL RANK_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullRankSearchContextException(RankSearchContextException, NullException):
    """Raised if an entity, method, or operation requires Rank but gets null instead."""
    ERROR_CODE = "NULL_RANK_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext cannot be validation"


#========================= RANK_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidRankSearchContextException(RankSearchContextException, ValidationException):
    """Catchall Exception for RankSearchContextValidator when a candidate fails a sanity check."""
    ERROR_CODE = "RANK_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext validation failed."


class NoRankSearchOptionSelectedException(RankSearchContextException, NoBuildOptionSelectedException):
    """"""
    ERROR_CODE = "NO_RANK_SEARCH_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the RankSearchContext options wre selected. An option must be picked."


class MoreThanOneRankSearchOptionPickedException(
    RankSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """"""
    ERROR_CODE = "TOO_MANY_RANK_SEARCH_OPTIONS_ERROR"
    DEFAULT_MESSAGE = "Only one RankSearchContext option can be selected."


#========================= RANK_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
class RankSearchContextBuildFailedException(RankSearchContextException, BuildFailedException):
    """
    Catchall Exception for RankSearchContextBuilder when it encounters an error building
    a RankSearchContext.
    """
    ERROR_CODE = "RANK_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "RankSearchContext build failed."