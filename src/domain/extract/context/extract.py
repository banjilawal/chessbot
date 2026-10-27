# src/domain/extract/context/extract.py

"""
Module: domain.extract.context.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from os import MFD_ALLOW_SEALING
from typing import Generic, Optional, TypeVar, cast

from domain import Context, ContextBlueprint, PrimeExtract
from transit import ContextCarrier

T = TypeVar("T", bound="Context")

class ContextPrimeExtract(PrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist ContextBlueprint and ContextCarrier data for ContextValidator.

    Attributes:
        reference: ContextCarrier[T]
        blueprint: Optional[ContextBlueprint[T]]

    Provides:

    Super Class:
        ContextPrimeExtract
    """

    def __init__(
            self,
            reference: ContextCarrier[T],
            blueprint: Optional[ContextBlueprint[T]] | None = None,
    ):
        """
        Args:
            reference: ContextCarrier[T]
            blueprint: Optional[ContextBlueprint[T]]
        """
        super().__init__(reference=reference, blueprint=blueprint)
        
    @property
    def reference(self) -> ContextCarrier[T]:
        return cast(ContextCarrier[T], super().reference)
    
    @property
    def blueprint(self) -> Optional[ContextBlueprint[T]]:
        return cast(ContextBlueprint[T], super().blueprint)
        
    @property
    def is_valid_context_size(self) -> bool:
        blueprint =  self.blueprint
        if blueprint is None:
            return False
        return blueprint.is_valid_size
    
    @property
    def has_wrong_context_size(self) -> bool:
        return not self.is_valid_context_size
        
 
    
