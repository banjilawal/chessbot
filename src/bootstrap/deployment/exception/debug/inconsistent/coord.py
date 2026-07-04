# src/logic//service/operation/promotion/exception/debug/double.py

"""
Module: logic.service.operation.promotion.exception.debug.double
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# INCONSISTENT_TOKEN_COORD_EXCEPTION #======================#
    "InconsistentTokenCoordException",
]

from system import InconsistentStateException


# ======================# INCONSISTENT_TOKEN_COORD_EXCEPTION #======================#
class InconsistentTokenCoordException(InconsistentStateException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that when a Token's current_position differs from its current square's coord.

    Super Class:
        *   InconsistentStateException

    Provides:


    # INHERITED ATTRIBUTES:
        *   InconsistentStateException class for inherited attributes.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See InconsistentStateException class for inherited methods.
    """
    ERR_CODE = "INCONSISTENT_TOKEN_COORD_EXCEPTION"
    MSG = "Token's current position differs from current square's coord."
    
    def __init__(
            self,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            msg: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
