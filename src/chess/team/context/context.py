# src/chess/team/context/context.py

"""
Module: chess.team.context.context
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.arena import Arena
from chess.agent import PlayerAgent
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
        *   player_agent (Optional[PlayerAgent])
        *   arena (Optional[Arena])
        *   color (Optional[ColorColor])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _arena: Optional[Arena] = None
    _player_agent: Optional[PlayerAgent] = None
    _color: Optional[GameColor] = None
    
    def __init__(
            self,
            id: Optional[int] = None,
            name: Optional[str] = None,
            arena: Optional[Arena] = None,
            player_agent: Optional[PlayerAgent] = None,
            color: Optional[GameColor] = None,
    ):
        method = "TeamContext.__init__"
        super().__init__(id=id, name=name)
        self._arena = arena
        self._player_agent = player_agent
        self._color = color
    
    @property
    def player_agent(self) -> Optional[PlayerAgent]:
        return self._player_agent
    
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
            "player_agent": self._player_agent,
            "color": self._color,
        }
