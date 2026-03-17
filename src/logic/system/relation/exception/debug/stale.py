# src/logic/system/relation/exception/debug/stale.py

"""
Module: logic.system.relation.exception.debug.stale
Author: Banji Lawal
Created: 2025-11-26
version: 1.0.0
"""

__all__ = [
    # ======================# STALE_RELATION_LINK EXCEPTION #======================#
    "StaleRelationException",
]

from logic.system import RelationDebugException


# ======================# STALE_RELATION_LINK EXCEPTION #======================#
class StaleRelationException(RelationDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that, a failing result was returned because the primary had a stale
        link to a former satellite

    Super Class:
        *   RelationDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "STALE_RELATION_LINK_EXCEPTION"
    MSG = "The primary had a stale link to a former satellite."
