# src/chess/attack/exception/debug/item/stale.py

"""
Module: chess.attack.exception.debug.item.stale
Author: Banji Lawal
Created: 2026-01-24
version: 1.0.0
"""

__all__ = [
    # ======================# ATTACKER_SOURCE_SQUARE_HAS_STALE_LINK EXCEPTION #======================#
    "StaleLinkDiscoveredInAttackingSquareSearchException",
]

from chess.attack import AttackDebugException


# ======================# ATTACKER_SOURCE_SQUARE_HAS_STALE_LINK EXCEPTION #======================#
class StaleLinkDiscoveredInAttackingSquareSearchException(AttackDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attack failed because one of the hits for the source

    # PARENT:
        *   AttackDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ATTACKING_EMPTY_SQUARE_ERROR"
    DEFAULT_MESSAGE = "Attack failed: The item was occupied by a stale."