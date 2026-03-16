# src/logic/token/database/core/operation/crud/collision/exception/wrapper.py

"""
Module: logic.token.database.core.operation.crud.collision.exception.wrapper
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

___all__ = [
    # ======================# TOKEN_COLLIDER_DETECTED #======================#
    "TokenColliderException",
]

from logic.system import ColliderException


# ======================# TOKEN_COLLIDER_DETECTED #======================#
class TokenColliderException(ColliderException):
    """
    # ROLE: Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a token collided with the test subject
    2.  Identify the method where the collision test was performed.

    # PARENT:
        *   ColliderException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ColliderException class for inherited attributes.

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
        *   See ColliderException class for inherited methods.
    """
    OP_NAME = "CollisionDetection"
    RSLT_TYPE = "CollisionReport"
    ERR_CODE = "TOKEN_COLLIDER_DETECTED"
    MSG = "Another Token collided with the test subject."
    
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
 

