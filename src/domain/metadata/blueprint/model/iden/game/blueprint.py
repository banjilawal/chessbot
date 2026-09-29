# src/domain/metadata/blueprint/model/iden/game/blueprint.py

"""
Module: domain.metadata.blueprint.model.iden.game.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import (
    Arena, CheckmateEncounter, Game, IdentifiableModelBlueprint, PlayerArchetypeBinder,
    StalemateEncounter
)
from err import GameNullException
from sync import TurnManagementService


class GameBlueprint(IdentifiableModelBlueprint[Game]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Game object.

     Attributes:
        arena: Arena
        binder: PlayerArchetypeBinder
        turn_service: TurnManagementService
        checkmate: Optional[CheckmateEncounter]
        stalemate: Optional[StalemateEncounter]
        

        domain_class: Type[Game]
        search_context_class: Type[GameContext]
        domain_null_exception: GameNullException

     Provides:

     Super Class:
        IdentifiableModelBlueprint
     """
    _arena: Arena
    _binder: PlayerArchetypeBinder
    _turn_service: TurnManagementService
    _checkmate: Optional[CheckmateEncounter]
    _stalemate: Optional[StalemateEncounter]

    def __init__(
            self,
            arena: Arena,
            binder: PlayerArchetypeBinder,
            checkmate: Optional[CheckmateEncounter] | None = None,
            stalemate: Optional[StalemateEncounter] | None = None,
            turn_service: Optional[TurnManagementService] | None = None,
            domain_class: Optional[Type[Game]] | None = None,
            domain_null_exception: Optional[GameNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            arena: Arena
            binder: PlayerArchetypeBinder
            checkmate: Optional[CheckmateEncounter]
            stalemate: Optional[StalemateEncounter]
            turn_service: Optional[TurnManagementService]
            domain_class: Optional[Type[Game]]
            domain_null_exception: Optional[GameNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Game],
            domain_null_exception=domain_null_exception or GameNullException(),
        )
        self._arena = arena
        self._binder = binder
        self._checkmate = checkmate
        self._stalemate = stalemate
        self._turn_service = turn_service or TurnManagementService()
    
    @property
    def arena(self) -> Arena:
        return self._arena
    
    @property
    def binder(self) -> PlayerArchetypeBinder:
        return self._binder
    
    @property
    def checkmate(self) -> Optional[CheckmateEncounter]:
        return self._checkmate
    
    @property
    def stalemate(self) -> Optional[StalemateEncounter]:
        return self._stalemate
    
    @property
    def turn_service(self) -> TurnManagementService:
        return self._turn_service
    
    @property
    def domain_class(self) -> Type[Game]:
        return cast(Type[Game], super().domain_class)
    
    @property
    def domain_null_exception(self) -> GameNullException:
        return cast(GameNullException, super().domain_null_exception)

