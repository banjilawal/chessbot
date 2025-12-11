# src/chess/agent/validator/exception/registration/base.py

"""
Module: chess.agent.validator.exception.registration.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import InvalidAgentException
from chess.system import RegistrationException

__all__ = [
    #======================# AGENT REGISTRATION EXCEPTION SUPER CLASS #======================#
    "AgentRegistrationException",
]


#======================# AGENT_REGISTRATION EXCEPTION SUPER CLASS #======================#
class AgentRegistrationException(InvalidAgentException, RegistrationException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall Exception for when an Agent has set its owner correctly but the owner does not
        have the agent in its collection.

    # PARENT:
        *   InvalidAgentException
        *   RegistrationException

    # PROVIDES:
        *   gentRegistrationException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "AGENT_REGISTRATION_ERROR"
    DEFAULT_MESSAGE = "Agent not registered with parent."