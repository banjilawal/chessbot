# src/logic/board/analyzer/wrapper.py

"""
Module: logic.board.analyzer.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE #======================#
    "BoardSquareAnalyzerFailureException",
]

from logic.system import AnalysisException


# ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE #======================#
class BoardSquareAnalyzerFailureException(AnalysisException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate a computation was unsuccessful and did not produce a result.
        2.  Identify the method where the failure occurred.

    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super:
        OperationException
    """
    OP = "Computation"
    RSLT_TYPE = "ComputationResult"
    ERR_CODE = "COMPUTATION_FAILURE"
    MSG = "Computation method failed."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
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
    """
    Role:Exception Wrapper, Encapsulation, Error Chaining

    Responsibilities:
    1.  Wrap any exception that kills the relation test process before the board-item relationship
        status has been evaluated.

    Super Class:
        *   WrapperException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_SQUARE_RELATION_ANALYSIS_FAILURE"
    MSG = "Board-Square relation analysis failed."