# src/logic/token/service/operation/arithmetic/multiplication/exception/validator.py

"""
Module: logic.token.service.operation.arithmetic.multiplication.exception.work
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COORD_MULTIPLICATION_FAILURE #======================#
    "CoordMultiplicationException",
]

from system import ComputationException

# ======================# COORD_MULTIPLICATION_FAILURE #======================#
class CoordMultiplicationException(ComputationException):
    """
    Role:
        -   Worker Method Identifier
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a CoordMultiplicationProcess was not completed.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[ResultCategory]

    Provides

    Super Class:
        ComputationException
    """
    MSG = "Coord multiplication failed."
    ERR_CODE = "COORD_MULTIPLICATION_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[ResultCategory]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            title=title,
            err_code=err_code,
            rslt_type=rslt_type,
        )