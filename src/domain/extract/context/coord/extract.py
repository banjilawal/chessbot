# src/domain/extract/context/coord/extract.py

"""
Module: domain.extract.context.coord.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, CoordContextBlueprint, ContextPrimeExtract
from transit import CoordContextCarrier


class CoordContextPrimeExtract(ContextPrimeExtract[CoordContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for CoordValidator.

    Attributes:
        contextCarrier: CoordContextCarrier
        blueprint: Optional[CoordContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: CoordContextCarrier,
            blueprint: Optional[CoordContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: CoordContextCarrier
            blueprint: Optional[ContextBlueprint[Coord]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> CoordContextCarrier:
        return cast(CoordContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[CoordContextBlueprint]:
        return cast(CoordContextBlueprint, super().blueprint)