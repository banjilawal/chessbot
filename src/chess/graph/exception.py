# src/chess/graph/exception.py

"""
Module: chess.graph.exception
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException, BuildFailedException

__all__ = [
    'GraphException',
    
    # ======================# GRAPH VALIDATION EXCEPTIONS #======================#
    'InvalidGraphException',

    
    # ======================# NULL GRAPH EXCEPTIONS #======================#
    'NullGraphException',

    
    # ======================# GRAPH BUILD EXCEPTIONS #======================#  
    'GraphBuildFailedException',
]



class GraphException(ChessException):
    """
    Super class of all exceptions team_name Graph object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all graph exceptions
    """
    ERROR_CODE = "GRAPH_ERROR"
    DEFAULT_MESSAGE = "Graph raised an exception."


# ======================# GRAPH VALIDATION EXCEPTIONS #======================#
class InvalidGraphException(GraphException, ValidationException):
    """Raised by GraphValidators if client fails validator."""
    ERROR_CODE = "GRAPH_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "GraphValidation failed."



# ======================# NULL GRAPH EXCEPTIONS #======================#
class NullGraphException(GraphException, NullException):
    """
    Raised if an entity, method, or operation requires team_name graph but gets null instead.
    Graph is an abstract method. KingGraph and CombatantGraph are its subclasses.
    Do not throw NullAttackException. Raise NullKingGraph or NullCombatantGraph instead.
    they are more descriptive and better suited for debugging.
    """
    ERROR_CODE = "NULL_GRAPH_ERROR"
    DEFAULT_MESSAGE = "Graph cannot be null."


# ======================# GRAPH BUILD EXCEPTIONS #======================#  
class GraphBuildFailedException(GraphException, BuildFailedException):
    """
    Indicates Coord could not be built. Wraps and re-raises errors that occurred
    during build.
    """
    ERROR_CODE = "GRAPH_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Graph build failed.."
