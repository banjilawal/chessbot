# src/domain/extract/model/coord/extract.py

"""
Module: domain.extract.model.coord.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Coord, CoordBlueprint, ModelPrimeExtract
from transit import CoordCarrier


class CoordPrimeExtract(ModelPrimeExtract[Coord]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for CoordValidator.

    Attributes:
        carrier: CoordCarrier
        blueprint: Optional[CoordBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: CoordCarrier,
            blueprint: Optional[CoordBlueprint] | None = None,
    ):
        """
        Args:
            carrier: CoordCarrier
            blueprint: Optional[Blueprint[Coord]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> CoordCarrier:
        return cast(CoordCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[CoordBlueprint]:
        return cast(CoordBlueprint, super().blueprint)