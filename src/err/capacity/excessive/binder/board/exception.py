# src/err/capacity/excessive/binder/board/exception.py

"""
Module: err.capacity.excessive.binder.board.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from err import ColorBinderOverCapacityException

_all_ = [
    # ======================# BOARD_TEAM_COLOR_BINDER_OVER_CAPACITY #======================#
    "BoardTeamBinderOverCapacityException",
]
# ======================# BOARD_TEAM_COLOR_BINDER_OVER_CAPACITY #======================#
class BoardTeamColorBinderOverCapacityException(
    ColorBinderOverCapacityException
):
    """
    Role:
        - Error Tracing

    Responsibilities:
        1.  Indicating a required BoardTeamColorBinder is over its capacity.

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
        BinderOverCapacityException
    """
    MSG = "BoardTeamColorBinder is over its capacity."
    ERR_CODE = "BOARD_TEAM_COLOR_BINDER_OVER_CAPACITY"
    
    def _init_(
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
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: Optional[Exception]
            cls_name: Optional[Str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super()._init_(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt_type=mthd_rslt_type,
        )
