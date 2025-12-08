# src/chess/agent/validator/exception/registration/exception.py

"""
Module: chess.agent.validator.exception.registration.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentException
from chess.system import RegistrationException

__all__ = [
    # ======================# AGENT REGISTRATION EXCEPTION SUPER CLASS #======================#
    "AgentRegistrationException"
]


# ======================# AGENT_REGISTRATION EXCEPTION SUPER CLASS #======================#
class AgentRegistrationException(InvalidAgentException, RegistrationException):
    ERROR_CODE = "AGENT_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Agent not registered with parent."


# ======================# AGENT_NOT_REGISTERED_WITH_GAME EXCEPTION #======================#
class AgentNotRegisteredWithGameException(AgentRegistrationException):
    ERROR_CODE = "AGENT_NOT_REGISTERED_WITH_GAME_ERROR"
    DEFAULT_MESSAGE = (
        "Agent is not registered as one of the Game's participants. There is no relationship "
        "between them."
    )