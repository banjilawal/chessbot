# src/agent/search/context/exception.py

"""
Module: chess.agent.search.context.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "BoardSearchContextException",
    
# ========================= NULL BOARD_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullBoardSearchContextException",
    
# ========================= BOARD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidBoardSearchContextException",
    "NoBoardSearchOptionSelectedException",
    "MoreThanOneBoardSearchOptionPickedException",
    
# ========================= BOARD_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
    "BoardSearchContextBuildFailedException",
]


class BoardSearchContextException(ContextException):
    """
    Super class of exceptions raised by AgentTeamSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext raised an exception."


#========================= NULL BOARD_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullBoardSearchContextException(BoardSearchContextException, NullException):
    """Raised if an entity, method, or operation requires Board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext cannot be null"


#========================= BOARD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
class InvalidBoardSearchContextException(
    BoardSearchContextException,
    ValidationException
):
    """Catchall Exception for BoardSearchContextValidator when a validation candidate fails a sanity check."""
    ERROR_CODE = "BOARD_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext validation failed."


class NoBoardSearchOptionSelectedException(
    BoardSearchContextException,
    NoBuildOptionSelectedException
):
    """"""
    ERROR_CODE = "NO_BOARD_SEARCH_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the AgentTeamSearchContext options wre selected. An option must be picked."


class MoreThanOneBoardSearchOptionPickedException(
    BoardSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """"""
    ERROR_CODE = "TOO_MANY_BOARD_SEARCH_OPTIONS_ERROR"
    DEFAULT_MESSAGE = "Only one AgentTeamSearchContext option can be selected."


#========================= BOARD_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
class BoardSearchContextBuildFailedException(BoardSearchContextException, BuildFailedException):
    """
    Catchall Exception for BoardSearchContextBuilder when it encounters an error building
    a AgentTeamSearchContext.
    """
    ERROR_CODE = "BOARD_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "AgentTeamSearchContext build failed."