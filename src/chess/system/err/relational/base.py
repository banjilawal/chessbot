# src/chess/system/err/relational/base.py

"""
Module: chess.system.err.relational.base
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ChessException

___all__ = [
    # ======================# NO_RELATIONSHIP EXCEPTION #======================#
    "NoRelationshipException",
]


#======================# NO_RELATIONSHIP EXCEPTION #======================#
class NoRelationshipException(ChessException):
    """
    # ROLE: Error Tracing, Debugging, Catchall
    
    # RESPONSIBILITIES:
    1.  Indicate that a relationship that is required between entities does not exist.
    
    # PARENT:
        *   ChessException
        
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "NO_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "Relationship raised an exception."
