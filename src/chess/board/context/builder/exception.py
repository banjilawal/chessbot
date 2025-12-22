# src/board/searcher/exception.py

"""
Module: chess.board.searcher.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""
from chess.board.context import BoardContextException
from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "BoardSearchContextException",
    
#========================= NULL BOARD_SEARCH_CONTEXT EXCEPTION =========================#
    "NullBoardContextException",
    
#========================= BOARD_SEARCH_CONTEXT VALIDATION EXCEPTION =========================#
    "InvalidBoardSearchContextException",
    "NoBoardSearchOptionSelectedException",
    "MoreThanOneBoardSearchOptionPickedException",
    
#========================= BOARD_SEARCH_CONTEXT BUILD EXCEPTION =========================#
    "BoardContextBuildFailedException",
]


class BoardSearchContextException(ContextException):
    """
    Super class of exception raised by TeamSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext raised an exception."


#========================= NULL_BOARD_CONTEXT EXCEPTION =========================#
class NullBoardContextException(BoardContextException, NullException):
    """Raised if an entity, method, or operation requires Board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext cannot be validation"


#========================= BOARD_SEARCH_CONTEXT VALIDATION EXCEPTION =========================#
class InvalidBoardSearchContextException(
    BoardSearchContextException,
    ValidationException
):
    """Catchall Exception for BoardSearchContextValidator when a candidate fails a sanity check.""""""
    ERROR_CODE = "BOARD_SEARCH_CONTEXT_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext validation failed."


class NoBoardSearchOptionSelectedException(
    BoardSearchContextException,
    NoBuildOptionSelectedException
):
    """"""
    ERROR_CODE = "NO_BOARD_SEARCH_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the TeamSearchContext options wre selected. An option must be picked."


class MoreThanOneBoardSearchOptionPickedException(
    BoardSearchContextException,
    BuildOptionSelectionTooLargeException
):
    """
    ERROR_CODE = "TOO_MANY_BOARD_SEARCH_OPTIONS_ERROR"
    DEFAULT_MESSAGE = "Only one TeamSearchContext option can be selected."


#========================= BOARD_CONTEXT_BUILD EXCEPTION =========================#
class BoardContextBuildFailedException(BoardSearchContextException, BuildFailedException):
    """
    Catchall Exception for BoardSearchContextBuilder when it encounters an error building
    a TeamSearchContext.
    """
    ERROR_CODE = "BOARD_SEARCH_CONTEXT_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext build failed."

