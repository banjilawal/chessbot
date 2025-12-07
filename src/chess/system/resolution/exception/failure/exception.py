# src/chess/system/searcher/collision/base.py

"""
Module: chess.system.searcher.collision.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""



from chess.system.resolution  import ResolutionException







__all__ = [

    
    # ======================# SEARCH_COLLISION EXCEPTIONS #======================#
    'ResolutionFailedException',
    'ResolvingIDConflictFailedException',
    'SearchNameCollisionException',
    'ResolvingCoordConflictFailedException',
    
    'SquareSearchIdCollisionException',
    'SquareSearchNameCollisionException',
    'SquareSearchCoordCollisionException',
    
    'TeamSearchIdCollisionException'
]


class ResolutionFailedException(ResolutionException):
    """
    # RESPONSIBILITY
    Raised when searching with a globally unique attribute like an id and
    the resolution process shows the entity is a orphan


    # RELATED EXCEPTIONS
        *   AttackException
        *   CastlingException
        *   CheckmateException
        *   HostageException
        *   NullException
        *   PromotionException
        *   RosterException
        *   TravelException
    """
    ERROR_CODE = "RESOLUTION_FAILED_ERROR"
    DEFAULT_MESSAGE = "The resolution process failed to break the attribute conflict."










