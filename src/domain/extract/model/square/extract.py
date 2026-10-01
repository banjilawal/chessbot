# src/domain/extract/model/square/extract.py

"""
Module: domain.extract.model.square.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelPrimeExtract
from domain import Square, SquareBlueprint
from transit import SquareCarrier


class SquarePrimeExtract(ModelPrimeExtract[Square]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for SquareValidator.

    Attributes:
        carrier: SquareCarrier
        blueprint: Optional[SquareBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: SquareCarrier,
            blueprint: Optional[SquareBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Square]
            blueprint: Optional[Blueprint[Square]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> SquareCarrier:
        return cast(SquareCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[SquareBlueprint]:
        return cast(SquareBlueprint, super().blueprint)