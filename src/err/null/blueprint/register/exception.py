# src/err/null/blueprint/register/exception.py

"""
Module: err.null.register.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional



__all__ = [
    # ======================# REGISTER_BLUEPRINT_NULL_ERROR #======================#
    "RegisterBlueprintNullException",
]

from err import BlueprintNullException


# ======================# REGISTER_BLUEPRINT_NULL_ERROR #======================#
class RegisterBlueprintNullException(BlueprintNullException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a required RegisterBlueprint is null.

    Cannot Be Null.s:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            MTHD_RSLT_TYPE: Optional[MethodResultType]
            
    Provides:

    Super Class:
        BlueprintNullException
    """
    MSG = "RegisterBlueprint cannot be null."
    ERR_CODE = "REGISTER_BLUEPRINT_NULL_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            MTHD_RSLT_TYPE: Optional[MethodResultType] | None = None,
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
            MTHD_RSLT_TYPE: Optional[MethodResultType]
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
            MTHD_RSLT_TYPE=MTHD_RSLT_TYPE,
        )
