# src/domain/extract/struct/team/extract.py

"""
Module: domain.extract.struct.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import StructPrimeExtract, Team, TeamBlueprint
from transit import TeamCarrier


class TeamPrimeExtract(StructPrimeExtract[Team]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for TeamValidator.

    Attributes:
        carrier: TeamCarrier
        blueprint: Optional[TeamBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: TeamCarrier,
            blueprint: Optional[TeamBlueprint] | None = None,
    ):
        """
        Args:
            carrier: TeamCarrier
            blueprint: Optional[Blueprint[Team]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> TeamCarrier:
        return cast(TeamCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[TeamBlueprint]:
        return cast(TeamBlueprint, super().blueprint)