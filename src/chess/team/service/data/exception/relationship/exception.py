# src/chess/team/service/data/exception/relationship/exception.py

"""
Module: chess.team.service.data.exception.relationship.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""


from chess.system import BiDirectionalException

__all__ = [
    #======================# TEAM_RELATION EXCEPTION #======================#
    "TeamRelationshipException",
    
    #======================# TEAM_GAME_RELATIONSHIP EXCEPTION #======================#
    "NoTeamGameRelationshipException",
    
    #======================# TEAM_MISMATCHES_AGENT EXCEPTION #======================#
    "TeamMismatchesAgentException",
]


#======================# TEAM_RELATION EXCEPTION #======================#
class TeamRelationshipException(BiDirectionalException):
    """Catchall for Team relationship errors"""
    ERROR_CODE = "TEAM_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "No relationship found with Team."


#======================# TEAM_GAME_RELATIONSHIP EXCEPTION #======================#
class NoTeamGameRelationshipException(TeamRelationshipException):
    """Raised when Team.game != game"""
    ERROR_CODE = "NO_TEAM_GAME_RELATIONSHIP_ERROR"
    DEFAULT_MESSAGE = "There is no relationship between the Game and Team."


#======================# TEAM_MISMATCHES_AGENT EXCEPTION #======================#
class TeamMismatchesAgentException(TeamRelationshipException):
    """Raised when Team.player_agent != player_agent this is different"""
    ERROR_CODE = "TEAM_MISMATCHES_AGENT_ERROR"
    DEFAULT_MESSAGE = "Team has not assigned itself to the player_agent. Team.player_agent != player_agent."
