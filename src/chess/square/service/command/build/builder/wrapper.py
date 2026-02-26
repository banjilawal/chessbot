# src/chess/square/service/build/request/validator/wrapper.py

"""
Module: chess.square.service.build.request.validator.wrapper
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

__all__ = [
    # ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
    "SquareBuildCommandFabException",
]

from chess.system import BuilderException


# ======================# SQUARE_BUILD_REQUEST_FAILURE #======================#
class SquareBuildCommandFabException(BuilderException):
    """
    # ROLE: Error Method Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  An error occurred in SquareBuildRequestValidator.validate that, prevented a success
        result from being returned.

    # PARENT:
        *   ValidationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_BUILD_REQUEST_FAILED"
    MSG = "SquareBuildRequest validation failed."
    CLS_NAME = "ServiceRequestException"
    
    def __new__(cls, msg: str = MSG, ex: Exception | None = None):
        super().__init__()
    
    def __init__(self, msg: str = MSG, ex: Exception | None = None) -> None:
