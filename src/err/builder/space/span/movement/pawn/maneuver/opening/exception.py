# src/err/builder/space/span/setter/pawn/maneuver/exception.py

"""
Module: err.builder.space.span.movement.pawn.maneuver.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import PawnManeuverVectorSetException
from result import MethodResultType

__all__ = [
    # ======================# PAWN_OPENING_MANEUVER_VECTOR_SET_ERROR #======================#
    "OpeningPawnManeuverVectorSetException",
]

# ======================# PAWN_OPENING_MANEUVER_VECTOR_SET_ERROR #======================#
class OpeningPawnManeuverVectorSetException(PawnManeuverVectorSetException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
         1.  Indicate that a PawnOpeningManeuverVectorSet instance encountered an error.
        
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
        PawnManeuverVectorSetException
    """
    MSG = "An error occurred with a PawnOpeningManeuverVectorSet."
    ERR_CODE = "PAWN_OPENING_MANEUVER_VECTOR_SET_ERROR"

    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
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
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt_type
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
