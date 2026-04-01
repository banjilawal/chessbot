# src/logic/token/database/search/route/validator/transaction.py
"""
Module: logic.token.database.search.route.validator.transaction
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_QUERY_PARAMS_VALIDATION_FAILURE #======================#
    "TokenQueryParamsValidationException",
]

from logic.system import ValidationException


# ======================# TOKEN_QUERY_PARAMS_VALIDATION_FAILURE #======================#
class TokenQueryParamsValidationException(ValidationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that one of the params sent to the TokenSearchRouter did not
            pass a safety check.

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
    MSG = "TokenQueryRouting param failed a verification check."
    ERR_CODE = "TOKEN_QUERY_PARAMS_VALIDATION_FAILURE"
    
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
