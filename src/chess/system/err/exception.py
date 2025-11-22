# src/chess/system/err/collision.py

"""
Module: chess.system.err.exception
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

__all__ = [
    "ChessException",
    
    # ======================# ROLL_BACK EXCEPTIONS #======================#
    "RollbackException",
    "RollbackFailedException",
    
    # ======================# IMPLEMENTATION EXCEPTIONS #======================#
    "NotImplementedException",
    
    # ======================# STARVATION EXCEPTIONS #======================#
    "ResourceException",

    # ======================# INCONSISTENCY EXCEPTIONS #======================#
    "InconsistencyException",
    "InvariantBreachException",
    "InconsistentCollectionException",
    
    # ======================# BUILD_OPTIONS EXCEPTIONS #======================#
    "NoBuildOptionSelectedException",
    "BuildOptionSelectionTooLargeException",
    
    # ======================# NULL/EMPTY EXCEPTIONS #======================#
    "NullException",
    "NullNumberException",
    "NullStringException",
    "BlankStringException",
    
    # ======================# GAME_COLOR EXCEPTIONS #======================#
    "GameColorException",
    "InvalidGameColorException",
    "NullGameColorException",
]

from typing import Optional


class ChessException(Exception):
    """Super class for application exceptions. do not use directly."""
    ERROR_CODE = "CHESS_ERROR"
    DEFAULT_MESSAGE = "Chess error occurred."
    _ex: Optional[Exception]
    _error_code: str
    _message: str
    
    def __init__(
            self,
            message: str = DEFAULT_MESSAGE,
            error_code: str = ERROR_CODE,
            ex: Optional[Exception] = None,
    ):
        self._ex = ex
        self._error_code = error_code
        self._message = message
        super().__init__(message)
    
        
    @property
    def ex(self) -> Exception:
        return self._ex
    
    @property
    def error_code(self) -> str:
        return self._error_code
    
    @property
    def msg(self) -> str:
        return self._message
    
    def __str__(self):
        return f"{self._error_code}: {self._message}"
    
    # Only the super class needs the explict constructor
    # def __init__(self, message: str):
    #     self.message = message or self.DEFAULT_MESSAGE
    #     super().__init__(self.message)
    
    # Only the super class needs to declare team_name toString. Subclasses
    # will use this.





# ======================# IMPLEMENTATION EXCEPTIONS #======================#
class NotImplementedException(ChessException):
    ERROR_CODE = "NOT_IMPLEMENTED_WARNING"
    DEFAULT_MESSAGE = "Not implemented."


# ======================# STARVATION EXCEPTIONS #======================#
class ResourceException(ChessException):
    ERROR_CODE = "RESOURCE_ERROR"
    DEFAULT_MESSAGE = "Resource raised an exception."


# ======================# INCONSISTENCY EXCEPTIONS #======================#
class InconsistencyException(ChessException):
    """
    Raised if service inconsistency is detected
    """
    ERROR_CODE = "DATA_INCONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "A service inconsistency was detected."


class InvariantBreachException(ChessException):
    """
    Raised when a fundamental invariant of the system or environment is violated.
    This rollback_exception type signals a breach of consistency — meaning the system’s
    assumptions about its internal state are no longer valid.
    """
    DEFAULT_CODE = "INVARIANT_BREACH_ERROR"
    DEFAULT_MESSAGE = "A system invariant was violated, indicating a critical state inconsistency. or service loss."


class InconsistentCollectionException(InconsistencyException):
    """
    Raised if a data_set's state is inconsistent or its service corrupted
    """
    ERROR_CODE = "INCONSISTENT_COLLECTION_ERROR"
    DEFAULT_MESSAGE = "Collection is an inconsistent state. Data might be corrupted."


# ======================# BUILD_OPTIONS EXCEPTIONS #======================#
class NoBuildOptionSelectedException(ChessException):
    """
    Raised when none of the possible options required to builder an object are selected.
    Mainly used by Context classes
    """
    ERROR_CODE = "NO_BUILD_OPTION_SELECTED_ERROR"
    DEFAULT_MESSAGE = "None of the options required for the builder were."


class BuildOptionSelectionTooLargeException(ChessException):
    """Raised when too many of the available builder options are selected. Mainly used by Context classes."""
    ERROR_CODE = "TOO_MANY_BUILD_OPTIONS_SELECTED_ERROR"
    DEFAULT_MESSAGE = "Too many builder options were selected."



