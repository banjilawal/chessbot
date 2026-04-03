# src/logic/token/service/operation/arithmetic/convert/exception/validator.py

"""
Module: logic.token.service.operation.arithmetic.convert.exception.work
Author: Banji Lawal
Created: 2026-03-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional
# src/logic/coord/validation/exception/validator.py

"""
Module: logic.coord.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# VECTOR_COORD_UNION_VALIDATION_FAILURE #======================#
    "VectorCoordUnionValidatorException",
]

from logic.system import ValidationException


# ======================# VECTOR_COORD_UNION_VALIDATION_FAILURE #======================#
class VectorCoordUnionValidatorException(ValidationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Identify which VectorCoordUnionValidator method, a test failed.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super Class:
        ValidationException
    """
    ERR_CODE = "VECTOR_COORD_UNION_VALIDATION_FAILURE"
    MSG = "VectorCoordUnion validation check failed."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            title=title,
            err_code=err_code,
            rslt_type=rslt_type,
        )