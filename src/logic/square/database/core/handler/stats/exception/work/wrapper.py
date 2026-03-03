# src/logic/square/database/core/handler/stats/exception/work/wrapper.py

"""
Module: logic.square.database.core.handler.stats.exception.work.wrapper
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_STACK_COUNTS_ANALYSIS_FAILURE #======================#
    "SquareStackCountsAnalysisException",
]

from typing import Optional

from logic.system import ComputationException


# ======================# SQUARE_STACK_COUNTS_ANALYSIS_FAILURE #======================#
class SquareStackCountsAnalysisException(ComputationException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the computation failed.

    # PARENT:
        *   ComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ComputationException class for inherited attributes.

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
        *   See ComputationException class for inherited methods.
    """
    ERR_CODE = "SQUARE_STACK_COUNTS_ANALYSIS_FAILURE"
    MSG = "SquareStackCountsAnalysis failed."
    MTHD = "compute"
    OP_NAME = "Computation"
    RSLT = "ComputationResult"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)