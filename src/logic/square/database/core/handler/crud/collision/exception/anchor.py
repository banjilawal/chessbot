from __future__ import annotations
from typing import Optional

___all__ = [
    # ======================# SQUARE_COLLISION_DETECTOR_EXCEPTION #======================#
    "SquareCollisionDetectorException",
]

from logic.system import AnchorException


# ======================# SQUARE_COLLISION_DETECTOR_EXCEPTION #======================#
class SquareCollisionDetectorException(AnchorException):
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
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])
        *   cls_mthd (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    CLS_MTHD = None
    CLS_NAME = "SquareCollisionDetector"
    ERR_CODE = "SQUARE_COLLISION_DETECTOR_EXCEPTION"
    MSG = "SquareCollisionDetector raised an exception."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None
    ):
        """
        Args:
            msg: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd
        )
