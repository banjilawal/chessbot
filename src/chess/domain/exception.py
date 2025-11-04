# src/chess/domain/exception.py

"""
Module: chess.domain.exception
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
    'DomainTeamFieldIsNullException',
    'MissingDomainTreeException',
    'UnregisteredTeamMemberException',
    'DomainRosterNumberIsNullException',
    'DomainRankOutOfBoundsException',
    'DomainMissingDiscoveriesException',
    
    # ======================# NULL DOMAIN EXCEPTIONS #======================#
    'NullDomainException',
    'NullKingException',
    'NullCombatantException',
    
    # ======================# DOMAIN BUILD EXCEPTIONS #======================#  
    'DomainBuildFailedException',
]


class DomainException(ChessException):
    """
    Super class of all exceptions team Domain object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all domain exceptions
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
    Raised if `domain.positions` stack does not exist. If the `domain.positions == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "DOMAIN_MISSING_TREE_ERROR"
    DEFAULT_MESSAGE = "Domain has a null tree. The tree should never be null. There may be data inconsistency."


class DomainMissingDiscoveriesException(DomainException, InconsistencyException):
    """
    Raised if `domain.discovery` list does not exist. If the `domain.discoveries == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "DOMAIN_DISCOVERY_LIST_MISSING_ERROR"
    DEFAULT_MESSAGE = "Domain.discovery list is null. It should never be null. There may be service inconsistency or loss."


class UnregisteredTeamMemberException(DomainException):
    """Raised if team domain has its team set but the domain is not on the roster."""
    ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "The domain has assigned itself a team. but is not listed on that team's roster."


class DomainRosterNumberIsNullException(DomainException, NullException):
    """
    Raised a domain's roster number is null. This should never happen. the invariant roster number
    is set during build. If its null during validator there has been service loss or an inconsistency.
    """
    ERROR_CODE = "DOMAIN_NULL_ROSTER_NUMBER_ERROR"
    DEFAULT_MESSAGE = "A `Domain` object cannot have a null roster number. There may be service inconsistency or loss."


class DomainRankOutOfBoundsException(DomainException, NullException):
    """
    Raised a domain's rank is not a recognized chess rank
    """
    ERROR_CODE = "DOMAIN_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A `Domain` does not have a recognized chess rank."


# ======================# NULL DOMAIN EXCEPTIONS #======================#
class NullDomainException(DomainException, NullException):
    """
    Raised if an entity, method, or operation requires team domain but gets null instead.
    Domain is an abstract method. KingDomain and CombatantDomain are its subclasses.
    Do not throw NullAttackException. Raise NullKingDomain or NullCombatantDomain instead.
    they are more descriptive and better suited for debugging.
    """
    ERROR_CODE = "NULL_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "Domain cannot be null."


class NullKingException(NullDomainException):
    """
    Raised if team KingDomain is null. Raise NullCombatant instead of NullAttackException
    """
    ERROR_CODE = "NULL_KING_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "KingDomain cannot be null."


class NullCombatantException(NullDomainException):
    """
    Raised if team CombatantDomain is null. Raise NullCombatant instead of NullAttackException
    """
    ERROR_CODE = "NULL_COMBATANT_DOMAIN_ERROR"
    DEFAULT_MESSAGE = "CombatantDomain cannot be null."


# ======================# DOMAIN BUILD EXCEPTIONS #======================#  
class DomainBuildFailedException(DomainException, BuilderException):
    """
    Indicates Coord could not be built. Wraps and re-raises errors that occurred
    during build.
    """
    ERROR_CODE = "DOMAIN_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Domain build failed.."
