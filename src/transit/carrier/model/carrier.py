# src/transit/carrier/model/carrier.py

"""
Module: transit.carrier.model.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from domain import Model, ModelBlueprint
from transit import EntityCarrier

T = TypeVar("T", bound="Model")


class ModelCarrier(EntityCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Model or its Blueprint.

    Attributes:

    Provides:
        -   def extract_blueprint() -> Optional[ModelBlueprint[T]]

    Super Class:
        EntityCarrier
    """
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[ModelBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[ModelBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[T | ModelBlueprint[T]]:
        if (
                self.is_empty or
                self.is_not_consistent
        ):
            return None
        if self.has_model:
            return cast(T, super().entity)
        return cast(ModelBlueprint[T], super().entity)

    
    @abstractmethod
    def extract_blueprint(self) -> Optional[ModelBlueprint[T]]:
        pass



    