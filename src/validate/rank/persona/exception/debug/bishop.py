# src/logic/rank/validation/persona/exception/debug/persona/bishop.py

"""
Module: logic.rank.validation.persona.exception.debug.persona.bishop
Author: Banji Lawal
Created: 2025-11-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# BISHOP_PERSONA_MISMATCH_EXCEPTION #======================#
    "BishopPersonaMismatchException",
]

from logic.rank import BishopDebugException


# ======================# BISHOP_PERSONA_MISMATCH_EXCEPTION #======================#
class BishopPersonaMismatchException(BishopDebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that a Bishop does not have the correct Persona.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        BishopDebugException
    """
    MSG = "There is a mismatch between the Bishop and its persona."
    ERR_CODE = "BISHOP_PERSONA_MISMATCH_EXCEPTION"

    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
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
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )

    





