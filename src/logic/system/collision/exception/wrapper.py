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
    # ======================# COLLIDER_DETECTED #======================#
    "ColliderException",
]

from logic.system import OperationException


# ======================# COLLIDER_DETECTED #======================#
class ColliderException(OperationException):
    """
    # ROLE: Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate an object collided test subject
    2.  Identify the method where the collision test was performed.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See OperationException class for inherited attributes.

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
        *   See OperationException class for inherited methods.
    """
    OP_NAME = "CollisionDetection"
    RSLT_TYPE = "CollisionReport"
    ERR_CODE = "COLLIDER_DETECTED"
    MSG = "Collider ran into test subject."
    
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