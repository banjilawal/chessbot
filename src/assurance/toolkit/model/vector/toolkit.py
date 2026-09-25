# src/assurance/toolkit/model/vector/toolkit.py

"""
Module: assurance.toolkit.model.vector.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, VectorHelperTable
from domain import Vector, VectorManifest


class VectorValidatorToolkit(ModelValidatorToolkit[Vector]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Vector attribute validators and type metadata.

    Attributes:
        helper: VectorManifest
        metadata: VectorHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
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
        super().__init__(
            helper=helper or VectorHelperTable(),
            metadata=metadata or VectorManifest(),
        )
    
    @property
    def attribute(self) -> VectorHelperTable:
        return cast(VectorHelperTable, super().attribute)
    
    @property
    def metadata(self) -> VectorManifest:
        return cast(VectorManifest, super().metadata)