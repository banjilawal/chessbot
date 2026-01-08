# src/chess/player/model/variety/variety.py

"""
Module: chess.player.model.variety.variety
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from enum import Enum, auto
from chess.agent import AgentVariety, HumanAgent, MachineAgent


class AgentVariety(Enum):
    """
    # ROLE: Selection

    # RESPONSIBILITIES:
    1.  Used for picking an operation that on the basis of the Player subclass.
    2.  Safer than using strings.

    # PARENT:
        *   Enum

    # PROVIDES:
        *   subclass_from_variety:  -> [HumanAgent|MachineAgent]

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    HUMAN_AGENT = auto(),
    MACHINE_AGENT = auto(),
    
    @classmethod
    def subclass_from_variety(cls, variety: AgentVariety) -> [HumanAgent|MachineAgent]:
        if variety == AgentVariety.HUMAN_AGENT:
            return HumanAgent
        return MachineAgent