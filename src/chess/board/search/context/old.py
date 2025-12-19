# src/board/searcher/context/exception.py

"""
Module: chess.board.searcher.context.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""


from chess.system import (
    BuildOptionSelectionTooLargeException, ContextException, NoBuildOptionSelectedException, NullException,
    BuildFailedException, ValidationException,
)

__all__ = [
    "BoardSearchContextException",
    
#========================= NULL BOARD_SEARCH_CONTEXT EXCEPTIONS =========================#
    "NullBoardSearchContextException",
    
#========================= BOARD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
    "InvalidBoardSearchContextException",
    "NoBoardSearchOptionSelectedException",
    "MoreThanOneBoardSearchOptionPickedException",
    
#========================= BOARD_SEARCH_CONTEXT BUILD EXCEPTIONS =========================#
    "BoardContextBuildFailedException",
]


class BoardSearchContextException(ContextException):
    """
    Super class of exceptions raised by TeamSearchContext objects.
    Do not use directly. Subclasses give precise, fined-grained, debugging info.
    """
    ERROR_CODE = "SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext raised an exception."


#========================= NULL BOARD_SEARCH_CONTEXT EXCEPTIONS =========================#
class NullBoardSearchContextException(BoardSearchContextException, NullException):
    """Raised if an entity, method, or operation requires Board but gets null instead."""
    ERROR_CODE = "NULL_BOARD_SEARCH_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamSearchContext cannot be validation"


#========================= BOARD_SEARCH_CONTEXT VALIDATION EXCEPTIONS =========================#
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


from chess.system import BoundsException
from chess.coord import InvalidCoordContextException

__all__ = [
    # ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveCoordContextFlagsSetException"
]


# ========================= EXCESSIVE_COORD_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveCoordContextFlagsSetException(InvalidCoordContextException, BoundsException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates more than one CoordContext flag was enabled. Only one Coord attribute-value tuple can be used in
        a search.

    # PARENT:
        *   BoundsException
        *   InvalidCoordContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "EXCESSIVE_COORD_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "Excessive CoordContext flags were set. Only one CoordContext flag is allowed."