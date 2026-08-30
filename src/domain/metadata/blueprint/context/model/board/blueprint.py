# src/domain/metadata/blueprint/context/model/board/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import Arena, BoardContext, BoardState, ModelContextBlueprint, Team
from err import BoardContextNullException


class BoardContextBlueprint(ModelContextBlueprint[BoardContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a BoardContext.
         
     Attributes:
        id: Optional[int]
        team: Optional[Team]
        arena: Optional[Arena]
        state: Optional[BoardState]
        color: Optional[GameColor]
        
        domain_class: Type[BoardContext]
        domain_null_exception: BoardContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """
    
    _team: Optional[Team]
    _arena: Optional[Arena]
    _state: Optional[BoardState]
    _team_color: Optional[GameColor]
    
    def __init__(
            self,
            id: Optional[int] | None = None,
            team: Optional[Team] | None = None,
            arena: Optional[Arena] | None = None,
            state: Optional[BoardState] | None = None,
            team_color: Optional[GameColor] | None = None,
            domain_class: Optional[Type[BoardContext]] | None = None,
            domain_null_exception: Optional[BoardContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            team: Optional[Team]
            arena: Optional[Arena]
            state: Optional[BoardState]
            team_color: Optional[GameColor]
            domain_class: Type[BoardContext]
            domain_null_exception: BoardContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[BoardContext],
            domain_null_exception=domain_null_exception or BoardContextNullException(),
        )
        self._team = team
        self._state = state
        self._arena = arena
        self._team_color = team_color

    
    @property
    def domain_class(self) -> Type[BoardContext]:
        return cast(Type[BoardContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> BoardContextNullException:
        return  cast(BoardContextNullException, super().domain_null_exception)
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def state(self) -> Optional[BoardState]:
        return self._state
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def team_color(self) -> Optional[GameColor]:
        return self._team_color
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "team": self._team,
            "state": self._state,
            "arena": self._arena,
            "color": self._team_color,
        }
    
    
    
    
    


