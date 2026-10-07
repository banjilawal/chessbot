# src/domain/metadata/nulls/struct/chart/participate/group.py

"""
Module: domain.metadata.nulls.struct.chart.participate.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ChartNullGroup, Participation
from err import (
    ParticipationBlueprintNullException, ParticipationCarrierNullException,
    ParticipationNullException
)


class ParticipationNullGroup(ChartNullGroup[Participation]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Participation's integrity cycle.

    Attributes:
        model: ParticipationNullException
        carrier: ParticipationCarrierNullException
        blueprint:ParticipationBlueprintNullException

    Provides:

    Super Class:
        ChartNullGroup
    """

    
    def __init__(
            self,
            model: Optional[ParticipationNullException] | None = None,
            carrier: Optional[ParticipationCarrierNullException] | None = None,
            blueprint: Optional[ParticipationBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[ParticipationNullException]
            carrier: Optional[ParticipationCarrierNullException]
            blueprint: Optional[ParticipationBlueprintNullException]
        """
        super().__init__(
            model=model or ParticipationNullException(),
            carrier=carrier or ParticipationCarrierNullException(),
            blueprint=blueprint or ParticipationBlueprintNullException(),
        )
        
    @property
    def struct(self) -> ParticipationNullException:
        return cast(ParticipationNullException, super().model)
    
    @property
    def model(self) -> ParticipationNullException:
        return self.struct
    
    @property
    def carrier(self) -> ParticipationCarrierNullException:
        return cast(ParticipationCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ParticipationBlueprintNullException:
        return cast(ParticipationBlueprintNullException, super().blueprint)