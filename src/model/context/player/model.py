# src/model/context/player/model.py

"""
Module: model.context.player.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations


class PlayerContext(Context[Player]):
    """
    Role:
        -   Selection
        -   Routing mask
        -   Data-Holder

    Responsibilities:
        1.  Supply a Player attribute-value tuple which selects an execution path.

    Attributes:
        id: Optional[int]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        current_position:Optional[Coord]
        designation: Optional[str]
        color: Optional[GameColor]
        opening_square_name: Optional[str]

    Provides:
        -   to_dict() -> Dict[str, Any]

    Super Class:
        Context
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
        Raises:
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
        Raises:
            None
        """
        return {
            "id": self.id,
            "designation": self.designation,
            "team": self._team,
            "game": self._game,
            "variety": self._variety,
        }
    