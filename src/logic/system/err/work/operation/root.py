# src/logic/system/err/work/operation/root.py

"""
Module: logic.system.err.work.operation.root
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# OPERATION_FAILURE #======================#
    "OperationException",
]

from logic.system import WorkException


# ======================# OPERATION_FAILURE #======================#
class OperationException(WorkException):
    """
    Role:
        -   Process Identifier
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Identifies which WorkerClass method the error was caught.
        2.  Encapsulates the DebugException created after, a code block triggers a variable into its
            error state.

    Naming Convention:
        1.  Prefix is the Class schema with the Result schema.
        2.  The operation schema should match the Result subclass.
        3.  Operation outcome. This will always be Failed.
        4.  Suffix is Exception.
        5.  The Syntax is: [ClassName][ResultClassName]FailedException

    Error Code Convention::
        1.  All caps, snake case. Prefix is the class schema followed by the operation schema.
        2.  The operation schema should match the type of result.
        3.  Suffix is Exception.
        2.  The Syntax is: [Class]_[OPERATION]_FAILURE

    Default MSG Convention:
        1.  Sentence whose first word is the class schema followed by the operation schema.
        2.  The sentence ends with failed.
        3.  The Syntax is: [Class] operation failed.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:
    
    Super Class:
        WorkException
    """
    MSG = "Failure in method."
    ERR_CODE = "OPERATION_FAILURE"

    _op = Optional[str]
    _title = Optional[str]
    _rslt_type = Optional[str]
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd)
        self._op = op
        self._title = title
        self._rslt_type = rslt_type
    
    @property
    def op(self) -> Optional[str]:
        return self._op
    
    @property
    def title(self) -> Optional[str]:
        return self._title
    
    @property
    def rslt_type(self) -> Optional[str]:
        return self._rslt_type
    
    def __str__(self):
        return f"{super().__str__()}, op:{self._op}, rslt_type:{self._rslt_type}"


    

