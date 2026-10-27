# src/assurance/depend/toolkit/struct/chart/participate/toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.participate.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ChartLayerToolkit, ParticipationDependency
from domain import (
    Participation, ParticipationManifest, ParticipationNullGroup,
    ParticipationTypeUnion
)


class ParticipationLayerToolkit(ChartLayerToolkit[Participation]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type manifest.

    Attributes:
            wrapper: ParticipationDependency
            manifest: ParticipationManifest

    Provides:

    Super Class:
       ChartLayerToolkit
    """
    
    def __init__(
            self,
            dependency: Optional[ParticipationDependency] | None = None,
            manifest: Optional[ParticipationManifest] | None = None,
    ):
        """
            wrapper: Optional[ParticipationDependency]
            manifest: Optional[ParticipationManifest]
        """
        super().__init__(
            dependency=dependency or ParticipationDependency(),
            manifest=manifest or ParticipationManifest(),
        )
    
    @property
    def dependency(self) -> ParticipationDependency:
        return cast(ParticipationDependency, super().dependency)
    
    @property
    def manifest(self) -> ParticipationManifest:
        return cast(ParticipationManifest, super().manifest)
    
    @property
    def nulls(self) -> ParticipationNullGroup:
        return self.manifest.nulls
    
    @property
    def types(self) -> ParticipationTypeUnion:
        return self.manifest.types