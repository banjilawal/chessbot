# src/err/null/exchange/request/validation/model/attack/mate/exception.py

"""
Module: err.null.exchange.request.validation.model.attack.mate.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Optional

from artifcat import MethodResultType
from err import AttackValidationRequestNullException

__all__ = [
    # ======================# CHECKMATE_ATTACK_VALIDATION_REQUEST_NULL_ERROR #======================#
    "CheckCheckmateAttackValidationRequestNullException",
]

# ======================# CHECKMATE_ATTACK_VALIDATION_REQUEST_NULL_ERROR #======================#
class CheckCheckmateAttackValidationRequestNullException(AttackValidationRequestNullException):
    """
    Role:
        - Error Tracing

    Responsibilities:
        1.  Indicating that a CheckmateAttackValidationRequest is null.

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
        AttackValidationRequestNullException
    """
    MSG = "CheckmateAttackValidationRequest cannot be null."
    ERR_CODE = "CHECKMATE_ATTACK_VALIDATION_REQUEST_NULL_ERROR"
    
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