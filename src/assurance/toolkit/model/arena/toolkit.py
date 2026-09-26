# src/assurance/toolkit/model/arena/toolkit.py

"""
Module: assurance.toolkit.model.arena.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, ArenaValidationWrapperDict
from domain import Arena, ArenaManifest, ArenaNullGroup, ArenaTypeUnion

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
            wrapper: Optional[ArenaValidationWrapperDict] | None = None,
    ):
        """
        Args:
            wrapper: Optional[ArenaManifest]
            metadata: Optional[ArenaHelperTable]
        """
        super().__init__(
            wrapper=wrapper or ArenaValidationWrapperDict(),
            metadata=metadata or ArenaManifest(),
        )
    
    @property
    def wrapper(self) -> ArenaValidationWrapperDict:
        return cast(ArenaValidationWrapperDict, super().wrapper)
    
    @property
    def metadata(self) -> ArenaManifest:
        return cast(ArenaManifest, super().metadata)
    
    @property
    def nulls(self) -> ArenaNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> ArenaTypeUnion:
        return self.metadata.types