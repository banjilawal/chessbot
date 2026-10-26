# src/domain/extract/context/square/extract.py

"""
Module: domain.extract.context.square.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextPrimeExtract, Square, SquareContextBlueprint
from transit import SquareContextCarrier


class SquareContextPrimeExtract(ContextPrimeExtract[SquareContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for SquareValidator.

    Attributes:
        contextCarrier: SquareContextCarrier
        blueprint: Optional[SquareContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: SquareContextCarrier,
            blueprint: Optional[SquareContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: SquareContextCarrier
            blueprint: Optional[SquareContextBlueprint]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> SquareContextCarrier:
        return cast(SquareContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[SquareContextBlueprint]:
        return cast(SquareContextBlueprint, super().blueprint)