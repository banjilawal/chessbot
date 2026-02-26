# src/chess/system/relation/analysis/wrapper.py

"""
Module: chess.system.relation.analysis.wrapper
Author: Banji Lawal
Created: 2026-12-28
version: 1.0.0
"""
from typing import Optional

from chess.system import OperationException

__all__ = [
    # ======================# RELATION_ANALYSIS_FAILURE #======================#
    "AnalysisException",
]

# ======================# RELATION_ANALYSIS_FAILURE #======================#
class AnalysisException(OperationException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in Analyzer.analysis that, prevented the relation analysis from completing.
        An exception was sent instead of a report.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

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
        *   See WrapperException class for inherited methods.
    """
    ERR_CODE = "RELATION_ANALYSIS_FAILURE"
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

