# src/logic/token/service/operation/arithmetic/addition/exception/validator.py

"""
Module: logic.token.service.operation.arithmetic.addition.exception.work
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COORD_ADDITION_FAILURE #======================#
    "CoordAdditionException",
]

from logic.system import ComputationException

# ======================# COORD_ADDITION_FAILURE #======================#
class CoordAdditionException(ComputationException):
    """
    Role:
        -   Worker Method Identifier
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a CoordAdditionProcess was not completed.
        2.  Identify the method where the failure occurred.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides

    Super Class:
        ComputationException
    """
    MSG = "Coord addition failed."
    ERR_CODE = "COORD_ADDITION_FAILURE"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
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