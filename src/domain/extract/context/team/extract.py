# src/domain/extract/context/team/extract.py

"""
Module: domain.extract.context.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import TeamContextBlueprint
from transit import TeamContextCarrier


class TeamContextPrimeExtract(ContextPrimeExtract[TeamContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for TeamValidator.

    Attributes:
        contextCarrier: TeamContextCarrier
        blueprint: Optional[TeamContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: TeamContextCarrier,
            blueprint: Optional[TeamContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: TeamContextCarrier
            blueprint: Optional[ContextBlueprint[Team]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> TeamContextCarrier:
        return cast(TeamContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[TeamContextBlueprint]:
        return cast(TeamContextBlueprint, super().blueprint)