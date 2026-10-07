# src/transit/carrier/model/rank/carrier.py

"""
Module: transit.carrier.model.rank.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, Optional, TypeVar

from domain import Rank, RankBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Rank")


class RankCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Rank or its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[RankBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[RankBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[T]
    _blueprint: Optional[RankBlueprint[T]]
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[RankBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[RankBlueprint[T]]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[T | RankBlueprint[T]]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None
        )
    
    def extract_blueprint(self) -> Optional[RankBlueprint[T]]:
        if self.is_empty or self.has_model:
            return None
        return self._blueprint