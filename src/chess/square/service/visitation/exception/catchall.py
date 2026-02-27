# src/chess/square/service/visitation/exception/super.py

"""
Module: chess.square.service.visitation.exception.super
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""


__all__ = [
    # ======================# TOKEN_VISIT_HANDLER EXCEPTION #======================#
    "TokenVisitHandlerException",
]

from chess.system import AnchorException


# ======================# TOKEN_VISIT_HANDLER EXCEPTION #======================#
class TokenVisitHandlerException(AnchorException):
    """"
    # ROLE: Class/Module Identifier, Exception Chain Layer 3, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate a failure occurred in TokenVisitHandler.
    2.  The method where the error occurred is identified in the exception nested directly underneath.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TOKEN_VISIT_HANDLER_ERROR"
    MSG = "TokenVisitHandler raised an exception."