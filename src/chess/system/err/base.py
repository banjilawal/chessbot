# src/chess/system/err/exception.py

"""
Module: chess.system.err.base
Author: Banji Lawal
Created: 2025-10-04
version: 1.0.0
"""

from typing import Optional

__all__ = [
# ======================#  BASE APPLICATION EXCEPTION CLASS #======================#
    "ChessException",
# ======================# IMPLEMENTATION EXCEPTIONS #======================#
    "NotImplementedException",
# ======================# STARVATION EXCEPTIONS #======================#
    "ResourceException",
]

# ======================# BASE APPLICATION EXCEPTION CLASS #======================#
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
