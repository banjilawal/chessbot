# src/logic/hostage/validator/exception/debug/different/item.py

"""
Module: logic.hostage.validator.exception.debug.different.item
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_SQUARE EXCEPTION #======================#
    "PrisonerCapturedOnDifferentSquareException",
]

from logic.hostage import HostageException


# ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_SQUARE EXCEPTION #======================#
class PrisonerCapturedOnDifferentSquareException(HostageException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that a candidate failed its Hostage validation because the victor and prisoner were on
        different item.

    # PARENT:
        *   HostageException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VICTOR_AND_PRISONER_ON_DIFFERENT_SQUARE_EXCEPTION"
    MSG = "Hostage validation failed: The victor can only capture enemies on its own item."