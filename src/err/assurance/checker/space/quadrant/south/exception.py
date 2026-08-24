# src/err/assurance/checker/space/quadrant/exception.py

"""
Module: err.assurance.checker.space.quadrant.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional

from err import QuadrantCheckerException
from artifcat import MethodResultType


__all__ = [
    # ======================# SOUTWEST_QUADRANT_INTEGRITY_CHECKER_FAILURE #======================#
    "SoutwestQuadrantCheckerException",
]

# ======================# SOUTWEST_QUADRANT_INTEGRITY_CHECKER_FAILURE #======================#
class SoutwestQuadrantCheckerException(QuadrantCheckerException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicating assurance by an SoutwestQuadrantSChecker failed.

    Attributes:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        SoutwestQuadrantCheckerException
    """
    MSG = "SoutwestQuadrantRootCerfier failure."
    ERR_CODE = "SOUTWEST_QUADRANT_INTEGRITY_CHECKER_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: Optional[Exception]
            cls_name: Optional[Str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT_TYPE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
           mthd_rslt_type=mthd_rslt_type,
        )
