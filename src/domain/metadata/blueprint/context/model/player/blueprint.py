# src/domain/metadata/blueprint/context/model/player/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.player.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Game, ModelContextBlueprint, PlayerCategory, PlayerContext, Team
from err import PlayerContextNullException


class PlayerContextBlueprint(ModelContextBlueprint[PlayerContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an PlayerContext.
         
     Attributes:
        id: Optional[id]
        name: Optional[str]
        game: Optional[Game]
        wins: Option[bool]
        losses: Optional[bool]
        current_team: Optional[Team]
        player_category: Optional[PlayerCategory]
        
        domain_class: Type[PlayerContext]
        domain_null_exception: PlayerContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """
    
    _id: Optional[int]
    _name: Optional[str]
    _game: Optional[Game]
    _wins: Optional[bool]
    _losses: Optional[bool]
    _current_team: Optional[Team]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            game: Optional[Game] | None = None,
            wins: Optional[bool] | None = None,
            losses: Optional[bool] | None = None,
            current_team: Optional[Team] | None = None,
            player_category: Optional[PlayerCategory] | None = None,
            domain_class: Optional[Type[PlayerContext]] | None = None,
            domain_null_exception: Optional[PlayerContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            team: Optional[Team]
            game: Optional[Game]
            wins: Optional[bool]
            losses: Optional[bool]
            current_team: Optional[Team]
            player_category: Optional[PlayerCategory]
            domain_class: Type[PlayerContext]
            domain_null_exception: PlayerContextNullException
        """
        super().__init__(
            id=id,
            name=name,
            domain_class=domain_class or Type[PlayerContext],
            domain_null_exception=domain_null_exception or PlayerContextNullException(),
        )
        self._game = game
        self._wins = wins
        self._losses = losses
        self._current_team = current_team
        self._player_category = player_category
    
    @property
    def domain_class(self) -> Type[PlayerContext]:
        return cast(Type[PlayerContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> PlayerContextNullException:
        return  cast(PlayerContextNullException, super().domain_null_exception)
    
    @property
    def game(self) -> Optional[Game]:
        return self._game
    
    @property
    def wins(self) -> Optional[bool]:
        return self._wins
    
    @property
    def losses(self) -> Optional[bool]:
        return self._losses
    
    @property
    def current_team(self) -> Optional[Team]:
        return self._current_team
    
    @property
    def player_category(self) -> Optional[PlayerCategory]:
        return self._player_category
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "game": self._game,
            "wins": self._wins,
            "losses": self._losses,
            "current_team": self._current_team,
            "player_category": self._player_category,
        }
    
    
    
    
    


