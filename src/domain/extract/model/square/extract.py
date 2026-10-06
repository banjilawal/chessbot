# src/domain/extract/model/square/extract.py

"""
Module: domain.extract.model.square.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelPrimeExtract, Square, SquareBlueprint
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

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: SquareCarrier,
            blueprint: Optional[SquareBlueprint] | None = None,
    ):
        """
        Args:
            reference: SquareCarrier
            blueprint: Optional[SquareBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> SquareCarrier:
        return cast(SquareCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[SquareBlueprint]:
        return cast(SquareBlueprint, super().blueprint)