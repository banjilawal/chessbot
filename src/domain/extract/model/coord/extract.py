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
            reference: CoordCarrier,
            safe_blueprint: Optional[CoordBlueprint] | None = None,
    ):
        """
        Args:
            reference: CoordCarrier
            safe_blueprint: Optional[Blueprint[Coord]]
        """
        super().__init__(reference=reference, safe_blueprint=safe_blueprint)
        
    @property
    def reference(self) -> CoordCarrier:
        return cast(CoordCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[CoordBlueprint]:
        return cast(CoordBlueprint, super().blueprint)