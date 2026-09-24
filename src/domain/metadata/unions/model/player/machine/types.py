# src/domain/metadata/unions/model/player/machine/types.py

"""
Module: domain.metadata.unions.player.machine.types
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import MachinePlayerBlueprint, MachinePlayer, PlayerTypeUnion
from transit import MachinePlayerCarrier


class MachinePlayerTypeUnion(PlayerTypeUnion[MachinePlayer]):
    """
    Role:
        - Metadata

    Responsibilities:
        1.  Catalog of types associated with building and validating a
            MachinePlayer.

    Attributes:
        model: Type[MachinePlayer]
        carrier: Type[MachinePlayerCarrier]
        blueprint: Type[MachinePlayerBlueprint]

    Provides:

    Super Class:
        PlayerTypeUnion
    """
    
    def __init__(
            self, 
            model: Optional[Type[MachinePlayer]] | None = None,
            carrier: Optional[Type[MachinePlayerCarrier]] | None = None, 
            blueprint: Optional[Type[MachinePlayerBlueprint]] | None = None,
    ):
        """
        Args:
            model: Optional[Type[MachinePlayer]]
            carrier: Optional[Type[MachinePlayerCarrier]
            blueprint: Optional[Type[MachinePlayerBlueprint] 
        """
        super().__init__(
            model=model or MachinePlayer,
            carrier=carrier or MachinePlayerCarrier, 
            blueprint=blueprint or MachinePlayerBlueprint
        )
    
    @property
    def model(self) -> Type[MachinePlayer]:
        return cast(Type[MachinePlayer], super().model)
    
    @property
    def carrier(self) -> Type[MachinePlayerCarrier]:
        return cast(Type[MachinePlayerCarrier], super().carrier)
    
    @property
    def blueprint(self) -> Type[MachinePlayerBlueprint]:
        return cast(Type[MachinePlayerBlueprint], super().blueprint)