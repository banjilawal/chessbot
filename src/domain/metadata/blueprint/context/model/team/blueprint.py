# src/domain/metadata/blueprint/context/model/team/blueprint.py

"""
Module: domain.metadata.blueprint.context.model.team.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Any, Dict, Optional, Type, cast

from domain import Archetype, Board, ModelContextBlueprint, Player, TeamContext, TeamState
from err import TeamContextNullException


class TeamContextBlueprint(ModelContextBlueprint[TeamContext]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provide attributes for hydrating a TeamContext.
         
     Attributes:
        id: Optional[int]
        board: Optional[Board]
        player: Optional[Player]
        state: Optional[TeamState]
        archetype: Optional[Archetype]

        domain_class: Type[TeamContext]
        domain_null_exception: TeamContextNullException

     Provides:

     Super Class:
        ModelContextBlueprint
     """
    
    _board: Optional[Board]
    _owner: Optional[Player]
    _state: Optional[TeamState]
    _archetype: Optional[Archetype]

    
    def __init__(
            self,
            id: Optional[int] | None = None,
            board: Optional[Board] | None = None,
            player: Optional[Player] | None = None,
            state: Optional[TeamState] | None = None,
            archetype: Optional[Archetype] | None = None,
            domain_class: Optional[Type[TeamContext]] | None = None,
            domain_null_exception: Optional[TeamContextNullException] | None = None,
    ):
        """
        Args:
            board: Optional[Board]
            player: Optional[Player]
            state: Optional[TeamState]
            archetype: Optional[Archetype]
            domain_class: Type[TeamContext]
            domain_null_exception: TeamContextNullException
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[TeamContext],
            domain_null_exception=domain_null_exception or TeamContextNullException(),
        )
        self._board = board
        self._state = state
        self._owner = player
        self._archetype = archetype

    @property
    def domain_class(self) -> Type[TeamContext]:
        return cast(Type[TeamContext], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TeamContextNullException:
        return  cast(TeamContextNullException, super().domain_null_exception)
    
    @property
    def archetype(self) -> Optional[Archetype]:
        return self._archetype
    
    @property
    def player(self) -> Optional[Player]:
        return self._owner
    
    @property
    def board(self) -> Optional[Board]:
        return self._board
    
    @property
    def state(self) -> Optional[TeamState]:
        return self._state
    
    @property
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "board": self._board,
            "player": self._owner,
            "state": self._state,
            "archetype": self._archetype,
        }
    
    
    
    
    


