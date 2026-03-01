# src/logic/system/searcher/collision/exception.py

"""
Module: logic.system.searcher.collision.exception
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""



from logic.system.resolution  import ResolutionException







__all__ = [

    
    #======================# SEARCH_COLLISION EXCEPTION #======================#
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


    # RELATED EXCEPTION
        *   AttackException
        *   CastlingException
        *   CheckmateException
        *   HostageException
        *   NullException
        *   PromotionException
        *   RosterException
        *   TravelException
    """
    ERR_CODE = "RESOLUTION_FAILED_EXCEPTION"
    MSG = "The resolution process failed to break the attribute conflict."










