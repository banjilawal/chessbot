# src/chess/team/validator/exception/registration/game

"""
Module: chess.team.validator.exception.registration.game
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamRegistrationException

__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
    "TeamNotRegisteredWithGameException"
]

# ======================# TEAM_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
class TeamNotRegisteredWithGameException(TeamRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Team has assigned itself to a Game instance but indirect checks
        using the team.game == agent.current_game is false.

    # PARENT:
        *   TeamRegistrationException

    # PROVIDES:
    TeamNotRegisteredWithGameException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_NOT_REGISTERED_WITH_GAME_ERROR"
    DEFAULT_MESSAGE = (
        "Team is not registered with the current Game. There may inconsistencies between the "
        "game and team assigned to a player."
    )

