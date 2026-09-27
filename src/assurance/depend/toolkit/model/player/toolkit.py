# src/assurance/depend/toolkit/model/player/toolkit.py

"""
Module: assurance.depend.toolkit.model.player.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, PlayerWrapperDependency
from domain import Player, PlayerManifest, PlayerNullGroup, PlayerTypeUnion


class PlayerValidatorToolkit(ModelValidatorToolkit[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Player attribute validators and type metadata.

    Attributes:
        helper: PlayerManifest
        metadata: PlayerHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[PlayerManifest] | None = None,
            wrapper: Optional[PlayerWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[PlayerManifest]
            metadata: Optional[PlayerHelperTable]
        """
        super().__init__(
            wrapper=wrapper or PlayerWrapperDependency(),
            metadata=metadata or PlayerManifest(),
        )
    
    @property
    def wrapper(self) -> PlayerWrapperDependency:
        return cast(PlayerWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> PlayerManifest:
        return cast(PlayerManifest, super().metadata)
    
    @property
    def nulls(self) -> PlayerNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> PlayerTypeUnion:
        return self.metadata.types