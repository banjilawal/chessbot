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
    None
    """
    ERR_CODE = "RELATION_ANALYSIS_FAILURE"
    MSG = "Relation analysis failed."
    MTHD =  "analyze"
    OP_NAME = "RelationAnalysis"
    RSLT = "RelationReport"

    
    def __init__(
            self,
            rslt: Optional[str] = None,
            op_name: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        rslt = rslt or self.RSLT
        op_name = op_name or self.OP_NAME
        mthd = mthd or self.MTHD
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, rslt=rslt, mthd=mthd, op_name=op_name)
