# src/assurance/toolkit/model/rank/toolkit.py

"""
Module: assurance.toolkit.model.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, RankValidationWrapperDict
from domain import Rank, RankManifest, RankNullGroup, RankTypeUnion


class RankValidatorToolkit(ModelValidatorToolkit[Rank]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Rank attribute validators and type metadata.

    Attributes:
        helper: RankManifest
        metadata: RankHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[RankManifest] | None = None,
            wrapper: Optional[RankValidationWrapperDict] | None = None,
    ):
        """
        Args:
            wrapper: Optional[RankManifest]
            metadata: Optional[RankHelperTable]
        """
        super().__init__(
            wrapper=wrapper or RankValidationWrapperDict(),
            metadata=metadata or RankManifest(),
        )
    
    @property
    def wrapper(self) -> RankValidationWrapperDict:
        return cast(RankValidationWrapperDict, super().wrapper)
    
    @property
    def metadata(self) -> RankManifest:
        return cast(RankManifest, super().metadata)
    
    @property
    def nulls(self) -> RankNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> RankTypeUnion:
        return self.metadata.types