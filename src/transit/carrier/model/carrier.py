# src/transit/carrier/model/carrier.py

"""
Module: transit.carrier.model.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC
from typing import Generic, TypeVar

from domain import Model
from transit import EntityCarrier

T = TypeVar("T", bound="Model")


class ModelCarrier(EntityCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Model or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [T|Blueprint[T]]


    Provides:
        - def extract_blueprint() -> Optional[Blueprint[T]]

    Super Class:
        EntityCarrier
    """
    
    def __init__(self):
        super().__init__()


    