# src/assurance/depend/toolkit/struct/chart/footstep/toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.footstep.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ChartValidatorToolkit, FootstepDependency
from domain import Footstep, FootstepManifest, FootstepNullGroup, FootstepTypeUnion


class FootstepValidatorToolkit(ChartValidatorToolkit[Footstep]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: FootstepDependency
            metadata: FootstepManifest

    Provides:

    Super Class:
       ChartValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[FootstepDependency] | None = None,
            metadata: Optional[FootstepManifest] | None = None,
    ):
        """
            wrapper: Optional[FootstepDependency]
            metadata: Optional[FootstepManifest]
        """
        super().__init__(
            wrapper=wrapper or FootstepDependency(),
            metadata=metadata or FootstepManifest(),
        )
    
    @property
    def wrapper(self) -> FootstepDependency:
        return cast(FootstepDependency, super().wrapper)
    
    @property
    def metadata(self) -> FootstepManifest:
        return cast(FootstepManifest, super().metadata)
    
    @property
    def nulls(self) -> FootstepNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> FootstepTypeUnion:
        return self.metadata.types