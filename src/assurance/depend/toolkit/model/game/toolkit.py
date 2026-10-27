# src/assurance/depend/toolkit/model/game/toolkit.py

"""
Module: assurance.depend.toolkit.model.game.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, GameServiceDependency
from domain import Game, GameManifest, GameNullWarningSet, GameLayer


class GameLayerToolkit(ModelLayerToolkit[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Game attribute validators and type manifest.

    Attributes:
        helper: GameManifest
        manifest: GameServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[GameManifest] | None = None,
            dependency: Optional[GameServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[GameManifest]
            manifest: Optional[GameServiceDependency]
        """
        super().__init__(
            dependency=dependency or GameServiceDependency(),
            manifest=manifest or GameManifest(),
        )
    
    @property
    def dependency(self) -> GameServiceDependency:
        return cast(GameServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> GameManifest:
        return cast(GameManifest, super().manifest)
    
    @property
    def nulls(self) -> GameNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> GameLayer:
        return self.manifest.types