# src/logic/pair/schema/exception/deletion/exist.py

"""
Module: logic.pair.schema.exception.deletion.exist
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# PAIR_DESTINATION_NOT_FOUND_EXCEPTION #======================#
    "PairNotFoundException",
]

from system import DebugException


# ======================# PAIR_DESTINATION_NOT_FOUND_EXCEPTION #======================#
class PairNotFoundException(DebugException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the PairStack method identified in layer-0 of the exception chain.

    2.  A failing Result was returned because a pair the client needs was not found.

    Super Class:
        *   DebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val (Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "PAIR_DESTINATION_NOT_FOUND_EXCEPTION"
    MSG = "Pair was not found."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
    ):
        """
        Args:
            msg: str
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val, )