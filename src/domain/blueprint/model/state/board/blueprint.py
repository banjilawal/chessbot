# src/domain/bluprint/model/state/board/blueprint.py

"""
Module: domain.bluprint.model.state.board.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Arena, Board, BoardState, StateModelBlueprint, TeamBinder
from err import BoardNullException


class BoardBlueprint(StateModelBlueprint[Board]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Board object.

     Attributes:
        arena: Arena
        state: BoardState
        binder: TeamBinder
        
        domain_class: Type[Board]
        search_context_class: Type[BoardContext]
        domain_null_exception: BoardNullException
        id: Optional[int]

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _arena: Arena
    _validation_state: BoardState
    _binder: TeamBinder
    
    def __init__(
            self,
            arena: Arena,
            binder: TeamBinder,
            validation_state: Optional[BoardState] | None = None,
            domain_class: Optional[Type[Board]] | None = None,
            domain_null_exception: Optional[BoardNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            arena: Arena
            binder: TeamBinder
            validation_state: Optional[BoardState]
            domain_class: Optional[Type[Board]]
            domain_null_exception: Optional[BoardNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Board],
            domain_null_exception=domain_null_exception or BoardNullException(),
        )
        self._arena = arena
        self._binder = binder
        self._state = validation_state or BoardState.IS_EMPTY
        
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def binder(self) -> TeamBinder:
        return self._binder
    
    @property
    def validation_state(self) -> BoardState:
        return self._state
    
    @property
    def domain_class(self) -> Type[Board]:
        return cast(Type[Board], super().domain_class)
    
    @property
    def domain_null_exception(self) -> BoardNullException:
        return cast(BoardNullException, super().domain_null_exception)

    

