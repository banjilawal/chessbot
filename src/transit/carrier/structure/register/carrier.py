# src/transit/carrier/structure/register/carrier.py

"""
Module: transit.carrier.structure.register.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC
from typing import Generic, TypeVar

from domain import Register
from transit import StructureCarrier

T = TypeVar("T", bound="Register")


class RegisterCarrier(StructureCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Register its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [T | RegisterBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[RegisterBlueprint[T]]

    Super Class:
        StructureCarrier
    """
    
    def __init__(self):
        super().__init__()


    