# src/logic/coord/database/core/handler/crud/exception/push/wrapper.py

"""
Module: logic.coord.database.core.handler.crud.exception.push.wrapper
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PUSHING_COORD_EXCEPTION #======================#
    "PushingCoordException",
]

from logic.system import InsertionException


# ======================# PUSHING_COORD_EXCEPTION #======================#
class PushingCoordException(InsertionException):
    """
    # ROLE: Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a Coord insertion was unsuccessful.
    2.  Identify the method where the failure occurred.

    # PARENT:
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See InsertionException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See InsertionException class for inherited methods.
    """
    OP = "Insertion"
    RSLT_TYPE = "InsertionResult"
    ERR_CODE = "PUSHING_COORD_EXCEPTION"
    MSG = "Pushing a coord from the stack failed."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )
