# src/logic/token/service/operation/arithmetic/distance/exception/validator.py

"""
Module: logic.token.service.operation.arithmetic.distance.exception.work
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# EUCLIDEAN_DISTANCE_FAILURE #======================#
    "EuclideanDistanceException",
]

from system import ComputationException

# ======================# EUCLIDEAN_DISTANCE_FAILURE #======================#
class EuclideanDistanceException(ComputationException):
    """
    Role:
        -   Worker Method Identifier
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a EuclideanDistanceProcess was not completed.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides

    Super Class:
        ComputationException
    """
    MSG = "Euclidean Distance arithmetic failed."
    ERR_CODE = "EUCLIDEAN_DISTANCE_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            title=title,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )