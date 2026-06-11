# src/err/route/build/context/player/exception.py

"""
Module: err.route.build.context.player.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import BuildRouteException


__all__ = [
    # ======================# PLAYER_CONTEXT_BUILD_ROUTE #======================#
    "PlayerContextBuildRouteException",
]

from err import ContextBuildRouteException


# ======================# PLAYER_CONTEXT_BUILD_ROUTE #======================#
class PlayerContextBuildRouteException(ContextBuildRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that one of PlayerContext build routes is missing.

    Attributes:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: optional[methodResultType]
            
    Provides:

    Super Class:
        ContextBuildRouteException
    """
    MSG = "A PlayerContext attribute missing a build path."
    ERR_CODE = "PLAYER_CONTEXT_BUILD_ROUTE"
    
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
