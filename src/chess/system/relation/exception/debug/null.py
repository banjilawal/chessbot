# src/chess/system/relation/exception/debug/null.py

"""
Module: chess.system.relation.exception.debug.null
Author: Banji Lawal
Created: 2025-11-26
version: 1.0.0
"""

___all__ = [
    # ======================# NO_RELATIONSHIP EXCEPTION #======================#
    "NoRelationException",
]

from chess.system import RelationDebugException


#======================# NO_RELATIONSHIP EXCEPTION #======================#
class NoRelationException(RelationDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that, a failing result was returned because the candidates did not have any relationship

    # PARENT:
        *   RelationDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "NO_RELATIONSHIP_EXCEPTION"
    MSG = "The candidates do not have any relationship."
