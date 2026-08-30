# src/transit/carrier/space/carrier.py

"""
Module: transit.carrier.space.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from carrier import EntityCarrier

T = TypeVar("T", bound="Space")

class SpaceCarrier(EntityCarrier, Generic[T], ABC):
    """
    Role:
        - Data Transport

    Responsibilities:
        1.  Transport either:
            -  a Space[T]
            -  a SpaceBlueprint[T]

    Attributes:
        is_carrying_model: bool
        is_carrying_blueprint: bool
        is_empty: bool
        exceeds_capacity: bool

        entity: [Space[T]| SpaceBlueprint[T] | None]

    Provides:
        - def extract_blueprint() -> Optional[SpaceBlueprint[T]]

    Super Class:
        EntityCarrier
    """
    def __init__(self):
        super().__init__()


    