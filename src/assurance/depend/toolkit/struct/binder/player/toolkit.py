# src/assurance/depend/toolkit/struct/binder/player/toolkit.py

"""
Module: assurance.depend.toolkit.struct.binder.player.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import BinderLayerToolkit, PlayerBinderDependency
from domain import (
    PlayerBinder, PlayerBinderManifest, PlayerBinderNullWarningSet,
    PlayerBinderLayer
)


class PlayerBinderLayerToolkit(BinderLayerToolkit[PlayerBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: PlayerBinderDependency
            manifest: PlayerBinderManifest

    Provides:

    Super Class:
       BinderLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[PlayerBinderDependency] | None = None,
            manifest: Optional[PlayerBinderManifest] | None = None,
    ):
        """
            wrapper: Optional[PlayerBinderDependency]
            manifest: Optional[PlayerBinderManifest]
        """
        super().__init__(
            dependency=dependency or PlayerBinderDependency(),
            manifest=manifest or PlayerBinderManifest(),
        )
    
    @property
    def dependency(self) -> PlayerBinderDependency:
        return cast(PlayerBinderDependency, super().dependency)
    
    @property
    def manifest(self) -> PlayerBinderManifest:
        return cast(PlayerBinderManifest, super().manifest)
    
    @property
    def nulls(self) -> PlayerBinderNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> PlayerBinderLayer:
        return self.manifest.types