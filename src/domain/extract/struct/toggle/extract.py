# src/domain/extract/struct/toggle/extract.py

"""
Module: domain.extract.struct.toggle.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import StructPrimeExtract, Toggle, ToggleBlueprint
from transit import ToggleCarrier

T = TypeVar("T", bound="Toggle")

class TogglePrimeExtract(StructPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ToggleValidator.

    Attributes:
        carrier: ToggleCarrier
        blueprint: Optional[ToggleBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            reference: ToggleCarrier[T],
            blueprint: Optional[ToggleBlueprint[T]] | None = None,
    ):
        """
        Args:
            reference: ToggleCarrier[T]
            blueprint: Optional[ToggleBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ToggleCarrier[T]:
        return cast(ToggleCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[ToggleBlueprint[T]]:
        return cast(ToggleBlueprint, super().blueprint)