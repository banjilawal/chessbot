from __future__ import annotations
from typing import Optional

___all__ = [
    # ======================# SQUARE_COLLISION_DETECTION_EXCEPTION #======================#
    "SquareCollisionDetectionException",
]

from logic.system import CollisionDetectionException


# ======================# SQUARE_COLLISION_DETECTION_EXCEPTION #======================#
class SquareCollisionDetectionException(CollisionDetectionException):
    """
    # ROLE: Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Provide SquareCollisionDetector as:
            *   Reporting
            *   Coverage
        target for layer-2 debugging exceptions.
    2.  Indicate which SquareCollisionDetector method received a worker's
        (layer-1) failure result.

    # PARENT:
        *   CollisionDetectionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See CollisionDetectionException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See CollisionDetectionException class for inherited methods.
    """
    MTHD = None
    OP = "CollisionDetection"
    RSLT_TYPE = "CollisionDetectionResult"
    ERR_CODE = "SQUARE_COLLISION_DETECTION_EXCEPTION"
    MSG = "SquareCollisionDetection raised an exception."
    
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
            msg: Optional[str]
            mthd: Optional[str]
            ex Optional[Exception]
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
