# src/chess/agent/context/context.py

"""
Module: chess.agent.context.context
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.system import Context
from chess.agent import Agent, AgentVariety


class AgentContext(Context[Agent]):
    _team: Optional[Team] = None
    _variety: Optional[AgentVariety] = None
    
    def __init__(
            self,
            id: Optional[id] = None,
            name: Optional[str] = None,
            variety: Optional[AgentVariety] = None,
    ):
        super().__init__(id=id, name=name)
        self._variety = variety
    
    @property
    def variety(self) -> Optional[AgentVariety]:
        return self._variety
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "variety": self._variety,
        }
    