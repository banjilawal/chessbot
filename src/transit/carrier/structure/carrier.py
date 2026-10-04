# src/transit/carrier/struct/carrier.py

"""
Module: transit.carrier.struct.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from domain import Struct, StructBlueprint
from transit import EntityCarrier

T = TypeVar("T", bound="Struct")

class StructCarrier(EntityCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Struct or its Blueprint.

    Attributes:
        entity: [T | StructBlueprint[T]]


    Provides:
        -   def extract_blueprint() -> Optional[StructBlueprint[T]]

    Super Class:
        EntityCarrier
    """
    
    def __init__(self):
        super().__init__()
    
    @property
    def entity(self) -> Optional[T | StructBlueprint[T]]:
        if (
                self.is_empty or
                self.is_not_consistent
        ):
            return None
        if self.has_model:
            return cast(T, super().entity)
        return cast(StructBlueprint[T], super().entity)
    
    @property
    @abstractmethod
    def has_model(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_blueprint(self) -> bool:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[StructBlueprint[T]]:
        pass



    