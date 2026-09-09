# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import CoordHelperTable, ModelValidationToolkit
from domain import Coord, CoordManifest



class CoordValidationToolkit(ModelValidationToolkit[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Coord attribute validators and type metadata.

    Attributes:
        helper: Optional[CoordManifest]
        metadata: Optional[CoordHelperTable]

    Provides:

    Super Class:
    """
    _metadata: CoordManifest
    _helper: CoordHelperTable
    
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
        self._helper = helper or CoordHelperTable()
        self._metadata = metadata or CoordManifest()
    
    @property
    def helper(self) -> CoordHelperTable:
        return cast(CoordHelperTable, super().helper)
    
    @property
    def metadata(self) -> CoordManifest:
        return cast(CoordManifest, super().metadata)
