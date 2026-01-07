# src/chess/player/map.py

"""
Module: chess.player.map
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from typing import Optional

from chess.game import Game
from chess.team import Team
from chess.system import Context
from chess.player import Player, PlayerVariety


class PlayerContext(Context[Player]):
    """
    # ROLE: Filter, Search, Selection, Reverse/Forward Lookups

    # RESPONSIBILITIES:
    Provide an PlayerFinder with an attribute value to find Players with a matching value in
    their version of the attribute.

    # PARENT:
        *   Context

    # PROVIDES:
        *   to_dict:    -> dict

    # LOCAL ATTRIBUTES:
        *   team (Optional[Team])
        *   game (Optional[Game])
        *   variety (Optional[PlayerVariety])
        
    # INHERITED ATTRIBUTES:
        *   See Context class for inherited attributes.
    """
    _team: Optional[Team]
    _game: Optional[Game]
    _variety: Optional[PlayerVariety]
    
    def __init__(
            self,
            id: Optional[id] = None,
            name: Optional[str] = None,
            team: Optional[Team] = None,
            game: Optional[Game] = None,
            variety: Optional[PlayerVariety] = None,
    ):
        """
        # ACTION:
        Constructor

        # PARAMETERS:
            *   id (Optional[int])
            *   designation (Optional[str])
            *   team (Optional[Team])
            *   game (Optional[Game])
            *   variety (Optional[PlayerVariety])

        # RETURNS:
        None

        # RAISES:
        None
        """
        super().__init__(id=id, name=name)
        self._team = team
        self._game = game
        self._variety = variety
        
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def variety(self) -> Optional[PlayerVariety]:
        return self._variety
    
    def to_dict(self) -> dict:
        """
        # Convert the PlayerContext object to a dictionary.

        # PARAMETERS:
        None

        # RETURNS:
        dict

        # RAISES:
        None
        """
        return {
            "id": self.id,
            "designation": self.name,
            "team": self._team,
            "game": self._game,
            "variety": self._variety,
        }
    