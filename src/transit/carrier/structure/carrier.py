# src/transit/carrier/structure/carrier.py

"""
Module: transit.carrier.structure.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC
from typing import Generic, TypeVar

from domain import Structure
from transit import EntityCarrier

T = TypeVar("T", bound="Structure")


class StructureCarrier(EntityCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Structure or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [T | StructureBlueprint[T]]


    Provides:
        -   def extract_blueprint() -> Optional[StructureBlueprint[T]]

    Super Class:
        EntityCarrier
    """
    
    def __init__(self):
        super().__init__()


    