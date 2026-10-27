# src/assurance/depend/toolkit/model/player/toolkit.py

"""
Module: assurance.depend.toolkit.model.player.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, PlayerServiceDependency
from domain import (
    Player, PlayerManifest, PlayerNullWarningSet, PlayerLayer
)

class PlayerLayerToolkit(ModelLayerToolkit[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Player attribute validators and type manifest.

    Attributes:
        helper: PlayerManifest
        manifest: PlayerServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[PlayerManifest] | None = None,
            dependency: Optional[PlayerServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[PlayerManifest]
            manifest: Optional[PlayerServiceDependency]
        """
        super().__init__(
            dependency=dependency or PlayerServiceDependency(),
            manifest=manifest or PlayerManifest(),
        )
    
    @property
    def dependency(self) -> PlayerServiceDependency:
        return cast(PlayerServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> PlayerManifest:
        return cast(PlayerManifest, super().manifest)
    
    @property
    def nulls(self) -> PlayerNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> PlayerLayer:
        return self.manifest.types