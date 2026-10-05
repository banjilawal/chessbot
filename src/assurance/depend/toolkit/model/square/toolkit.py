# src/assurance/depend/toolkit/model/square/toolkit.py

"""
Module: assurance.depend.toolkit.model.square.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, SquareWrapperDependency
from domain import Square, SquareManifest, SquareNullGroup, SquareTypeUnion


class SquareValidatorToolkit(ModelValidatorToolkit[Square]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Square attribute validators and type metadata.

    Attributes:
        helper: SquareManifest
        metadata: SquareWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[SquareManifest] | None = None,
            wrapper: Optional[SquareWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[SquareManifest]
            metadata: Optional[SquareWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or SquareWrapperDependency(),
            metadata=metadata or SquareManifest(),
        )
    
    @property
    def wrapper(self) -> SquareWrapperDependency:
        return cast(SquareWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> SquareManifest:
        return cast(SquareManifest, super().metadata)
    
    @property
    def nulls(self) -> SquareNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> SquareTypeUnion:
        return self.metadata.types