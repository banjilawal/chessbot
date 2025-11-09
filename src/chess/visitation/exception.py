# src/chess/visitation/exception.py

"""
Module: chess.graph.visitation.exception
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, InconsistencyException, NullException, ValidationException
)

__all__ = [
    'VisitationEventException',
    
    # ======================# VISITATION VALIDATION EXCEPTIONS #======================#
    'InvalidVisitationEventException',
    'VisitationTeamFieldIsNullException',
    'VisitationMissingCoordStackException',
    'UnregisteredTeamMemberException',
    'VisitationRosterNumberIsNullException',
    'VisitationRankOutOfBoundsException',
    'VisitationMissingDiscoveriesException',
    
    # ======================# NULL VISITATION EXCEPTIONS #======================#
    'NullVisitationEventException',
    'NullKingException',
    'NullCombatantException',
    
    # ======================# VISITATION BUILD EXCEPTIONS #======================#  
    'VisitationBuildFailedException',
]


class VisitationEventException(ChessException):
    """
    Super class of all exceptions team Visitationation object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all visitationation exceptions
    """
    ERROR_CODE = "VISITATION_ERROR"
    DEFAULT_MESSAGE = "Visitationation raised an rollback_exception."


# ======================# VISITATION VALIDATION EXCEPTIONS #======================#
class InvalidVisitationEventException(VisitationEventException, ValidationException):
    """Raised by VisitationValidators if client fails validator."""
    ERROR_CODE = "VISITATION_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "Visitationation validator failed."


class VisitationTeamFieldIsNullException(VisitationEventException, InconsistencyException):
    """
    Raised if `visitationation.team` is null. Might indicate a consistency or build problem because `Visitationation.team` should
    never be null.
    """
    ERROR_CODE = "VISITATION_TEAM_FIELD_NULL_ERROR"
    DEFAULT_MESSAGE = "Visitationation.team consistency is null. It should never be null. There may be service inconsistency."


class VisitationMissingCoordStackException(VisitationEventException, InconsistencyException):
    """
    Raised if `visitationation.positions` stack does not exist. If the `visitationation.positions == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "VISITATION_COORD_STACK_MISSING_ERROR"
    DEFAULT_MESSAGE = "Visitationation.positions list is null. It should never be null. There may be service inconsistency or loss."


class VisitationMissingDiscoveriesException(VisitationEventException, InconsistencyException):
    """
    Raised if `visitationation.discovery` list does not exist. If the `visitationation.discoveries == null there is service inconsistency
    or loss.
    """
    ERROR_CODE = "VISITATION_DISCOVERY_LIST_MISSING_ERROR"
    DEFAULT_MESSAGE = "Visitationation.discovery list is null. It should never be null. There may be service inconsistency or loss."


class UnregisteredTeamMemberException(VisitationEventException):
    """Raised if team visitationation has its team set but the visitationation is not on the roster."""
    ERROR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
    DEFAULT_MESSAGE = "The visitationation has assigned itself a team. but is not listed on that team's roster."


class VisitationRosterNumberIsNullException(VisitationEventException, NullException):
    """
    Raised a visitationation's roster number is null. This should never happen. the invariant roster number
    is set during build. If its null during validator there has been service loss or an inconsistency.
    """
    ERROR_CODE = "VISITATION_NULL_ROSTER_NUMBER_ERROR"
    DEFAULT_MESSAGE = "A `Visitationation` object cannot have a null roster number. There may be service inconsistency or loss."


class VisitationRankOutOfBoundsException(VisitationEventException, NullException):
    """
    Raised a visitationation's bounds is not a recognized chess bounds
    """
    ERROR_CODE = "VISITATION_RANK_OUT_OF_BOUNDS_ERROR"
    DEFAULT_MESSAGE = "A `Visitationation` does not have a recognized chess bounds."


# ======================# NULL VISITATION EXCEPTIONS #======================#
class NullVisitationEventException(VisitationEventException, NullException):
    """
    Raised if an entity, method, or operation requires team visitationation but gets null instead.
    Visitationation is an abstract method. KingVisitation and CombatantVisitation are its subclasses.
    Do not throw NullAttackException. Raise NullKingVisitation or NullCombatantVisitation instead.
    they are more descriptive and better suited for debugging.
    """
    ERROR_CODE = "NULL_VISITATION_ERROR"
    DEFAULT_MESSAGE = "Visitationation cannot be null."


class NullKingException(NullVisitationEventException):
    """
    Raised if team KingVisitation is null. Raise NullCombatant instead of NullAttackException
    """
    ERROR_CODE = "NULL_KING_VISITATION_ERROR"
    DEFAULT_MESSAGE = "KingVisitation cannot be null."


class NullCombatantException(NullVisitationEventException):
    """
    Raised if team CombatantVisitation is null. Raise NullCombatant instead of NullAttackException
    """
    ERROR_CODE = "NULL_COMBATANT_VISITATION_ERROR"
    DEFAULT_MESSAGE = "CombatantVisitation cannot be null."


# ======================# VISITATION BUILD EXCEPTIONS #======================#  
class VisitationBuildFailedException(VisitationEventException, BuilderException):
    """
    Indicates Coord could not be built. Wraps and re-raises errors that occurred
    during build.
    """
    ERROR_CODE = "VISITATION_BUILD_FAILED_ERROR"
    DEFAULT_MESSAGE = "Visitationation build failed.."
