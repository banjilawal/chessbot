# src/chess/system/find/exception/base.py

"""
Module: chess.system.find.exception.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# SEARCH EXCEPTION #======================#
    "SearchException",
]


# ======================# SEARCH EXCEPTION #======================#
class SearchException(ChessException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised by Search operations and Finders.
    3.  Catchall for Search errors not covered by SearchException subclasses.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SEARCH_ERROR"
    DEFAULT_MESSAGE = "Search raised an error."
