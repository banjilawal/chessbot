# src/assurance/depend/toolkit/model/rank/toolkit.py

"""
Module: assurance.depend.toolkit.model.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, RankWrapperDependency
from domain import Rank, RankManifest, RankNullGroup, RankTypeUnion


class RankValidatorToolkit(ModelValidatorToolkit[Rank]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Rank attribute validators and type metadata.

    Attributes:
        helper: RankManifest
        metadata: RankWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[RankManifest] | None = None,
            wrapper: Optional[RankWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[RankManifest]
            metadata: Optional[RankWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or RankWrapperDependency(),
            metadata=metadata or RankManifest(),
        )
    
    @property
    def wrapper(self) -> RankWrapperDependency:
        return cast(RankWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> RankManifest:
        return cast(RankManifest, super().metadata)
    
    @property
    def nulls(self) -> RankNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> RankTypeUnion:
        return self.metadata.types