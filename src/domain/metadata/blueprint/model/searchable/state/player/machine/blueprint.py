# src/domain/metadata/blueprint/model/searchable/state/player/machine/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.player.machine.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import MachinePlayer, PlayerBlueprint
from err import MachineNullException
from game import GameAdviser


class MachineBlueprint(PlayerBlueprint):
    """
    Role:
        1.  Metadata
    
    Responsibilities:
        1.  Provides values for hydrating a MachinePlayer object.
    
    Attributes:
        name: str
        adviser: Optional[GameAdviser]
        id: Optional[int]
        
        domain_class: Type[MachinePlayer]
        domain_null_exception: MachineNullException
    
    Provides:
    
    Super Class:
        PlayerBlueprint
    """
    
    def __init__(self,
            name: str,
            adviser: Optional[GameAdviser] | None = None,
            domain_class: Optional[Type[MachinePlayer]] | None = None,
            domain_null_exception: Optional[MachineNullException] | None = None,
            id: Optional[int] | None = None,
        ):
        """
        Args:
            name: str
            adviser: Optional[GameAdviser]
            domain_class: Optional[Type[MachinePlayer]]
            domain_null_exception: Optional[MachineNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            name=name,
            adviser=adviser,
            domain_class=domain_class or MachinePlayer,
            domain_null_exception=domain_null_exception or MachineNullException(),
        )
        

    @property
    def domain_class(self) -> Type[MachinePlayer]:
        return cast(Type[MachinePlayer], super().domain_class)
    
    @property
    def domain_null_exception(self) -> MachineNullException:
        return cast(MachineNullException, super().domain_null_exception)