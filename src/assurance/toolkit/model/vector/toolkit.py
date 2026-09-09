# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import VectorHelperTable, ModelValidationToolkit
from domain import Vector, VectorManifest



class VectorValidationToolkit(ModelValidationToolkit[Vector]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Vector attribute validators and type metadata.

    Attributes:
        helper: Optional[VectorManifest]
        metadata: Optional[VectorHelperTable]

    Provides:

    Super Class:
    """
    _metadata: VectorManifest
    _helper: VectorHelperTable
    
    def __init__(
            self,
            metadata: Optional[VectorManifest] | None = None,
            helper: Optional[VectorHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[VectorManifest]
            metadata: Optional[VectorHelperTable]
        """
        self._helper = helper or VectorHelperTable()
        self._metadata = metadata or VectorManifest()
    
    @property
    def helper(self) -> VectorHelperTable:
        return cast(VectorHelperTable, super().helper)
    
    @property
    def metadata(self) -> VectorManifest:
        return cast(VectorManifest, super().metadata)
