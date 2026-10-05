# src/assurance/depend/toolkit/struct/chart/participate/toolkit.py

"""
Module: assurance.depend.toolkit.struct.chart.participate.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ChartValidatorToolkit, ParticipationDependency
from domain import (
    Participation, ParticipationManifest, ParticipationNullGroup,
    ParticipationTypeUnion
)


class ParticipationValidatorToolkit(ChartValidatorToolkit[Participation]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: TokenChartDependency
            metadata: TokenChartManifest

    Provides:

    Super Class:
       ChartValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[ParticipationDependency] | None = None,
            metadata: Optional[ParticipationManifest] | None = None,
    ):
        """
            wrapper: Optional[TokenChartDependency]
            metadata: Optional[TokenChartManifest]
        """
        super().__init__(
            wrapper=wrapper or ParticipationDependency(),
            metadata=metadata or ParticipationManifest(),
        )
    
    @property
    def wrapper(self) -> ParticipationDependency:
        return cast(ParticipationDependency, super().wrapper)
    
    @property
    def metadata(self) -> ParticipationManifest:
        return cast(ParticipationManifest, super().metadata)
    
    @property
    def nulls(self) -> ParticipationNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> ParticipationTypeUnion:
        return self.metadata.types