# MISSING_src/err/route/build/context/player/exception.py

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
    # ======================# MISSING_PLAYER_CONTEXT_BUILD_ROUTE #======================#
    "PlayerContextBuildRouteException",
]

from err import ContextBuildRouteException


# ======================# MISSING_PLAYER_CONTEXT_BUILD_ROUTE #======================#
class PlayerContextBuildRouteException(ContextBuildRouteException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

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
            
    Provides:

    Super Class:
        ContextBuildRouteException
    """
    MSG = "A PlayerContext attribute missing a build path."
    ERR_CODE = "PLAYER_CONTEXT_BUILD_ROUTE"
    
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
