# src/logic/system/collision/exception/wrapper.py

"""
Module: logic.system.collision.exception.wrapper
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# COLLISION_DETECTION_FAILURE #======================#
    "CollisionDetectionException",
]

from logic.system import CollectionOperationException


# ======================# COLLISION_DETECTION_FAILURE #======================#
class CollisionDetectionException(CollectionOperationException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes why the collision detection operation was aborted.

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
        *   See WrapperException class for inherited methods.
    """
    ERR_CODE = "COLLISION_DETECTION_FAILURE"
    MSG = "Collision detection failed."
    MTHD = "detect"
    OP_NAME = "CollisionDetection"
    RSLT = "CollisionDetectionResult"
    
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