# src/transit/carrier/structure/carrier.py

"""
Module: transit.carrier.structure.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import Structure, StructureBlueprint
from transit import EntityCarrier

T = TypeVar("T", bound="Structure")

class StructureCarrier(EntityCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Structure or its Blueprint.

    Attributes:
        entity: [T | StructureBlueprint[T]]


    Provides:
        -   def extract_blueprint() -> Optional[StructureBlueprint[T]]

    Super Class:
        EntityCarrier
    """
    
    def __init__(self):
        super().__init__()
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | StructureBlueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def has_model(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_blueprint(self) -> bool:
        pass

    
    @abstractmethod
    def extract_blueprint(self) -> Optional[StructureBlueprint[T]]:
        pass



    