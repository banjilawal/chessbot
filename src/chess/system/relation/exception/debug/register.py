# src/chess/system/relation/exception/debug/register.py

"""
Module: chess.system.relation.exception.debug.register
Author: Banji Lawal
Created: 2025-11-26
version: 1.0.0
"""

__all__ = [
    # ======================# NOT_REGISTERED EXCEPTION #======================#
    "NotRegisteredException",
]

from chess.system import RelationDebugException


# ======================# NOT_REGISTERED EXCEPTION #======================#
class NotRegisteredException(RelationDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging
    
    # INTRODUCTION:
        Indicate that the owning side of a one-to-many is broken. The many side knows its owner from its owner
        attribute. If the owner does not find the many_instance in its collection there item is not registered
        with the owner. Raised when Entity.owner == owner but the Owner does not find the item in its dataset.
    
    # RESPONSIBILITIES:
    1.  Indicate that, a failing result was returned because the satellite has not registered itself with its
        primary.
        
    # PARENT:
        *   RelationDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NOT_REGISTERED_EXCEPTION"
    MSG = "The satellite has not registered itself with its primary"
