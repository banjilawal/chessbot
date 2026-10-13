# src/domain/extract/struct/binder/extract.py

"""
Module: domain.extract.struct.binder.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast


from domain import ArchetypeBinder, StructPrimeExtract, BinderBlueprint
from transit import BinderCarrier

T = TypeVar("T", bound="ArchetypeBinder")

class BinderPrimeExtract(StructPrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for BinderValidator.

    Attributes:
        carrier: BinderCarrier
        blueprint: Optional[BinderBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            reference: BinderCarrier[T],
            blueprint: Optional[BinderBlueprint[T]] | None = None,
    ):
        """
        Args:
            reference: BinderCarrier[T]
            blueprint: Optional[BinderBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> BinderCarrier[T]:
        return cast(BinderCarrier, super().reference)
    
    @property
    def blueprint(self) -> Optional[BinderBlueprint[T]]:
        return cast(BinderBlueprint, super().blueprint)