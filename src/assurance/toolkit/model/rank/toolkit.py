# src/assurance/toolkit/model/rank/toolkit.py

"""
Module: assurance.toolkit.model.rank.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, RankHelperTable
from domain import Rank, RankManifest


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
            helper: Optional[RankHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[RankManifest]
            metadata: Optional[RankHelperTable]
        """
        super().__init__(
            helper=helper or RankHelperTable(),
            metadata=metadata or RankManifest(),
        )
    
    @property
    def attribute(self) -> RankHelperTable:
        return cast(RankHelperTable, super().attribute)
    
    @property
    def metadata(self) -> RankManifest:
        return cast(RankManifest, super().metadata)