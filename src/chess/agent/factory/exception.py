# src/chess/agent/factory/exception.py

"""
Module: chess.agent.factory.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentContextException
from chess.system import BuildFailedException

__all__ = [
    # ======================# AGENT_CONTEXT BUILD EXCEPTIONS #======================#
    "AgentBuildFailedException",
]


# ======================# AGENT_CONTEXT BUILD EXCEPTIONS #======================#
class AgentBuildFailedException(AgentContextException, BuildFailedException):
    """
    Catchall exception for when AgentFactory encounters an error building a new Agent instance.
    """
    ERROR_CODE = "AGENT_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "Agent build failed."