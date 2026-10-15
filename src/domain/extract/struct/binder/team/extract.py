# src/domain/extract/struct/binder/team/extract.py

"""
Module: domain.extract.struct.binder.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import TeamBinder, TeamBinderBlueprint, BinderPrimeExtract
from transit import TeamBinderCarrier


class TeamBinderPrimeExtract(BinderPrimeExtract[TeamBinder]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for TeamBinderValidator.

    Attributes:
        carrier: TeamBinderCarrier
        blueprint: Optional[TeamBinderBlueprint]

    Provides:

    Super Class:
        BinderPrimeExtract
    """

    def __init__(
            self,
            reference: TeamBinderCarrier,
            blueprint: Optional[TeamBinderBlueprint] | None = None,
    ):
        """
        Args:
            reference: TeamBinderCarrier
            blueprint: Optional[TeamBinderBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> TeamBinderCarrier:
        return cast(TeamBinderCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[TeamBinderBlueprint]:
        return cast(TeamBinderBlueprint, super().blueprint)