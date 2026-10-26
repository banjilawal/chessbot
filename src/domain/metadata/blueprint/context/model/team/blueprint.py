# src/domain/metadata/blueprint/context/model/team/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from config import GameColor
from domain import Archetype, Board,  ContextBlueprint, Player, TeamContext
from err import TeamContextNullException


class TeamContextBlueprint(ContextBlueprint[TeamContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a TeamContext.
         
     Attributes:
        id: Optional[int]
        board: Optional[Board]
        owner: Optional[Player]
        state: Optional[TeamState]
        color: Optional[GameColor]
        archetype: Optional[Archetype]

        domain_class: Type[TeamContext]
        domain_null_exception: TeamContextNullException

     Provides:

     Super Class:
        ContextBlueprint
     """
    _board: Optional[Board]
    _owner: Optional[Player]
    _archetype: Optional[Archetype]

    
    def __init__(
            self,
            id: Optional[int] | None = None,
            board: Optional[Board] | None = None,
            owner: Optional[Player] | None = None,
            archetype: Optional[Archetype] | None = None,
            domain_class: Optional[Type[TeamContext]] | None = None,
            domain_null_exception: Optional[TeamContextNullException] | None = None,
    ):
        """
        Args:
            id: Optional[int]
            board: Optional[Board]
            owner: Optional[Player]
            archetype: Optional[Archetype
            domain_class: Type[TeamContext]
            domain_null_exception: TeamContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[TeamContext],
            domain_null_exception=domain_null_exception or TeamContextNullException(),
        )
        self._board = board
        self._owner = owner
        self._archetype = archetype
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def owner(self) -> Optional[Player]:
        return self._owner
    
    @property
    def archetype(self) -> Optional[Archetype]:
        return self._archetype

    @property
    def domain_class(self) -> Type[TeamContext]:
        return cast(Type[TeamContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TeamContextNullException:
        return  cast(TeamContextNullException, super().domain_null_exception)
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self._board,
            "owner": self._owner,
            "archetype": self._archetype,
        }
    
    
    
    
    


