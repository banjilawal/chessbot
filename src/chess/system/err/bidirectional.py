# src/chess/system/err/bidirectional.py

"""
Module: chess.system.err.bidirectional
Author: Banji Lawal
Created: 2025-11-21
version: 1.0.0
"""

from chess.system import ChessException

___all__ = [
#======================# BOUNDS EXCEPTION SUPER CLASS #======================#
    "BiDirectionalException",
]


#======================# BI_DIRECTIONAL RELATIONSHIP EXCEPTION SUPER CLASS #======================#
class BiDirectionalException(ChessException):
    """
    # INTRODUCTION:
    There is a subtle difference between bidirectional and registration exceptions.
    
    ## WHAT IS A BIDIRECTIONAL RELATIONSHIP?
    This is simply a relationship between two entities that does not involve a data set.
    The parties will have may have

    ## TYPES OF BIDIRECTIONAL RELATIONSHIPS:
        1.  A one-to-one relationship between the parties.
        
        2.  There is a one-to-many relationship between the parties but the
            one-side does not have a collection of the many-sides.
            
        3.  The owning side has a collection of some many-sides. But a
            particular instance of the many-side entity has its owner attribute
            set to someone else. That is
                many_side_entity.owner != owner
    
    ## TYPICAL USE CASES FOR BIDIRECTIONAL RELATIONSHIP:
    
    ### Aliveness:
        *   Verifying a transient relationship between an entity occupying another.
            The transient occupier needs to launch a transaction from the hosting
            entity.
        
        TYPICAL USE CASE: Verifying a Piece is active if it is occupying a Square.
    
    ### Finder Filtering
        *   Using the one-side to filter items in a many-sides by one-side along with
            some other unique attribute they all have with the shared attribute that
            at least one collection member has.
        
        TYPICAL USE CASE: Filtering Team datasets by Game (shared attribute) and
                        globally unique (id), or locally unique (name, color)
        
    ## WHAT IS A REGISTRATION RELATIONSHIP
    THere are two conditions.
        1.  many_side_entity.owner == owner
        2.  many_side_entity in owner.many_items_dataset.
        
    # ROLE: Error Tracing, Debugging
    
    # RESPONSIBILITIES:
    1.  Indicate if a required bidirectional relationship does not exist
    
    # PARENT:
        *   ChessException
        
    # PROVIDES:
    BiDirectionalException
    
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    DEFAULT_CODE = "NO_BI_DIRECTIONAL_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "There is no bidirectional relationship nor any connection between the entities."
