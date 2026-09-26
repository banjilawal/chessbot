# src/assurance/toolkit/model/path/toolkit.py

"""
Module: assurance.toolkit.model.path.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, PathHelperTable
from domain import Path, PathManifest, PathNullGroup, PathTypeUnion


class PathValidatorToolkit(ModelValidatorToolkit[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Path attribute validators and type metadata.

    Attributes:
        helper: PathManifest
        metadata: PathHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[PathManifest] | None = None,
            helper: Optional[PathHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[PathManifest]
            metadata: Optional[PathHelperTable]
        """
        super().__init__(
            helper=helper or PathHelperTable(),
            metadata=metadata or PathManifest(),
        )
    
    @property
    def helper(self) -> PathHelperTable:
        return cast(PathHelperTable, super().helper)
    
    @property
    def metadata(self) -> PathManifest:
        return cast(PathManifest, super().metadata)
    
    @property
    def nulls(self) -> PathNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> PathTypeUnion:
        return self.metadata.types