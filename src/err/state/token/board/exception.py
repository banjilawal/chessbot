# src/err/state/token/board/exception.py

"""
Module: err.state.token.board.exception
Author: Banji Lawal
Created: 2026-04-07
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from err import TokenStateException
from result import MethodResultType


__all__ = [
    # ======================# TOKEN_BOARD_STATE_INCONSISTENCY_ERROR #======================#
    "TokenBoardConsistencyStateException",
]

# ======================# TOKEN_BOARD_STATE_INCONSISTENCY_ERROR #======================#
class TokenBoardConsistencyStateException(TokenStateException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a TokenBoardState value did not match a Token's existence on the Board.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        TokenStateException
    """
    MSG = "Token.board_state is not consistent with the token's existence on the board."
    ERR_CODE = "TOKEN_BOARD_STATE_INCONSISTENCY_ERROR"
    
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
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
