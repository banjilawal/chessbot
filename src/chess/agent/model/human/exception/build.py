# src/chess/agent/model/human/exception/build.py

"""
Module: chess.agent.model.human.exception.build
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.agent import AgentBuildFailedException, HumanAgent

__all__ = [
    # ======================# HUMAN_AGENT EXCEPTION #======================#
    "HumanAgentBuildFailedException",
]


# ======================# HUMAN_AGENT BUILD EXCEPTIONS #======================#
class HumanAgentBuildFailedException(HumanAgent, AgentBuildFailedException):
    """
    # ROLE:

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during HumanAgent build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an HumanAgentBuilder method.

    # PARENT
        *   HumanAgentException
        *   AgentBuildFailedException

    # PROVIDES:
    HumanAgentBuildFailedException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "HUMAN_AGENT_BUILD_ERROR"
    DEFAULT_MESSAGE = "HumanAgent build failed."
