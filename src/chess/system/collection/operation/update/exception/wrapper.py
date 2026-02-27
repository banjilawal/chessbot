# src/chess/system/collection/operation/update/exception/wrapper.py

"""
Module: chess.system.collection.operation.update.exception.wrapper
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# UPDATE_FAILURE #======================#
    "UpdateException",
]

from chess.system import CollectionOperationException

# ======================# UPDATE_FAILURE #======================#
class UpdateException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes the cause the update failed.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See CollectionException class for inherited attributes.

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
        *   See WorkerException class for inherited methods.
    """
    ERR_CODE = "UPDATE_FAILURE"
    MSG = "Update failed."
    MTHD = "update"
    OP_NAME = "update"
    RSLT = "UpdateResult"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)