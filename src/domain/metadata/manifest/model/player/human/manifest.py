# src/domain/metadata/manifest/model/player/human/manifest.py

"""
Module: domain.metadata.manifest.model.player.human.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import (
    HumanPlayerNullGroup, HumanPlayer, HumanPlayerTypeUnion, PlayerManifest
)


class HumanPlayerManifest(PlayerManifest[HumanPlayer]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the HumanPlayer 
            security lifecycle.

     Attributes:
        types: HumanPlayerTypeUnion
        nulls: HumanPlayerNullGroup

     Provides:

     Super Class:
        PlayerManifest
     """
    
    def __init__(
            self,
            types: Optional[HumanPlayerTypeUnion] | None = None,
            nulls: Optional[HumanPlayerNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[HumanPlayerTypeUnion]
            nulls: Optional[HumanPlayerNullGroup]
        """
        super().__init__(
            types=types or HumanPlayerTypeUnion(),
            nulls=nulls or HumanPlayerNullGroup(),
        )
    
    @property
    def types(self) -> HumanPlayerTypeUnion:
        return cast(HumanPlayerTypeUnion, super().types)
    
    @property
    def nulls(self) -> HumanPlayerNullGroup:
        return cast(HumanPlayerNullGroup, super().nulls)