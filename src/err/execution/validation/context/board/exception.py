# src/err/transit/router/validation/context/board/exception.py

"""
Module: err.transit.router.validation.board.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional

from artifcat import MethodResultType
from err import MissingValidationRouteException


__all__ = [
    # ======================# MISSING_BOARD_CONTEXT_VALIDATION_ROUTE #======================#
    "BoardContextValidationRouteMissingException",
]

from err import ContextValidationRouteMissingException


# ======================# MISSING_BOARD_CONTEXT_VALIDATION_ROUTE #======================#
class BoardContextValidationRouteMissingException(ContextValidationRouteMissingException):
    """
    Role:
        - Error Tracing

    Responsibilities:
        1.  Indicating that a BoardContext validation route is missing.

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
        ContextValidationRouteMissingException
    """
    MSG = "A BoardContext attribute missing a validation path."
    ERR_CODE = "MISSING_BOARD_CONTEXT_VALIDATION_ROUTE"
    
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
