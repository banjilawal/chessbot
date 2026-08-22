# src/domain/transit/space/reservoir/__init__.py

"""
Module: domain.transit.space.reservoir.__init__
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from carrier import EntityCarrier

T = TypeVar("T", bound="SpaceReservoir")

class SpaceReservoirCarrier(EntityCarrier, Generic[T], ABC):
    """
    Role:
        -   Data Transport

    Responsibilities:
        1.  Transport either:
            -   a SpaceReservoir[T]
            -   a SpaceReservoirReservoirBlueprint[T]

    Attributes:
        is_carrying_model: bool
        is_carrying_blueprint: bool
        is_not_carrying_anything: bool
        is_carrying_too_much: bool

        entity: [SpaceReservoir[T]| SpaceReservoirReservoirBlueprint[T] | None]

    Provides:
        -   def extract_blueprint() -> Optional[SpaceReservoirBlueprint[T]]

    Super Class:
        EntityCarrier
    """
    def __init__(self, ):
        super().__init__()


    