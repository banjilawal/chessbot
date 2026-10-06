# src/domain/extract/model/scalar/extract.py

"""
Module: domain.extract.model.scalar.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelPrimeExtract, Scalar, ScalarBlueprint
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

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: ScalarCarrier,
            blueprint: Optional[ScalarBlueprint] | None = None,
    ):
        """
        Args:
            reference: EScalarCarrier
            blueprint: Optional[Blueprint[Scalar]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ScalarCarrier:
        return cast(ScalarCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[ScalarBlueprint]:
        return cast(ScalarBlueprint, super().blueprint)