# src/err/null/binder/board/exception.py

"""
Module: err.null.binder.board.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations

from err import BinderNullException

__all__ = [
    # ======================# BOARD_TEAM_BINDER_NULL_EXCEPTION #======================#
    "BoardTeamBinderNullException",
]
# ======================# BOARD_TEAM_BINDER_NULL_EXCEPTION #======================#
class BoardTeamBinderNullException(BinderNullException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a required BoardTeamBinder is null.

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
        BinderNullException
    """
    MSG = "BoardTeamBinder cannot be null."
    ERR_CODE = "BOARD_TEAM_BINDER_NULL_EXCEPTION"
    
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
