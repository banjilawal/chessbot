# src/logic/board/analyzer/exception/failure.py

"""
Module: logic.board.analyzer.exception.failure
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE #======================#
    "BoardSquareAnalysisException",
]

from logic.system import AnalysisException


# ======================# BOARD_SQUARE_RELATION_ANALYSIS_FAILURE #======================#
class BoardSquareAnalysisException(AnalysisException):
    """
    Role:
        - Worker Method Identification
        - Exception Chain Layer 1
        - Exception Messaging

    Responsibilities:
        1.  Indicate a arithmetic was unsuccessful and did not produce a result.
        2.  Identify the method where the failure occurred.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super:
        OperationException
    """
    ERR_CODE = "BOARD_SQUARE_RELATION_ANALYSIS_FAILURE"
    MSG = "A rank failed a validation test. BoardSquareAnalyzer cannot proceed. Analysis aborted."
    
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