# src/transit/carrier/struct/binder/carrier.py

"""
Module: transit.carrier.struct.binder.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import ArchetypeBinder, BinderBlueprint
from transit import StructCarrier

T = TypeVar("T", bound="ArchetypeBinder")


class BinderCarrier(StructCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Binder its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[BinderBlueprint[T]]
        entity: [T | BinderBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[BinderBlueprint[T]]

    Super Class:
        StructCarrier
    """
    
    def __init__():
        super().__init__()
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | BinderBlueprint[T]]:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[BinderBlueprint[T]]:
        pass


    