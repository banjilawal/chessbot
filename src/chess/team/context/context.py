# src/chess/team/map.py

"""
Module: chess.team.map
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from typing import Optional

from chess.team import Team
from chess.arena import Arena
from chess.player import Player
from chess.system import Context, GameColor


class TeamContext(Context[Team]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an TeamFinder with an attribute value to find Teams with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   player (Optional[Player])
        *   arena (Optional[Arena])
        *   color (Optional[ColorColor])

    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _arena: Optional[Arena] = None
    _player: Optional[Player] = None
    _color: Optional[GameColor] = None
    
    def __init__(
            self,
            id: Optional[int] = None,
            arena: Optional[Arena] = None,
            player: Optional[Player] = None,
            color: Optional[GameColor] = None,
    ):
        method = "TeamContext.__init__"
        super().__init__(id=id, name=None)
        self._arena = arena
        self._player = player
        self._color = color
    
    @property
    def player(self) -> Optional[Player]:
        return self._player
    
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
        # RETURNS:
            dict
        # RAISES:
        None
        """
        return {
            "id": self.id,
            "arena": self._arena,
            "player": self._player,
            "color": self._color,
        }
