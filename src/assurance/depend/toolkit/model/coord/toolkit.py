# src/assurance/depend/toolkit/model/coord/toolkit.py

"""
Module: assurance.depend.toolkit.model.coord.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, CoordWrapperDependency
from domain import Coord, CoordManifest, CoordNullGroup, CoordTypeUnion


class CoordValidatorToolkit(ModelValidatorToolkit[Coord]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Coord attribute validators and type metadata.

    Attributes:
        helper: CoordManifest
        metadata: CoordHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[CoordManifest] | None = None,
            wrapper: Optional[CoordWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[CoordManifest]
            metadata: Optional[CoordHelperTable]
        """
        super().__init__(
            wrapper=wrapper or CoordWrapperDependency(),
            metadata=metadata or CoordManifest(),
        )
    
    @property
    def wrapper(self) -> CoordWrapperDependency:
        return cast(CoordWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> CoordManifest:
        return cast(CoordManifest, super().metadata)
    
    @property
    def nulls(self) -> CoordNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> CoordTypeUnion:
        return self.metadata.types