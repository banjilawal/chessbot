# src/chess/system/relation/exception/debug/register.py

"""
Module: chess.system.relation.exception.debug.register
Author: Banji Lawal
Created: 2025-11-26
version: 1.0.0
"""

__all__ = [
    # ======================# STALE_LINK EXCEPTION #======================#
    "StaleRelationException",
]

from chess.system import RelationDebugException


# ======================# STALE_LINK EXCEPTION #======================#
class StaleRelationException(RelationDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Indicate that, a failing result was returned because the primary had a stale link to a former
        satellite.
        
    # PARENT:
        *   RelationDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "STALE_LINK_ERROR"
    DEFAULT_MESSAGE = "The primary had a stale link to a former satellite."
