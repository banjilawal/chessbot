# src/domain/metadata/manifest/strcture/chart/participate/manifest.py

"""
Module: domain.metadata.manifest.struct.chart.participate.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartManifest, Participation, ParticipationNullGroup, ParticipationTypeUnion


class ParticipationManifest(ChartManifest[Participation]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the TokenChart
            security lifecycle.

     Attributes:
        types: TokenChartTypeUnion
        nulls: TokenChartNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[ParticipationTypeUnion] | None = None,
            nulls: Optional[ParticipationNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[TokenChartTypeUnion]
            nulls: Optional[TokenChartNullGroup]
        """
        super().__init__(
            types=types or ParticipationTypeUnion(),
            nulls=nulls or ParticipationNullGroup(),
        )

        
    @property
    def types(self) -> ParticipationTypeUnion:
        return cast(ParticipationTypeUnion, super().types)
    
    @property
    def nulls(self) -> ParticipationNullGroup:
        return cast(ParticipationNullGroup, super().nulls)