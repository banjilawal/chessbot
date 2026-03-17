# src/logic/system/relation/debug/analzyer.py

"""
Module: logic.system.relation.debug.analyzer
Author: Banji Lawal
Created: 2025-12-28
version: 1.0.0
"""
from typing import Any, Optional

from logic.system import DebugException, OperationException

__all__ = [
    # ======================# ANALYZER_FAILURE_EXCEPTION #======================#
    "AnalyzerFailureException",
]

# ======================# ANALYZER_FAILURE_EXCEPTION #======================#
class AnalyzerFailureException(DebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that the RelationAnalyzer aborted because a candidate was not 
            validated.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        DebugException
    """
    ERR_CODE = "ANALYZER_FAILURE_EXCEPTION"
    MSG = "A candidate was not validated. Analyzer cannot proceed."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  An error occurred in Analyzer.analysis that, prevented the relation analysis from completing.
        An exception was sent instead of a report.

    Super Class:
        *   OperationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See OperationException class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See WrapperException class for inherited methods.
    """
    ERR_CODE = "ANALYZER_FAILURE_EXCEPTION"
    MSG = "Relation analysis failed."
    MTHD = "analyze"
    OP = "RelationAnalysis"
    RSLT_TYPE = "RelationReport"
    
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

