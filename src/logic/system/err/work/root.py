# src/logic/system/err/worker.py

"""
Module: logic.system.err.work
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# WORK_EXCEPTION #======================#
    "WorkException",
]

from logic.system import ChessException

# ======================# WORK_EXCEPTION #======================#
class WorkException(ChessException):
    """
    Role:
        -   Process Identifier
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Abstract exception for Work subclasses which indicate
                -   The work
                -   It's method
            that produced an exception instead of a payload in it's result.
    
    Naming Convention:
        1.  Prefix is the Class name with the Result name.
        2.  The operation name should match the Result subclass.
        3.  Operation outcome. This will always be Failed.
        4.  Suffix is Exception.
        5.  The Syntax is: [ClassName][ResultClassName]FailedException
    
    Error Code Convention:
        1.  All caps, snake case. Prefix is the class name followed by the operation name.
        2.  The operation name should match the type of result.
        3.  Suffix is Exception.
        2.  The Syntax is: [WORK_TITLE]_[OPERATION]_FAILURE
    
    Default MSG Convention:
        1.  Sentence whose first word is the class name followed by the operation name.
        2.  The sentence ends with failed.
        3.  The Syntax is: [Class] operation failed.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:
    
    Super Class:
        ChessException
    """
    MSG = "method failed."
    ERR_CODE = "METHOD_FAILURE"
    
    _mthd: Optional[str]
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(err_code=err_code, msg=msg, ex=ex)
        self._mthd = mthd
    
    @property
    def mthd(self) -> Optional[str]:
        return self._mthd
    
    def __str__(self):
        return f"{super().__str__()}, mthd:{self._mthd}"
    