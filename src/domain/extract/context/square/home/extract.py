# src/domain/extract/context/square/home/extract.py

"""
Module: domain.extract.context.square.home.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextPrimeExtract, HomeSquare, HomeSquareContextBlueprint
from transit import HomeSquareContextCarrier


class HomeSquareContextPrimeExtract(ContextPrimeExtract[HomeSquareContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for HomeSquareValidator.

    Attributes:
        contextCarrier: HomeSquareContextCarrier
        blueprint: Optional[HomeSquareContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: HomeSquareContextCarrier,
            blueprint: Optional[HomeSquareContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: HomeSquareContextCarrier
            blueprint: Optional[HomeSquareContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> HomeSquareContextCarrier:
        return cast(HomeSquareContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[HomeSquareContextBlueprint]:
        return cast(HomeSquareContextBlueprint, super().blueprint)