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

from typing import Optional

from chess.system import ChessException


# ======================# CATCHALL EXCEPTION #======================#
class CatchallException(ChessException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Identifies the class or module in which the error occurred.
    2.  Encapsulates the WrapperException which identifies the method that raised the error.
    3.  Topmost part of the 3-layer exception chain. Should only contain a WrapperException.

    # RESPONSIBILITIES:
    1.  Outermost layer of the 3-part exception chain that is created when an operation's result is failure.
    
    # NAMING CONVENTION:
    1.  Class name followed by the Exception suffix
    2.  The Syntax is: [Class]Exception

    # ERROR CODE CONVENTION:
    1.  Class name followed by the ERROR suffix.
    2.  The Syntax is: [Class]_ERROR
    
    # DEFAULT MSG CONVENTION:
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
    ERR_CODE = "CATCHALL_ERROR"
    MSG = "CatchallException."
    
    def __init__(self, ex: Optional[Exception], err_code: str = ERR_CODE, msg: str = MSG,):
        super().__init__(ex, err_code)