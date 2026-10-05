# src/assurance/depend/toolkit/struct/chart/walk/toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.walk.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ChartValidatorToolkit, WalkDependency
from domain import Walk, WalkManifest, WalkNullGroup, WalkTypeUnion


class WalkValidatorToolkit(ChartValidatorToolkit[Walk]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: WalkDependency
            metadata: WalkManifest

    Provides:

    Super Class:
       ChartValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[WalkDependency] | None = None,
            metadata: Optional[WalkManifest] | None = None,
    ):
        """
            wrapper: Optional[WalkDependency]
            metadata: Optional[WalkManifest]
        """
        super().__init__(
            wrapper=wrapper or WalkDependency(),
            metadata=metadata or WalkManifest(),
        )
    
    @property
    def wrapper(self) -> WalkDependency:
        return cast(WalkDependency, super().wrapper)
    
    @property
    def metadata(self) -> WalkManifest:
        return cast(WalkManifest, super().metadata)
    
    @property
    def nulls(self) -> WalkNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> WalkTypeUnion:
        return self.metadata.types