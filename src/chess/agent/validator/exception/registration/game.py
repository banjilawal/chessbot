# src/chess/agent/validator/exception/registration/game.py

"""
Module: chess.agent.validator.exception.registration.game
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentRegistrationException


__all__ = [
    #======================# AGENT REGISTRATION EXCEPTION SUPER CLASS #======================#
    "AgentNotRegisteredWithGameException",
]




#======================# AGENT_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
class AgentNotRegisteredWithGameException(AgentRegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Agent has assigned itself to a Game instance, the Game has not
        registered the Agent as one of its two participants.
    2.  Raised if the agent.game == game but agent not in game.players

    # PARENT:
        *   AgentRegistrationException

    # PROVIDES:
    AgentNotRegisteredWithGameException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_NOT_REGISTERED_WITH_GAME_ERROR"
    DEFAULT_MESSAGE = (
        "Agent is not registered as one of the Game's participants. Only the Agent "
        "side of the relationship is set."
    )