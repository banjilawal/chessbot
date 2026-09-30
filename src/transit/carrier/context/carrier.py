# src/transit/carrier/context/carrier.py

"""
Module: transit.carrier.context.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC
from typing import Generic, TypeVar

from domain import Context
from transit import EntityCarrier

T = TypeVar("T", bound="Context")


class ContextCarrier(EntityCarrier[TContext], ABC, Generic[TContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated ContextContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [T|Blueprint[TContext]Context]


    Provides:
        -   def extract_ContextBlueprint() -> Optional[Blueprint[TContext]Context]

    Super Class:
        EntityCarrier
    """
    
    def __init__(self):
        super().__init__()


    