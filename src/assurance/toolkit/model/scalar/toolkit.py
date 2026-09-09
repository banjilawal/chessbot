# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ScalarHelperTable, ModelValidationToolkit
from domain import Scalar, ScalarManifest



class ScalarValidationToolkit(ModelValidationToolkit[Scalar]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Scalar attribute validators and type metadata.

    Attributes:
        helper: Optional[ScalarManifest]
        metadata: Optional[ScalarHelperTable]

    Provides:

    Super Class:
    """
    _metadata: ScalarManifest
    _helper: ScalarHelperTable
    
    def __init__(
            self,
            metadata: Optional[ScalarManifest] | None = None,
            helper: Optional[ScalarHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[ScalarManifest]
            metadata: Optional[ScalarHelperTable]
        """
        self._helper = helper or ScalarHelperTable()
        self._metadata = metadata or ScalarManifest()
    
    @property
    def helper(self) -> ScalarHelperTable:
        return cast(ScalarHelperTable, super().helper)
    
    @property
    def metadata(self) -> ScalarManifest:
        return cast(ScalarManifest, super().metadata)
