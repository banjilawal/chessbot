# src/logic/square/service/operation/validation/exception/registration/player.py

"""
Module: logic.square.service.operation.validation.exception.registration.player
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""
from typing import Any, Optional

from system import NotRegisteredException

__all__ = [
    # ======================# SQUARE_NOT_REGISTERED_WITH_BOARD_EXCEPTION #======================#
    "SquareBoardRegisteredException",
]


# ======================# SQUARE_NOT_REGISTERED_WITH_BOARD_EXCEPTION #======================#
class SquareBoardRegisteredException(NotRegisteredException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that SquareValidation failed because the square had not added itself
            to the board's squares.
            
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        NotRegisteredException
    """
    ERR_CODE = "SQUARE_NOT_REGISTERED_WITH_BOARD_EXCEPTION"
    MSG = "Square validation failed: The square had not registered with its board."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code = err_code,
        )