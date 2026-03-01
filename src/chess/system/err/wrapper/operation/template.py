# src/chess/system/err/wrapper/tOperation/template.py

"""
Module: chess.system.err.wrapper.tOperation.template
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOPERATION_FAILURE #======================#
    "TOperationException",
]

from chess.system import OperationException


# ======================# TOPERATION_FAILURE #======================#
class TOperationException(OperationException):
    """
    # ROLE: Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Identifies which _TWORKER_CLASS__ method the error was caught.
    2.  Encapsulates the DebugException created after, a code block triggers a variable into its
        error state.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See OperationException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See OperationException class for inherited methods.
    """
    ERR_CODE = "TOPERATION_FAILURE"
    MSG = "Failure in _TWORKER_CLASS__ method."
    MTHD: None
    OP: None
    RSLT_TYPE: None
    
    _op = Optional[str]
    _rslt_type = Optional[str]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        op = op or self.OP
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )



    

