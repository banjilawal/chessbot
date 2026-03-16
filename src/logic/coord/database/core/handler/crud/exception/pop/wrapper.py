# src/logic/coord/database/core/handler/crud/exception/pop/wrapper.py

"""
Module: logic.coord.database.core.handler.crud.exception.pop.wrapper
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# POPPING_COORD_EXCEPTION #======================#
    "PoppingCoordException",
]
from logic.system import DeletionException


# ======================# POPPING_COORD_EXCEPTION #======================#
class PoppingCoordException(DeletionException):
    """
    # ROLE: Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a Coord deletion was unsuccessful.
    2.  Identify the method where the failure occurred.

    # PARENT:
        *   DeletionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DeletionException class for inherited attributes.

    # CONSTRUCTOR:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DeletionException class for inherited methods.
    """
    OP = "Deletion"
    RSLT_TYPE = "DeletionResult"
    ERR_CODE = "POPPING_COORD_EXCEPTION"
    MSG = "Popping a coord from the stack failed."
    
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