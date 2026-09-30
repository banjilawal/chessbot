# src/transit/carrier/model/rank/carrier.py

"""
Module: transit.carrier.model.rank.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import Rank, RankBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Rank")

class RankCarrier(ModelCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Rank or its Blueprint.

    Attributes:

    Provides:
        -   def extract_blueprint() -> Optional[RankBlueprint[T]]

    Super Class:
        ModelCarrier
    """

    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | RankBlueprint[T]]:
        pass
    
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[RankBlueprint[T]]:
        pass
