# src/domain/extract/struct/coord/extract.py

"""
Module: domain.extract.struct.coord.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import StructPrimeExtract
from domain import Coord, CoordBlueprint
from transit import CoordCarrier


class CoordPrimeExtract(StructPrimeExtract[Coord]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for CoordValidator.

    Attributes:
        carrier: CoordCarrier
        blueprint: Optional[CoordBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: CoordCarrier,
            blueprint: Optional[CoordBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Coord]
            blueprint: Optional[Blueprint[Coord]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> CoordCarrier:
        return cast(CoordCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[CoordBlueprint]:
        return cast(CoordBlueprint, super().blueprint)