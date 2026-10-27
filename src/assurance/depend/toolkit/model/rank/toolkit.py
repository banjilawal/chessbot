# src/assurance/depend/toolkit/model/rank/toolkit.py

"""
Module: assurance.depend.toolkit.model.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, RankServiceDependency
from domain import Rank, RankManifest, RankNullWarningSet, RankLayer


class RankLayerToolkit(ModelLayerToolkit[Rank]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Rank attribute validators and type manifest.

    Attributes:
        helper: RankManifest
        manifest: RankServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[RankManifest] | None = None,
            dependency: Optional[RankServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[RankManifest]
            manifest: Optional[RankServiceDependency]
        """
        super().__init__(
            dependency=dependency or RankServiceDependency(),
            manifest=manifest or RankManifest(),
        )
    
    @property
    def dependency(self) -> RankServiceDependency:
        return cast(RankServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> RankManifest:
        return cast(RankManifest, super().manifest)
    
    @property
    def nulls(self) -> RankNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> RankLayer:
        return self.manifest.types