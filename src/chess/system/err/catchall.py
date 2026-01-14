# src/chess/system/err/catchall.py

"""
Module: chess.system.err.catchall
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

__all__ = [
    # ======================# CATCHALL EXCEPTION #======================#
    "CatchallException",
]

from chess.system import ChessException


# ======================# CATCHALL EXCEPTION #======================#
class CatchallException(ChessException):
    """
    # ROLE: Catchall, Exception Messaging

    # RESPONSIBILITIES:
    1.  Outermost layer of the 3-part exception chain that is created when an operation's result is failure.
    
    # NAMING CONVENTION:
    1.  Class name followed by the Exception suffix
    2.  The Syntax is: [Class]Exception

    # ERROR CODE CONVENTION:
    1.  Class name followed by the ERROR suffix.
    2.  The Syntax is: [Class]_ERROR
    
    # DEFAULT MESSAGE CONVENTION:
    1.  Class name followed by "raised an exception."
    2.  The Syntax is: [Class] raised an exception

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "CATCHALL_ERROR"
    DEFAULT_MESSAGE = "CatchallException."