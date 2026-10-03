# src/transit/carrier/structure/chart/carrier.py

"""
Module: transit.carrier.structure.chart.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC
from typing import Generic, TypeVar

from domain import ParticipantChart
from transit import StructureCarrier

T = TypeVar("T", bound="ParticipantChart")


class ChartCarrier(StructureCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Chart its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [T | ChartBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[ChartBlueprint[T]]

    Super Class:
        StructureCarrier
    """
    
    def __init__(self):
        super().__init__()


    