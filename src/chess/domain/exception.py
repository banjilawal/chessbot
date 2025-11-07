# src/chess/owner/exception.py

"""
Module: chess.owner.exception
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, InconsistencyException, NullException, ValidationException
)

__all__ = [
    'DomainException',
    
    # ======================# DOMAIN VALIDATION EXCEPTIONS #======================#
    'InvalidDomainException',
    'DomainMissingTreeException',
    'CapturedDomainOwnerException',
    'CheckmatedKingDomainOwnerException',
    'PieceNotOnRosterDomainOwnerException',
    'InconsistenDomainAddressException',
    'RemovedPieceCannotOwnDomainException',
    
    # ======================# NULL DOMAIN EXCEPTIONS #======================#
    'NullDomainException',
    
    # ======================# DOMAIN BUILD EXCEPTIONS #======================#  
    'DomainBuildFailedException',
]


class DomainException(ChessException):
    """
    Super class of all exceptions team Domain object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all owner exceptions
    """
    ERROR_CODE = "DOMAIN_ERROR"
    DEFAULT_MESSAGE = "Domain raised an rollback_exception."


# ======================# DOMAIN VALIDATION EXCEPTIONS #======================#
class InvalidDomainException(DomainException, ValidationException):
    """Raised by DomainValidators if client fails validator."""
    ERROR_CODE = "DOMAIN_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Domain validator failed."

class DomainMissingTreeException(DomainException, InconsistencyException):
    """
    Raised if `owner.positions` stack does not exist. If the `owner.positions == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "DOMAIN_MISSING_TREE_ERROR"
    DEFAULT_MESSAGE = "Domain has a null tree. The tree should never be null. There may be data inconsistency."

class CapturedDomainOwnerException(DomainException):
    """
    Raised if `owner.discovery` list does not exist. If the `owner.discoveries == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "HOSTAGE_CANNOT_OWN_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "Domain.discovery list is null. It should never be null. There may be service inconsistency or loss."

class PieceNotOnRosterDomainOwnerException(DomainException):
    """Raised if team owner has its team set but the owner is not on the roster."""
    ERROR_CODE = "PIECE_NOT_ON_ROSTER_CANNOT_OWN_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "The owner has assigned itself a team. but is not listed on that team's roster."

class CheckmatedKingDomainOwnerException(DomainException):
    """
    Raised a owner's roster number is null. This should never happen. the invariant roster number
    is set during build. If its null during validator there has been service loss or an inconsistency.
    """
    ERROR_CODE = ""
    DEFAULT_MESSAGE = "A `Domain` object cannot have a null roster number. There may be service inconsistency or loss."

class InconsistenDomainAddressException(DomainException, InconsistencyException):
    """
    Raised a owner's rank is not a recognized chess rank
    """
    ERROR_CODE = "DOMAIN_ADDRESS_INCONSISTENCY_ERROR"
    DEFAULT_MESSAGE = "The owner address doest not match the owner's current position. There may inconsistent data."


# ======================# NULL DOMAIN EXCEPTIONS #======================#
class NullDomainException(DomainException, NullException):
    """
    Raised if an entity, method, or operation requires team owner but gets null instead.
    Domain is an abstract method. KingDomain and CombatantDomain are its subclasses.
    Do not throw NullAttackException. Raise NullKingDomain or NullCombatantDomain instead.
    they are more descriptive and better suited for debugging.
    """
    ERROR_CODE = "NULL_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "Domain cannot be null."


class RemovedPieceCannotOwnDomainException(DomainException):
    """
    Raised if team KingDomain is null. Raise NullCombatant instead of NullAttackException
    """
    ERROR_CODE = "REMOVED_PIECE_CANNOT_OWN_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "KingDomain cannot be null."



# ======================# DOMAIN BUILD EXCEPTIONS #======================#  
class DomainBuildFailedException(DomainException, BuilderException):
    """
    Indicates Coord could not be built. Wraps and re-raises errors that occurred
    during build.
    """
    ERROR_CODE = "DOMAIN_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Domain build failed.."
