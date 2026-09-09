# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import RankHelperTable, ModelValidationToolkit
from domain import Rank, RankManifest



class RankValidationToolkit(ModelValidationToolkit[Rank]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Rank attribute validators and type metadata.

    Attributes:
        helper: Optional[RankManifest]
        metadata: Optional[RankHelperTable]

    Provides:

    Super Class:
    """
    _metadata: RankManifest
    _helper: RankHelperTable
    
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
        self._helper = helper or RankHelperTable()
        self._metadata = metadata or RankManifest()
    
    @property
    def helper(self) -> RankHelperTable:
        return cast(RankHelperTable, super().helper)
    
    @property
    def metadata(self) -> RankManifest:
        return cast(RankManifest, super().metadata)
