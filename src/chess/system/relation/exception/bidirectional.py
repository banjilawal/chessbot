# src/chess/system/err/relational/bidirectional.py

"""
Module: chess.system.err.relational.bidirectional
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import NoRelationshipException

___all__ = [
# ======================# NO_BIDIRECTIONAL_RELATIONSHIP EXCEPTION #======================#
    "NoBidirectionalRelationException",
]



#======================# NO_BIDIRECTIONAL_RELATIONSHIP EXCEPTION #======================#
class NoBidirectionalRelationException(NoRelationshipException):
    """
    # ROLE: Error Tracing, Debugging
    
    # RESPONSIBILITIES:
    1.  Indicate that a required bidirectional relationship between two entities does not exist.
    
    # PARENT:
        *   NoRelationshipException
        
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "NO_BIDIRECTIONAL_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "There is no bidirectional relationship between the entities."
