# src/chess/graph/exception.py

"""
Module: chess.graph.exception
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from chess.system import ChessException, NullException, ValidationException, BuildFailedException

__all__ = [
    'DomainException',
    
    # ======================# DOMAIN VALIDATION EXCEPTIONS #======================#
    'InvalidDomainException',

    
    # ======================# NULL DOMAIN EXCEPTIONS #======================#
    'NullDomainException',

    
    # ======================# DOMAIN BUILD EXCEPTIONS #======================#  
    'DomainBuildFailedException',
]



class DomainException(ChessException):
    """
    Super class of all exceptions team_name Domain object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all graph exceptions
    """
    ERROR_CODE = "DOMAIN_ERROR"
    DEFAULT_MESSAGE = "Domain raised an exception."


# ======================# DOMAIN VALIDATION EXCEPTIONS #======================#
class InvalidDomainException(DomainException, ValidationException):
    """Raised by DomainValidators if client fails validator."""
    ERROR_CODE = "DOMAIN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "DomainValidation failed."



# ======================# NULL DOMAIN EXCEPTIONS #======================#
class NullDomainException(DomainException, NullException):
    """
    Raised if an entity, method, or operation requires team_name graph but gets null instead.
    Domain is an abstract method. KingDomain and CombatantDomain are its subclasses.
    Do not throw NullAttackException. Raise NullKingDomain or NullCombatantDomain instead.
    they are more descriptive and better suited for debugging.
    """
    ERROR_CODE = "NULL_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "Domain cannot be null."


# ======================# DOMAIN BUILD EXCEPTIONS #======================#  
class DomainBuildFailedException(DomainException, BuildFailedException):
    """
    Indicates Coord could not be built. Wraps and re-raises errors that occurred
    during build.
    """
    ERROR_CODE = "DOMAIN_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Domain build failed.."
