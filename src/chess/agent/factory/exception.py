# src/chess/agent/factory/exception.py

"""
Module: chess.agent.factory.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentException
from chess.system import BuildFailedException

__all__ = [
    # ======================# AGENT BUILD EXCEPTIONS #======================#
    "AgentBuildFailedException",
]


# ======================# AGENT BUILD EXCEPTIONS #======================#
class AgentBuildFailedException(AgentException, BuildFailedException):
    """
    Catchall exception for when AgentFactory encounters an error building a new Agent instance.
    """
    ERROR_CODE = "AGENT_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "Agent build failed."