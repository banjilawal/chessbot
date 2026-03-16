# src/logic/persona/exception/debug.py

"""
Module: logic.persona.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# PERSONA_DEBUG_EXCEPTION #======================#
    "PersonaDebugException",
]

from logic.system import DebugException

# ======================# PERSONA_DEBUG_EXCEPTION #======================#
class PersonaDebugException(DebugException):
    """
    # ROLE: Capture Error Variable State, Exception Chain Layer 2, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        err_code: Optional[str]
        ex: Optional[Exception]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "PERSONA_EXCEPTION"
    MSG = str = "Persona had an error."

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
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, var=var, val=val, err_code=err_code,)

