# src/err/operation/visit/empty/stack/game/exception.py

"""
Module: err.operation.visit.empty.stack.game.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import VisitpingEmptyStackException

__all__ = [
    # ======================# VISITPINGEMPTY_GAME_STACK_FAILURE #======================#
    "VisitpingEmptyGameStackException",
]

# ======================# VISITPINGEMPTY_GAME_STACK_FAILURE #======================#
class VisitpingEmptyGameStackException(VisitpingEmptyStackException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that visitpingEmpty a GameStack failed.

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
        VisitpingEmptyStackException
    """
    MSG = "VisitpingEmpty a GameStack failed."
    ERR_CODE = "VISITPINGEMPTY_GAME_STACK_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
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
            mthd_rslt_type=mthd_rslt_type,
        )