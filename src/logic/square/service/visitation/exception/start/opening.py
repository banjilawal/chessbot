# src/logic/square/service/visitation/exception/start/opening.py

"""
Module: logic.square.service.visitation.exception.start.opening
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

__all__ = [
    # ======================# VISITING_WRONG_OPENING_SQUARE EXCEPTION #======================#
    "VisitingWrongOpeningSquareException",
]

from logic.square import SquareDebugException


class VisitingWrongOpeningSquareException(SquareDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging
    
    Responsibilities:
    A Validation failure result was returned because a Token was trying to form on the wrong opening square.

    Super Class:
        *   SquareDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VISITING_WRONG_OPENING_SQUARE_EXCEPTION"
    MSG = "Visit validation failed: Token attempted forming on the wrong opening square."