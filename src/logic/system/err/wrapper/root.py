# src/logic/system/err/worker.py

"""
Module: logic.system.err.worker
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# WORKER_EXCEPTION #======================#
    "WorkerException",
]

from logic.system import ChessException

# ======================# WORKER_EXCEPTION #======================#
class WorkerException(ChessException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Abstract exception for Worker subclasses which indicate
            *   The worker
            *   It's method
        that produced an exception instead of a payload in it's result.
    
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

    # CONSTRUCTOR PARAMETERS:)
        *   err_code (str)
        *   msg (str
        *   ex (Optional[Exception])
        *   mthd (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    ERR_CODE = "METHOD_FAILURE"
    MSG = "method failed."
    MTHD: None
    
    _mthd: Optional[str]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        mthd = mthd or self.MTHD
        msg = msg or self.MSG
        super().__init__(err_code=err_code, msg=msg, ex=ex)
        self._mthd = mthd
    
    @property
    def mthd(self) -> Optional[str]:
        return self._mthd
    
    def __str__(self):
        return f"{super().__str__()}, mthd:{self._mthd}"
    