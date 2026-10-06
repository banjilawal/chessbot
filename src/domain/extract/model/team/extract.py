# src/domain/extract/model/team/extract.py

"""
Module: domain.extract.model.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelPrimeExtract, Team, TeamBlueprint
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

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: TeamCarrier,
            safe_blueprint: Optional[TeamBlueprint] | None = None,
    ):
        """
        Args:
            reference: TeamCarrier
            safe_blueprint: Optional[Blueprint[Team]]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> TeamCarrier:
        return cast(TeamCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[TeamBlueprint]:
        return cast(TeamBlueprint, super().blueprint)