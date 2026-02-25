# src/chess/neighbor/collision.py

"""
Module: chess.graph.neighbor.exception
Author: Banji Lawal
Created: 2025-11-03
version: 1.0.0
"""

from chess.system import (
    ChessException, BuilderException, InconsistencyException, NullException, ValidationException
)

__all__ = [
    'VisitationEventException',
    
    #======================# VISITATION VALIDATION EXCEPTION #======================#
    'InvalidVisitationEventException',
    'VisitationTeamFieldIsNullException',
    'VisitationMissingCoordStackException',
    'UnregisteredTeamMemberException',
    'VisitationRosterNumberIsNullException',
    'VisitationRankOutOfBoundsException',
    'VisitationMissingDiscoveriesException',
    
    #======================# NULL VISITATION EXCEPTION #======================#
    'NullVisitationEventException',
    'NullKingException',
    'NullCombatantException',
    
    #======================# VISITATION BUILD EXCEPTION #======================#
    'VisitationBuildException',
]


class VisitationEventException(ChessException):
    """
    Super class of all exception team_name Visitationation object raises. Do not use directly. Subclasses
    give details useful for debugging. This class exists primarily to allow catching
    all visitationation exception
    """
    ERR_CODE = "VISITATION_ERROR"
    MSG = "Visitationation raised an exception."


#======================# VISITATION VALIDATION EXCEPTION #======================#
class InvalidVisitationEventException(VisitationEventException, ValidationException):
    """Raised by VisitationValidators if client fails coord_stack_validator."""
    ERR_CODE = "VISITATION_VALIDATION_ERROR"
    MSG = "Visitationation validation failed."


class VisitationTeamFieldIsNullException(VisitationEventException, InconsistencyException):
    """
    Raised if `visitationation.team_name` is validation. Might indicate a consistency or builder problem because `Visitationation.team_name` should
    never be validation.
    """
    ERR_CODE = "VISITATION_TEAM_FIELD_NULL_ERROR"
    MSG = "Visitationation.team_name consistency is validation. It should never be validation. There may be entity_service inconsistency."


class VisitationMissingCoordStackException(VisitationEventException, InconsistencyException):
    """
    Raised if `visitationation.positions` stack does not exist. If the `visitationation.positions == validation there is entity_service inconsistency
    or loss.
    """
    ERR_CODE = "VISITATION_COORD_STACK_MISSING_ERROR"
    MSG = "Visitationation.positions list is validation. It should never be validation. There may be entity_service inconsistency or loss."


class VisitationMissingDiscoveriesException(VisitationEventException, InconsistencyException):
    """
    Raised if `visitationation.discovery` list does not exist. If the `visitationation.discoveries == validation there is entity_service inconsistency
    or loss.
    """
    ERR_CODE = "VISITATION_DISCOVERY_LIST_MISSING_ERROR"
    MSG = "Visitationation.discovery list is validation. It should never be validation. There may be entity_service inconsistency or loss."


class UnregisteredTeamMemberException(VisitationEventException):
    """Raised if team_name visitationation has its team_name set but the visitationation is not on the roster."""
    ERR_CODE = "UNREGISTERED_TEAM_MEMBER_ERROR"
    MSG = "The visitationation has assigned itself a team_name. but is not listed on that team_name's roster."


class VisitationRosterNumberIsNullException(VisitationEventException, NullException):
    """
    Raised a visitationation's roster number is validation. This should never happen. the invariant roster number
    is set during builder. If its validation during coord_stack_validator there has been entity_service loss or an inconsistency.
    """
    ERR_CODE = "VISITATION_NULL_ROSTER_NUMBER_ERROR"
    MSG = "A `Visitationation` object cannot have a validation roster number. There may be entity_service inconsistency or loss."


class VisitationRankOutOfBoundsException(VisitationEventException, NullException):
    """
    Raised a visitationation's bounds is not a recognized chess bounds
    """
    ERR_CODE = "VISITATION_RANK_OUT_OF_BOUNDS_ERROR"
    MSG = "A `Visitationation` does not have a recognized chess bounds."


#======================# NULL VISITATION EXCEPTION #======================#
class NullVisitationEventException(VisitationEventException, NullException):
    """
    Raised if an entity, method, or operation requires team_name visitationation but gets validation instead.
    Visitationation is an abstract method. KingVisitation and CombatantVisitation are its subclasses.
    Do not throw NullAttackException. Raise NullKingVisitation or NullCombatantVisitation instead.
    they are more descriptive and better suited for debugging.
    """
    ERR_CODE = "NULL_VISITATION_ERROR"
    MSG = "Visitationation cannot be null."


class NullKingException(NullVisitationEventException):
    """
    Raised if team_name KingVisitation is validation. Raise NullCombatant instead of NullAttackException
    """
    ERR_CODE = "NULL_KING_VISITATION_ERROR"
    MSG = "KingVisitation cannot be null."


class NullCombatantException(NullVisitationEventException):
    """
    Raised if team_name CombatantVisitation is validation. Raise NullCombatant instead of NullAttackException
    """
    ERR_CODE = "NULL_COMBATANT_VISITATION_ERROR"
    MSG = "CombatantVisitation cannot be null."


#======================# VISITATION BUILD EXCEPTION #======================#
class VisitationBuildException(VisitationEventException, BuilderException):
    """
    Indicate That  Coord could not be built. Wraps and re-raises errors that occurred
    during builder.
    """
    ERR_CODE = "VISITATION_BUILD_FAILED"
    MSG = "Visitationation build failed."
