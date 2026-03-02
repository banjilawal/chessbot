# src/logic/square/database/core/util/stats/exception/super.py

"""
Module: logic.square.database.core.util.stats.exception.super
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

___all__ = [
    # ======================# SQUARE_STACK_ANALYZER_EXCEPTION #======================#
    "SquareStackServiceException",
]

from logic.system import AnchorException


# ======================# SQUARE_STACK_ANALYZER_EXCEPTION #======================#
class SquareStackAnalyzerException(AnchorException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Provide SquareStackAnalyzer as:
            *   Reporting
            *   Coverage
        target for layer-2 debugging exceptions.
    2.  Indicate which SquareStackAnalyzer method received a worker's (layer-1) failure result.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    CLS_MTHD = None
    CLS_NAME = "SquareStackAnalyzer"
    ERR_CODE = "SQUARE_STACK_ANALYZER_EXCEPTION"
    MSG = "SquareStackAnalyzer raised an exception."
 
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None
    ):
        """
        Args:
            msg: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)

___all__ = [
    # ======================# SQUARE_STACK_ANALYZER_EXCEPTION #======================#
    "SquareStackAnalyzerException",
]

from logic.system import AnchorException

# ======================# SQUARE_STACK_ANALYZER_EXCEPTION #======================#
class SquareStackAnalyzerException(AnchorException):
    """
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in SquareStackAnalyzer.
    2.  The method where the error occurred is identified in the exception
        nested directly underneath.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
