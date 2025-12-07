# src/chess/agent/model/variety.variety.py

"""
Module: chess.agent.model.variety.variety
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from enum import Enum, auto

class AgentVariety(Enum):
    """
    # ROLE: Selection

    # RESPONSIBILITIES:
    1.  Used for picking an operation that on the basis of the Agent subclass.
    2.  Safer than using strings.

    # PARENT
        *   Enum

    # PROVIDES:
    AgentVariety

    # ATTRIBUTES:
    None
    """
    HUMAN_AGENT = auto(),
    MACHINE_AGENT = auto(),