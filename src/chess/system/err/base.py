# src/chess/system/err/base.py

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
    # ======================# IMPLEMENTATION EXCEPTION #======================#
    "NotImplementedException",
    # ======================# STARVATION EXCEPTION #======================#
    "ResourceException",
]


# ======================# BASE APPLICATION EXCEPTION CLASS #======================#
class ChessException(Exception):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception by the application

    # PARENT:
        *   Exception

    # PROVIDES:
    NONE

    # LOCAL ATTRIBUTES:
        Static Class Fields:
            *   ERROR_CODE (str): Static class field
            *   DEFAULT_MESSAGE (str): Static class field
            
        Instance Fields:
            *   ex (Optional[Exception])
            *   error_code (str)
            *   message (str)
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "CHESS_ERROR"
    DEFAULT_MESSAGE = "Chess error occurred."
    
    _message: str
    _error_code: str
    _ex: Optional[Exception]
    
    def __init__(self, message: str = DEFAULT_MESSAGE, error_code: str = ERROR_CODE, ex: Optional[Exception] = None):
        super().__init__(message)
        self._ex = ex
        self._message = message
        self._error_code = error_code
    
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


# ======================# IMPLEMENTATION EXCEPTION #======================#
class NotImplementedException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a desired abstract method or feature has not been implemented in the lower level class,
    2.  Catchall for missing implementation errors that are not covered by lower level NotImplementedException.

    # PARENT:
        *   ChessException

    # PROVIDES:
    NotImplementedException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.
    """
    ERROR_CODE = "NOT_IMPLEMENTED_WARNING"
    DEFAULT_MESSAGE = "Not implemented."


# ======================# STARVATION EXCEPTION #======================#
class ResourceException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  super class of exception related to resource acquisition, release or utilization failures.
    2.  Catchall for resource problems that are not covered by lower level ResourceException subclasses.

    # PARENT:
        *   ChessException

    # PROVIDES:
    ResourceException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.
    """
    ERROR_CODE = "RESOURCE_ERROR"
    DEFAULT_MESSAGE = "Resource raised an exception."
