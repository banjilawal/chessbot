# src/domain/metadata/manifest/model/player/machine/manifest.py

"""
Module: domain.metadata.manifest.model.player.machine.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    MachinePlayerNullGroup, MachinePlayer, MachinePlayerTypeUnion, PlayerManifest
)


class MachinePlayerManifest(PlayerManifest[MachinePlayer]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the MachinePlayer 
            security lifecycle.

     Attributes:
        types: MachinePlayerTypeUnion
        nulls: MachinePlayerNullGroup

     Provides:

     Super Class:
        PlayerManifest
     """
    
    def __init__(
            self,
            types: Optional[MachinePlayerTypeUnion] | None = None,
            nulls: Optional[MachinePlayerNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[MachinePlayerTypeUnion]
            nulls: Optional[MachinePlayerNullGroup]
        """
        super().__init__(
            types=types or MachinePlayerTypeUnion(),
            nulls=nulls or MachinePlayerNullGroup(),
        )
    
    @property
    def types(self) -> MachinePlayerTypeUnion:
        return cast(MachinePlayerTypeUnion, super().types)
    
    @property
    def nulls(self) -> MachinePlayerNullGroup:
        return cast(MachinePlayerNullGroup, super().nulls)