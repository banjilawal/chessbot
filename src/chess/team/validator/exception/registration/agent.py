# src/chess/team/validator/exception/registration/player_agent.py

"""
Module: chess.team.validator.exception.registration.player_agent
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import  TeamRegistrationException


__all__ = [
    #======================# TEAM_NOT_REGISTERED_WITH_AGENT EXCEPTION #======================#
    "TeamNotRegisteredWithAgentException"
]

#======================# TEAM_NOT_REGISTERED_WITH_AGENT EXCEPTION #======================#
class TeamNotRegisteredWithAgentException(TeamRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Team has assigned itself to an PlayerAgent instance, whe the PlayerAgent searches
        its team_assignments no match is found.
    2.  This should really be used to see if the team is the current_team because we want to use it to play.
    3.  That is team.player_agent == player_agent but player_agent.current_team != team.

    # PARENT:
        *   TeamRegistrationException

    # PROVIDES:
    TeamNotRegisteredWithAgentException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_AGENT_ERROR"
    DEFAULT_MESSAGE = (
        "Team is not registered in PlayerAgent.team_assignments. Only the team-side of the relationship is set."
    )