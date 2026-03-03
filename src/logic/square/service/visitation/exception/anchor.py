# src/logic/square/service/visitation/exception/anchor.py

"""
Module: logic.square.service.visitation.exception.anchor
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_VISIT_HANDLER_EXCEPTION #======================#
    "TokenVisitHandlerException",
]

from logic.system import AnchorException

# ======================# TOKEN_VISIT_HANDLER_EXCEPTION #======================#
class TokenVisitHandlerException(AnchorException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Indicate that an error occurred in a TokenVisitHandler.

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

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    CLS_MTHD = None
    CLS_NAME = "TokenVisitHandler"
    ERR_CODE = "TOKEN_VISIT_HANDLER_EXCEPTION"
    MSG = " TokenVisitHandler raised an exception."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        cls_mthd = cls_mthd or self.CLS_MTHD
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name, cls_mthd=cls_mthd)

__all__ = [
    # ======================# TOKEN_VISIT_HANDLER_EXCEPTION #======================#
    "PoppingEmptySquareStackException",
]

from logic.system import DebugException


# ======================# TOKEN_VISIT_HANDLER_EXCEPTION #======================#
class PoppingEmptySquareStackException(DebugException):
    """
    # ROLE: Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the TokenVisitHandler method identified in layer-0 of the exception chain.

    1.  Indicate a failure occurred in TokenVisitHandler.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val (Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "TOKEN_VISIT_HANDLER_EXCEPTION"
    MSG = "TokenVisitHandler raised an exception."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: str
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val,)


__all__ = [
    # ======================# TOKEN_VISIT_HANDLER_EXCEPTION #======================#
    "TokenVisitHandlerException",
]

from logic.system import AnchorException


# ======================# TOKEN_VISIT_HANDLER_EXCEPTION #======================#
class TokenVisitHandlerException(AnchorException):
    """"
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:


    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
