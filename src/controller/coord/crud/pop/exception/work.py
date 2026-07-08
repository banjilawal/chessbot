# src/logic/coord/database/kernel/operation/crud/pop/exception/empty.py

"""
Module: logic.coord.database.kernel.operation.crud.pop.exception.empty
Author: Banji Lawal
Created: 2026-03-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COORD_STACK_POP_FAILURE #======================#
    "CoordStackPopException",
]

from system import DeletionException

# ======================# COORD_STACK_POP_FAILURE #======================#
class CoordStackPopException(DeletionException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a CoordStackStack pop was unsuccessful.
        2.  Identify the CoordStackService method where the pop operation failed.
        
    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:
    
    Super Class:
        DeletionOperation
    """
    OP = "Deletion"
    MTHD_RSLT = "DeletionResult"
    ERR_CODE = "COORD_STACK_POP_FAILURE"
    MSG = "CoordStackService pop failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )