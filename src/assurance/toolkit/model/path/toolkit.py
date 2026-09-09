# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import PathHelperTable, ModelValidationToolkit
from domain import Path, PathManifest



class PathValidationToolkit(ModelValidationToolkit[Path]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Path attribute validators and type metadata.

    Attributes:
        helper: Optional[PathManifest]
        metadata: Optional[PathHelperTable]

    Provides:

    Super Class:
    """
    _metadata: PathManifest
    _helper: PathHelperTable
    
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
        self._helper = helper or PathHelperTable()
        self._metadata = metadata or PathManifest()
    
    @property
    def helper(self) -> PathHelperTable:
        return cast(PathHelperTable, super().helper)
    
    @property
    def metadata(self) -> PathManifest:
        return cast(PathManifest, super().metadata)
