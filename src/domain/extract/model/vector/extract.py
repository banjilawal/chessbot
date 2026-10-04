# src/domain/extract/model/vector/extract.py

"""
Module: domain.extract.model.vector.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelPrimeExtract, Vector, VectorBlueprint
from transit import VectorCarrier


class VectorPrimeExtract(ModelPrimeExtract[Vector]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for VectorValidator.

    Attributes:
        carrier: VectorCarrier
        blueprint: Optional[VectorBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: VectorCarrier,
            blueprint: Optional[VectorBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Vector]
            blueprint: Optional[Blueprint[Vector]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> VectorCarrier:
        return cast(VectorCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[VectorBlueprint]:
        return cast(VectorBlueprint, super().blueprint)