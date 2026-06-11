# src/err/operation/registration/stack/graph/exception.py

"""
Module: err.operation.registration.stack.graph.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import StackRegistrationException

__all__ = [
    # ======================# GRAPH_STACK_REGISTRATION_FAILURE #======================#
    "GraphStackRegistrationException",
]

# ======================# GRAPH_STACK_REGISTRATION_FAILURE #======================#
class GraphStackRegistrationException(StackRegistrationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that registrationing onto a GraphStack failed.

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
        RegistrationingStackException
    """
    MSG = "Registrationing ont a GraphStack failed."
    ERR_CODE = "GRAPH_STACK_REGISTRATION_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            Mthd_rslt_Type: optional[methodResultType] | None = none,
    ):
        """
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: optional[Exception]
            cls_name: optional[Str]
            cls_mthd: optional[str]
            err_code: optional[str]
            mthd_rslt_type: optional[methodResultType]
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