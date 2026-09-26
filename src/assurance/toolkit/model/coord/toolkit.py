# src/assurance/toolkit/model/coord/toolkit.py

"""
Module: assurance.toolkit.model.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, CoordHelperTable
from domain import Coord, CoordManifest, CoordNullGroup, CoordTypeUnion


class CoordValidatorToolkit(ModelValidatorToolkit[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Coord attribute validators and type metadata.

    Attributes:
        helper: CoordManifest
        metadata: CoordHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[CoordManifest] | None = None,
            helper: Optional[CoordHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[CoordManifest]
            metadata: Optional[CoordHelperTable]
        """
        super().__init__(
            helper=helper or CoordHelperTable(),
            metadata=metadata or CoordManifest(),
        )
    
    @property
    def helper(self) -> CoordHelperTable:
        return cast(CoordHelperTable, super().helper)
    
    @property
    def metadata(self) -> CoordManifest:
        return cast(CoordManifest, super().metadata)
    
    @property
    def nulls(self) -> CoordNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> CoordTypeUnion:
        return self.metadata.types