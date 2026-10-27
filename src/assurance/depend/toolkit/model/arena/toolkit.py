# src/assurance/depend/toolkit/model/arena/toolkit.py

"""
Module: assurance.depend.toolkit.model.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, ArenaServiceDependency
from domain import Arena, ArenaManifest, ArenaNullWarningSet, ArenaLayer

class ArenaLayerToolkit(ModelLayerToolkit[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Arena attribute validators and type manifest.

    Attributes:
        helper: ArenaManifest
        manifest: ArenaServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[ArenaManifest] | None = None,
            dependency: Optional[ArenaServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[ArenaManifest]
            manifest: Optional[ArenaServiceDependency]
        """
        super().__init__(
            dependency=dependency or ArenaServiceDependency(),
            manifest=manifest or ArenaManifest(),
        )
    
    @property
    def dependency(self) -> ArenaServiceDependency:
        return cast(ArenaServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> ArenaManifest:
        return cast(ArenaManifest, super().manifest)
    
    @property
    def nulls(self) -> ArenaNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> ArenaLayer:
        return self.manifest.types