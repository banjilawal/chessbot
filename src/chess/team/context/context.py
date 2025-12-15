# src/chess/team/context/context.py

"""
Module: chess.team.context.context
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.agent import Agent
from chess.arena import Arena
from chess.system import Context, GameColor


class TeamContext(Context[Team]):
    """
    # ROLE: Finder Filter

    # RESPONSIBILITIES:
    Provide an TeamFinder with an attribute value to find Teams with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   agent (Optional[Agent])
        *   arena (Optional[Arena])
        *   color (Optional[ColorColor])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _arena: Optional[Arena] = None
    _agent: Optional[Agent] = None
    _color: Optional[GameColor] = None
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            arena: Optional[Arena] = None,
            agent: Optional[Agent] = None,
            color: Optional[GameColor] = None,
    ):
        method = "TeamContext.__init__"
        super().__init__(id=id, name=name)
        self._arena = arena
        self._agent = agent
        self._color = color
    
    @property
    def agent(self) -> Optional[Agent]:
        return self._agent
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    def to_dict(self) -> dict:
        """
        # ACTION:
        Convert a TeamContext attributes into a dictionary.
    
        # PARAMETERS:
        None
    
        # Returns:
            dict
    
        # RAISES:
        None
        """
        return {
            "id": self.id,
            "name": self.name,
            "arena": self._arena,
            "agent": self._agent,
            "color": self._color,
        }
