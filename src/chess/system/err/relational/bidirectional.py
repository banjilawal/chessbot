# src/chess/system/err/bidirectional.py

"""
Module: chess.system.err.bidirectional
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import ChessException

___all__ = [
    # ======================# BI_DIRECTIONAL RELATIONSHIP EXCEPTION #======================#
    "NoBidirectionalRelationshipException",
]


#======================# BI_DIRECTIONAL RELATIONSHIP EXCEPTION #======================#
class NoBidirectionalRelationshipException(ChessException):
    """
    # ROLE: Error Tracing, Debugging
    
    # RESPONSIBILITIES:
    1.  Indicate that a required bidirectional relationship does not exist.
    
    # PARENT:
        *   ChessException
        
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "MISSING_BIDIRECTIONAL_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "There is no bidirectional relationship nor any connection between the entities."
