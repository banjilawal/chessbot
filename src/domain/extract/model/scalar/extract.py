# src/domain/extract/model/scalar/extract.py

"""
Module: domain.extract.model.scalar.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelPrimeExtract
from domain import Scalar, ScalarBlueprint
from transit import ScalarCarrier


class ScalarPrimeExtract(ModelPrimeExtract[Scalar]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ScalarValidator.

    Attributes:
        carrier: ScalarCarrier
        blueprint: Optional[ScalarBlueprint]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            carrier: ScalarCarrier,
            blueprint: Optional[ScalarBlueprint] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[Scalar]
            blueprint: Optional[Blueprint[Scalar]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint,)
        
    @property
    def carrier(self) -> ScalarCarrier:
        return cast(ScalarCarrier, super().carrier)
    
    @property
    def blueprint(self) -> Optional[ScalarBlueprint]:
        return cast(ScalarBlueprint,super().blueprint)