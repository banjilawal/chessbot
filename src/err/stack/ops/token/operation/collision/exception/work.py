# src/logic/token/database/kernel/operation/collision/exception/debug/designation.py

"""
Module: logic.token.database.kernel.operation.collision.exception.debug.designation
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_COLLISION_DETECTOR_FAILURE #======================#
    "TokenCollisionDetectionException",
]

from system import RelationAnalysisException

# ======================# TOKEN_COLLISION_DETECTOR_FAILURE #======================#
class TokenCollisionDetectionException(RelationAnalysisException):
    """
    Role: 
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that the TokenCollisionAnalyst encountered an error. It did not run the collision tests.

    Super:
        TokenDebugException

    Provides:
    
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]        
    """
    ERR_CODE = "TOKEN_COLLISION_DETECTOR_FAILURE"
    MSG = "TokenCollisionAnalyst encountered an error. no collision tests were run."
    
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