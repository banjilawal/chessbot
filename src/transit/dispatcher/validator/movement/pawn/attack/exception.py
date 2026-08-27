# src/err/transit/dispatcher/validator/movement/offset/pawn/attack/exception.py

"""
Module: err.validator.movement.offset.pawn.attack.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, Optional

from err import PawnOffsetPatternValidatorException
from artifcat import MethodResultType

__all__ = [
    # ======================# ATTACK_OFFSET_PATTERN_VALIDATOR_FAILURE #======================#
    "AttackOffsetPatternValidatorException",
]


# ======================# ATTACK_OFFSET_PATTERN_VALIDATOR_FAILURE #======================#
class AttackOffsetPatternValidatorException(PawnOffsetPatternValidatorException):
    """
    Role:
        - Error Tracing

    Responsibilities:
        1.  Indicate an error occurred in an AttackOffsetPatternValidator failed.

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
        PawnOffsetPatternValidatorException
    """
    MSG = "AttackOffsetPatternValidator error."
    ERR_CODE = "ATTACK_OFFSET_PATTERN_VALIDATOR_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
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
    
    
