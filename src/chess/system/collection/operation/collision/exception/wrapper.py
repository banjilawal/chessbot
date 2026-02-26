# src/chess/system/collection/operation/collision/exception/wrapper.py

"""
Module: chess.system.collection.operation.collision.exception.wrapper
Author: Banji Lawal
Created: 2026-02-21
Version: 1.0.0
"""
from typing import Optional

from chess.system import CollectionOperationException

__all__ = [
    # ======================# COLLISION_DETECTION_FAILURE #======================#
    "CollisionDetectionException",
]


# ======================# COLLISION_DETECTION_FAILURE #======================#
class CollisionDetectionException(CollectionOperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes why the collision detection operation was aborted.

    # PARENT:
        *   CollectionOperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    
    ERR_CODE = "COLLISION_DETECTION_FAILURE"
    MSG = "Collision detection failed."
    MTHD = "detect"
    OP_NAME = "CollisionDetection"
    RSLT = "CollisionReport"
    
    def __init__(
            self,
            rslt: Optional[str] = None,
            op_name: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        rslt = rslt or self.RSLT
        op_name = op_name or self.OP_NAME
        mthd = mthd or self.MTHD
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, rslt=rslt, mthd=mthd, op_name=op_name)