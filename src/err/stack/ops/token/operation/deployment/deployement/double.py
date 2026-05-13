# src/logic/token/service/exception/deployment/state.py

"""
Module: logic.token.service.exception.deployment.state
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_STACK_ALREADY_DEPLOYED_EXCEPTION #======================#
    "TokenStackAlreadyDeployedException",
]

from model.token import TokenDebugException

# ======================# TOKEN_STACK_ALREADY_DEPLOYED_EXCEPTION #======================#
class TokenStackAlreadyDeployedException(TokenDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a token_stack has already been deployed on the board.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        TokenDebugException
    """
    ERR_CODE = "TOKEN_STACK_ALREADY_DEPLOYED_EXCEPTION"
    MSG = "The token schema has already been deployed."
    
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