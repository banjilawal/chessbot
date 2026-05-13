# MISSING_src/err/route/validation/context/game/exception.py

"""
Module: err.route.validation.context.game.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""
from __future__ import annotations
from typing import Any, Optional

from err import ValidationRouteException


__all__ = [
    # ======================# MISSING_GAME_CONTEXT_VALIDATION_ROUTE #======================#
    "GameContextValidationRouteException",
]

from err import ContextValidationRouteException


# ======================# MISSING_GAME_CONTEXT_VALIDATION_ROUTE #======================#
class GameContextValidationRouteException(ContextValidationRouteException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that one of GameContext validation routes is missing.

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
        ContextValidationRouteException
    """
    MSG = "A GameContext attribute missing a validation path."
    ERR_CODE = "GAME_CONTEXT_VALIDATION_ROUTE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
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
        )
