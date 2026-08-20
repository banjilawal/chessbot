# src/transit/space/axis/carrier.py

"""
Module: transit.space.axis.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from carrier import SpaceCarrier

T = TypeVar("T", bound="Axis")


class AxisCarrier(SpaceCarrier, ABC, Generic[T]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        1.  Transports either a Space or its Blueprint.

    Attributes:
        is_space_carrier: bool
        is_blueprint_carrier: bool
        
        entity: [T | Blueprint[T]]
        is_empty: bool
        has_overflow: bool
        to_dict: Dict[str, Any]
        size: int

    Provides:
        -   extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
       EntityCarrier
    """
    def __init__(self):
        super().__init__()


    