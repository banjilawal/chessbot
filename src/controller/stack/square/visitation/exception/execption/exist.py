# src/logic/square/database/kernel/operation/token/exception/work/exist.py

"""
Module: logic.square.database.kernel.operation.token.work.exception.exist
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# VISIT_DESTINATION_NOT_FOUND_EXCEPTION #======================#
    "VisitDestinationNotFoundException",
]

from system import DebugException

# ======================# VISIT_DESTINATION_NOT_FOUND_EXCEPTION #======================#
class VisitDestinationNotFoundException(DebugException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the SquareStackDepartureWorker method identified in layer-0 of the exception chain.

    2.  A failing  UpdateResult was returned because a token wanted to occupy a square which does not exist in
        the SquareStack.

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
    ERR_CODE = "VISIT_DESTINATION_NOT_FOUND_EXCEPTION"
    MSG = "SquareVisit start failed: token wanted to visit square which does not exist."
    
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
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val,)

