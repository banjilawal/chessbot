# src/domain/extract/context/arena/extract.py

"""
Module: domain.extract.context.arena.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ArenaContextBlueprint, ContextPrimeExtract
from transit import ArenaContextCarrier


class ArenaContextPrimeExtract(ContextPrimeExtract[ArenaContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for ArenaValidator.

    Attributes:
        contextCarrier: ArenaContextCarrier
        blueprint: Optional[ArenaContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: ArenaContextCarrier,
            blueprint: Optional[ArenaContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: ArenaContextCarrier
            blueprint: Optional[ContextBlueprint[Arena]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ArenaContextCarrier:
        return cast(ArenaContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[ArenaContextBlueprint]:
        return cast(ArenaContextBlueprint, super().blueprint)