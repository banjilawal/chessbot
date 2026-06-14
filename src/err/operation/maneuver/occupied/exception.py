# src/err/operation/maneuver/occupied/exception.py

"""
Module: err.operation.maneuver.occupied.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ManeuverException
from result import MethodResultType

__all__ = [
    # ======================# MANEUVER_DESTINATION_ALREADY_OCCUPIED #======================#
    "ManeuverDestinationOccupiedException",
]

# ======================# MANEUVER_DESTINATION_ALREADY_OCCUPIED #======================#
class ManeuverDestinationOccupiedException(ManeuverException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a token cannot maneuver because its destination is occupied.

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
        ManeuverException
    """
    MSG = "Cannot maneuver a token to a destination that is already occupied."
    ERR_CODE = "MANEUVER_DESTINATION_ALREADY_OCCUPIED"
    
    def __init__(
            self,
            msg: str = MSG,
            err_code: str = ERR_CODE,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
            Args:
            msg: str
            err_code: str
            var: Optional[str]
            val: Optional[Any]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            ex: Optional[Exception]
            mthd_rslt_type: Optional[MethodResultType]
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
            mthd_rslt_type=mthd_rslt_type,
        )
