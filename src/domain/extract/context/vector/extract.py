# src/domain/extract/context/vector/extract.py

"""
Module: domain.extract.context.vector.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextPrimeExtract, Vector, VectorContextBlueprint
from transit import VectorContextCarrier


class VectorContextPrimeExtract(ContextPrimeExtract[VectorContext]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for VectorValidator.

    Attributes:
        contextCarrier: VectorContextCarrier
        blueprint: Optional[VectorContextBlueprint]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: VectorContextCarrier,
            blueprint: Optional[VectorContextBlueprint] | None = None,
    ):
        """
        Args:
            reference: ContextCarrier[Vector]
            blueprint: Optional[ContextBlueprint[Vector]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> VectorContextCarrier:
        return cast(VectorContextCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[VectorContextBlueprint]:
        return cast(VectorContextBlueprint, super().blueprint)