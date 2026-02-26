# src/chess/system/err/wrapper.py

"""
Module: chess.system.err.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# WRAPPER EXCEPTION #======================#
    "WrapperException",
]

from chess.system import ChessException


# ======================# WRAPPER EXCEPTION #======================#
class WrapperException(ChessException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identifies the method in a class where the error occurred.
    2.  Encapsulates the DebugException which identifies the method's code block that raised the error.
    3.  Middle part of the 3-layer exception chain. Should only contain a DebugException.
    
    # NAMING CONVENTION:
    1.  Prefix is the Class name with the Result name. The operation name should match the Result subclass.
    2.  Operation outcome. This will always be Failed.
    3.  Suffix is Exception.
    4.  The Syntax is: [ClassName][ResultClassName]FailedException
    
    # ERROR CODE CONVENTION:
    1.  All caps, snake case. Prefix is the class name followed by the operation name. The operation name should
        match the type of result.
    3.  Suffix is Exception.
    2.  The Syntax is: [Class]_[OPERATION]_FAILURE
    
    # DEFAULT MSG CONVENTION:
    1.  Sentence whose first word is the class name followed by the operation name. The sentence ends with failed.
    2.  The Syntax is: [Class] operation failed.

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   mthd (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        # LOCAL ATTRIBUTES:
            *   mthd (Optional[str])
            
        # INHERITED ATTRIBUTES:
            See ChessException class for inherited attributes.

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    ERR_CODE = "METHOD_FAILURE"
    MSG = "A method failed."
    MTHD: None
    
    _mthd: Optional[str]
    
    def __init__(
            self,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        mthd = mthd or self.MTHD
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE

        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        self._mthd = mthd
    
    @property
    def mthd(self) -> Optional[str]:
        return self._mthd
    
    def __str__(self):
        return f"{super().__str__()}, mthd:{self._mthd}"
    