# src/err/validation/toggle/carrier/board/exception.py

"""
Module: err.validation.toggle.carrier.board.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations

from typing import Any, Optional

from err import EntityCarrierValidatorException
from result import MethodResultType


__all__ = [
    # ======================# BOARD_CARRIER_VALIDATOR_FAILURE #======================#
    "BoardCarrierValidatorException",
]

# ======================# BOARD_CARRIER_VALIDATOR_FAILURE #======================#
class BoardCarrierValidatorException(EntityCarrierValidatorException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a BoardCarrierValidator test.

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
        CarrierValidatorException
    """
    MSG = "BoardCarrier validation failed."
    ERR_CODE = "BOARD_CARRIER_VALIDATOR_FAILURE"
    
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
