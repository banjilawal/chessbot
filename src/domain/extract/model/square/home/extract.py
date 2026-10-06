# src/domain/extract/model/square/home/extract.py

"""
Module: domain.extract.model.square.home.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelPrimeExtract, HomeSquare, HomeSquareBlueprint
from transit import HomeSquareCarrier


class HomeSquarePrimeExtract(ModelPrimeExtract[HomeSquare]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for HomeSquareValidator.

    Attributes:
        carrier: HomeSquareCarrier
        blueprint: Optional[HomeSquareBlueprint]

    Provides:

    Super Class:
        ModelPrimeExtract
    """

    def __init__(
            self,
            reference: HomeSquareCarrier,
            blueprint: Optional[HomeSquareBlueprint] | None = None,
    ):
        """
        Args:
            reference: HomeSquareCarrier
            blueprint: Optional[HomeSquareBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> HomeSquareCarrier:
        return cast(HomeSquareCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[HomeSquareBlueprint]:
        return cast(HomeSquareBlueprint, super().blueprint)