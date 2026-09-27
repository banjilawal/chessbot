# src/domain/extract/model/team/extract.py

"""
Module: domain.extract.model.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelPrimeExtract
from domain import Team, TeamBlueprint
from transit import TeamCarrier


class TeamPrimeExtract(ModelPrimeExtract[Team]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for TeamValidator.

    Attributes:
        carrier: TeamCarrier
        blueprint: Optional[TeamBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: TeamCarrier,
            blueprint: Optional[TeamBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Team]
            blueprint: Optional[Blueprint[Team]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> TeamCarrier:
        return cast(TeamCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[TeamBlueprint]:
        return cast(TeamBlueprint,super().blueprint)