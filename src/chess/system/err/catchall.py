# src/chess/system/err/catchall.py

"""
Module: chess.system.err.catchall
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# CATCHALL EXCEPTION #======================#
    "CatchallException",
]

from chess.system import ChessException


# ======================# CATCHALL EXCEPTION #======================#
class CatchallException(ChessException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identifies the code block in a method where the error occurred.
    2.  Describe what condition or state prevented an operation from completing successfully.
    3.  Lowest part of the 3-layer exception chain. Should not contain other exceptions.

    # ERROR CODE CONVENTION:
    1.  All caps, snake case description of the error with _ERROR as the suffix.

    # DEFAULT MSG CONVENTION:
    1.  Wrapper msg followed by a colon. Description of the error after the colon.
    2.  The Syntax is: [Class] operation failed: [Description]

    # PARENT:
        *   Exception

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val Optional[None])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    """
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
        *   cls_name (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    ERR_CODE = "CLASS_ERROR"
    MSG = "An exception occurred in the class."
    
    def __init__(self, ex: Optional[Exception], err_code: str = ERR_CODE, msg: str = MSG,):
        super().__init__(ex, err_code)
    
