# src/assurance/toolkit/model/arena/toolkit.py

"""
Module: assurance.toolkit.model.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, ArenaHelperTable
from domain import Arena, ArenaManifest


class ArenaValidatorToolkit(ModelValidatorToolkit[Arena]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Arena attribute validators and type metadata.

    Attributes:
        helper: ArenaManifest
        metadata: ArenaHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
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
        super().__init__(
            helper=helper or ArenaHelperTable(),
            metadata=metadata or ArenaManifest(),
        )
    
    @property
    def attribute(self) -> ArenaHelperTable:
        return cast(ArenaHelperTable, super().attribute)
    
    @property
    def metadata(self) -> ArenaManifest:
        return cast(ArenaManifest, super().metadata)