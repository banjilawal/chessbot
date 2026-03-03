# src/logic/square/service/visitation/exception/start/add.py

"""
Module: logic.square.service.visitation.exception.start.add
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# START_SQUARE_VISIT_FAILURE #======================#
    "StartSquareVisitException",
]

from logic.system import UpdateException

# ======================# START_SQUARE_VISIT_FAILURE #======================#
class StartSquareVisitException(UpdateException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Identify the SquareStackService method where the push failed.
    
    2.  An error occurred in SquareStackTokenHandler.add_occupant that prevented a successful UpdateResult.
    3.  This error might have occurred in a different SquareStackTokenHandler method that also returns UpdateResults.

    # PARENT:
        *   UpdateException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See UpdateException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See UpdateException class for inherited methods.
    """
    OP = "Update"
    MTHD = Optional[None]
    RSLT_TYPE = "UpdateResult"
    MSG = "SquareVisit start failed."
    ERR_CODE = "START_SQUARE_VISIT_FAILURE"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
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