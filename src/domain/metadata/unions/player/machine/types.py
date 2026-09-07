# src/domain/metadata/unions/player/machine/types.py

"""
Module: domain.metadata.unions.player.machine.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import MachineBlueprint, MachinePlayer, PlayerTypeUnion
from transit import MachineCarrier


class MachineTypeUnion(PlayerTypeUnion[MachinePlayer]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a MachinePlayer.

    Attributes:
        model: Type[MachinePlayer]
        carrier: Type[MachineCarrier]
        blueprint: Type[MachineBlueprint]

    Provides:

    Super Class:
        PlayerTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[MachinePlayer]] | None = None,
            carrier: Optional[Type[MachineCarrier]] | None = None, 
            blueprint: Optional[Type[MachineBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[MachinePlayer]]
            carrier: Optional[Type[MachineCarrier]
            blueprint: Optional[Type[MachineBlueprint] 
        """
        super().__init__(
            model=model or MachinePlayer,
            carrier=carrier or MachineCarrier, 
            blueprint=blueprint or MachineBlueprint
        )
    
    @property
    def model(self) -> Type[MachinePlayer]:
        return cast(Type[MachinePlayer], super().model)
    
    @property
    def carrier(self) -> Type[MachineCarrier]:
        return cast(Type[MachineCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[MachineBlueprint]:
        return cast(Type[MachineBlueprint], super().blueprint)