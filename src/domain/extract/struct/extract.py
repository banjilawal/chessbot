# src/domain/extract/struct/extract.py

"""
Module: domain.extract.struct.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import Struct, StructBlueprint, PrimeExtract
from transit import StructCarrier

T = TypeVar("T", bound="Struct")

class StructPrimeExtract(PrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for StructValidator.

    Attributes:
        carrier: StructCarrier[T]
        blueprint: Optional[StructBlueprint[T]]

    Provides:

    Super Class:
        PrimeExtract
    """

    def __init__(
            self,
            carrier: StructCarrier[T],
            blueprint: Optional[StructBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[T]
            blueprint: Optional[Blueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> StructCarrier[T]:
        return cast(StructCarrier[T], super().carrier)
    
    @property
    def blueprint(self) -> Optional[StructBlueprint[T]]:
        return cast(StructBlueprint[T], super().blueprint)
    
