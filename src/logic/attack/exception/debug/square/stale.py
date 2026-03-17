# src/logic/attack/exception/debug/item/stale.py

"""
Module: logic.attack.exception.debug.item.stale
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKER_SOURCE_SQUARE_HAS_STALE_LINK EXCEPTION #======================#
    "StaleLinkDiscoveredInAttackingSquareSearchException",
]

from logic.attack import AttackDebugException


# ======================# ATTACKER_SOURCE_SQUARE_HAS_STALE_LINK EXCEPTION #======================#
class StaleLinkDiscoveredInAttackingSquareSearchException(AttackDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attack failed because one of the hits for the source

    Super Class:
        *   AttackDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ATTACKING_EMPTY_SQUARE_EXCEPTION"
    MSG = "Attack failed: The item was occupied by a stale."