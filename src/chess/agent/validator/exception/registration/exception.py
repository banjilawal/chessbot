# src/chess/agent/validator/exception/registration/exception.py

"""
Module: chess.agent.validator.exception.registration.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentException
from chess.system import RegistrationException

__all__ = ["AgentRegistrationException"]


class AgentRegistrationException(InvalidAgentException, RegistrationException):
    ERROR_CODE = "AGENT_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Agent not registered with parent."
