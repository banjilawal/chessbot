# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ArenaHelperTable, ModelValidationToolkit
from domain import Arena, ArenaManifest



class ArenaValidationToolkit(ModelValidationToolkit[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Arena attribute validators and type metadata.

    Attributes:
        helper: Optional[ArenaManifest]
        metadata: Optional[ArenaHelperTable]

    Provides:

    Super Class:
    """
    _metadata: ArenaManifest
    _helper: ArenaHelperTable
    
    def __init__(
            self,
            metadata: Optional[ArenaManifest] | None = None,
            helper: Optional[ArenaHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[ArenaManifest]
            metadata: Optional[ArenaHelperTable]
        """
        self._helper = helper or ArenaHelperTable()
        self._metadata = metadata or ArenaManifest()
    
    @property
    def helper(self) -> ArenaHelperTable:
        return cast(ArenaHelperTable, super().helper)
    
    @property
    def metadata(self) -> ArenaManifest:
        return cast(ArenaManifest, super().metadata)
