# src/chess/agent/validator/exception/registration/game.py

"""
Module: chess.agent.validator.exception.registration.game
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


from chess.agent import InvalidAgentException
from chess.system import RegistrationException


__all__ = [
    #======================# AGENT REGISTRATION EXCEPTION #======================#
    "AgentNotRegisteredWithGameException",
]




#======================# AGENT_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
class AgentNotRegisteredWithGameException(InvalidAgentException, RegistrationException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that while the Player has assigned itself to a Game instance, the Game has not
        registered the Player as one of its two participants.
    2.  Raised if the player_agent.game == game but player_agent not in game.players

    # PARENT:
        *   AgentRegistrationException

    # PROVIDES:
        *   AgentNotRegisteredWithGameException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_NOT_REGISTERED_WITH_GAME_ERROR"
    DEFAULT_MESSAGE = (
        "Player is not registered as one of the Game's participants. Only the Player "
        "side of the relationship is set."
    )