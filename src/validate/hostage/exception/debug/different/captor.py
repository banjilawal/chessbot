# src/logic/hostage/validation/exception/debug/different/board.py

"""
Module: logic.hostage.validation.exception.debug.different.board
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS EXCEPTION #======================#
    "PrisonerCapturedByDifferentEnemyException",
]

from model.hostage import HostageException


# ======================# VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS EXCEPTION #======================#
class PrisonerCapturedByDifferentEnemyException(HostageException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Indicate that a rank failed its Hostage validation because the prisoner had a different captor.

    Super Class:
        *   HostageException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "VICTOR_AND_PRISONER_ON_DIFFERENT_BOARDS_EXCEPTION"
    MSG = "Hostage validation failed: the prisoner was captured by a different friend."