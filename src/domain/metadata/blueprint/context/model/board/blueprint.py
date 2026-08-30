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
from domain import Arena, BoardSearchContext, ContextBlueprint, Team
from err import BoardContextNullException


class BoardContextBlueprint(ModelContextBlueprint[BoardSearchContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating an BoardSearchContext.
         
     Attributes:
        domain_class: Type[BoardSearchContext]
        domain_null_exception: BoardContextNullException
        id: Optional[int]
        arena: Optional[Arena]
        board: Optional[Board]
        team: Optional[Team]
        color: Optional[GameColor]

     Provides:

     Super Class:
        ModelContextBlueprint
     """
    _arena: Optional[Arena]
    _team: Optional[Team]
    _color: Optional[GameColor]
    
    def __init__(
            self,
            domain_class: Optional[Type[BoardSearchContext]] | None = None,
            domain_null_exception: Optional[BoardContextNullException] | None = None,
            id: Optional[int] | None = None,
            arena: Optional[Arena] | None = None,
            team: Optional[Team] | None = None,
            color: Optional[GameColor] | None = None,
    ):
        """
        Args:
            domain_class: Type[BoardSearchContext]
            domain_null_exception: BoardContextNullException
            arena: Optional[Arena]
            team: Optional[Team]
            color: Optional[GameColor]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[BoardSearchContext],
            domain_null_exception=domain_null_exception or BoardContextNullException(),
        )
        self._arena = arena
        self._color = color
        self._team = team
    
    @property
    def domain_class(self) -> Type[BoardSearchContext]:
        return cast(Type[BoardSearchContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> BoardContextNullException:
        return  cast(BoardContextNullException, super()._domain_null_exception)
    
    @property
    def arena(self) -> Optional[Arena]:
        return self._arena
    
    @property
    def team(self) -> Optional[Team]:
        return self._team
    
    @property
    def color(self) -> Optional[GameColor]:
        return self._color
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "arena": self._arena,
            "team": self._team,
            "color": self._color,
        }
    
    
    
    
    


