# src/context/abstract/exception/null.py

"""
Module: context.abstract.exception.null
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import NullContextException

_all_ = [
    # ======================# NULL_ALGEBRA_CONTEXT_EXCEPTION #======================#
    "NullAlgebraContextException",
]

# ======================# NULL_ALGEBRA_CONTEXT_EXCEPTION #======================#
class NullAlgebraContextException(NullContextException):
    """
    Role:
        -   Error tracing

    Responsibilities:
        1.  Indicate that null was received instead of an AlgebraContext.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides:

    Super Class:
       NullContextException
    """
    MSG = str = "AlgebraContext cannot be null."
    ERR_CODE = "NULL_ALGEBRA_CONTEXT_EXCEPTION"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
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
        )