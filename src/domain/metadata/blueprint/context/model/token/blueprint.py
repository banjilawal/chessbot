# src/domain/metadata/blueprint/context/model/token/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import (
    Coord, Formation, HomeSquare, ModelContextBlueprint, Rank, Team, TokenActivityState, TokenContext
)
from err import TokenContextNullException


class TokenContextBlueprint(ModelContextBlueprint[TokenContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an TokenContext.
         
     Attributes:
        id: Optional[int]
        name: Optional[str]
        team: Optional[Team]
        rank: Optional[Rank]
        ransom: Optional[int]
        color: Optional[GameColor]
        current_position:Optional[Coord]
        home_square: Optional[HomeSquare]
        formation: Optional[Formation]
        activity_state: Optional[TokenActivityState]
        
        domain_class: Type[TokenContext]
        domain_null_exception: TokenContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """
    _id: Optional[int]
    _name: Optional[str]
    _rank: Optional[Rank]
    _team: Optional[Team]
    _ransom: Optional[int]
    _color: Optional[GameColor]
    _formation: Optional[Formation]
    _current_position: Optional[Coord]
    _home_square: Optional[HomeSquare]
    _activity_state: Optional[TokenActivityState]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            name: Optional[str] | None = None,
            rank: Optional[Rank] | None = None,
            team: Optional[Team] | None = None,
            ransom: Optional[int] | None = None,
            color: Optional[GameColor] | None = None,
            formation: Optional[Formation] | None = None,
            current_position: Optional[Coord] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            activity_state: Optional[TokenActivityState] | None = None,
            domain_class: Optional[Type[TokenContext]] | None = None,
            domain_null_exception: Optional[TokenContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            name: Optional[str]
            team: Optional[Team]
            rank: Optional[Rank]
            ransom: Optional[int]
            color: Optional[GameColor]
            current_position:Optional[Coord]
            home_square: Optional[HomeSquare]
            domain_class: Type[TokenContext]
            activity_state: Optional[TokenActivityState]
            domain_null_exception: TokenContextNullException
        """
        super().__init__(
            id=id,
            name=name,
            domain_class=domain_class or Type[TokenContext],
            domain_null_exception=domain_null_exception or TokenContextNullException(),
        )
        self._rank = rank
        self._team = team
        self._color = color
        self._ransom = ransom
        self._formation = formation
        self._home_square = home_square
        self._activity_state = activity_state
        self._current_position = current_position
    
    @property
    def domain_class(self) -> Type[TokenContext]:
        return cast(Type[TokenContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TokenContextNullException:
        return  cast(TokenContextNullException, super().domain_null_exception)
    
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def ransom(self) -> Optional[int]:
        return self._ransom
    
    @property
    def formation(self) -> Optional[Formation]:
        return self._formation
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def home_square(self) -> Optional[HomeSquare]:
        return self._home_square
    
    @property
    def activity_state(self) -> Optional[TokenActivityState]:
        return self._activity_state
    
    @property
    def current_position(self) -> Optional[Coord]:
        return self._current_position
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "team": self._team,
            "rank": self._rank,
            "color": self._color,
            "ransom": self._ransom,
            "formation": self._formation,
            "home_square": self._home_square,
            "current_position": self._current_position,
        }
    
    
    
    
    


