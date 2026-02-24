# src/chess/hostage/exception.py

"""
Module: chess.hostage.exception
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from chess.system import ChessException

__all__ = [
    # ======================# HOSTAGE EXCEPTION #======================#
    "HostageException",
]

# ======================# HOSTAGE EXCEPTION #======================#
class HostageException(ChessException):
    """
    # ROLE: Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Catchall for Hostage exceptions.
  
    # PARENT:
        *   ChessException
  
    # PROVIDES:
    None
  
    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "HOSTAGE_ERROR"
    DEFAULT_MESSAGE = "Hostage raised an exception."