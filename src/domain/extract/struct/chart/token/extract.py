# src/domain/extract/struct/chart/participate.extract.py

"""
Module: domain.extract.struct.chart.participate.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Participation, ParticipationBlueprint, ChartPrimeExtract
from transit import ParticipationCarrier


class ParticipationPrimeExtract(ChartPrimeExtract[Participation]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ParticipationValidator.

    Attributes:
        carrier: ParticipationCarrier
        blueprint: Optional[ParticipationBlueprint]

    Provides:

    Super Class:
        ChartPrimeExtract
    """

    def __init__(
            self,
            carrier: ParticipationCarrier,
            blueprint: Optional[ParticipationBlueprint] | None = None,
    ):
        """
        Args:
            carrier: ParticipationCarrier
            blueprint: Optional[ParticipationBlueprint]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> ParticipationCarrier:
        return cast(ParticipationCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[ParticipationBlueprint]:
        return cast(ParticipationBlueprint, super().blueprint)