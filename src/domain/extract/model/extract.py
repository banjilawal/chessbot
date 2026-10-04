# src/domain/extract/model/extract.py

"""
Module: domain.extract.model.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from domain import Model, ModelBlueprint, PrimeExtract
from transit import ModelCarrier

T = TypeVar("T", bound="Model")

class ModelPrimeExtract(PrimeExtract[T], ABC, Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for ModelValidator.

    Attributes:
        carrier: ModelCarrier[T]
        blueprint: Optional[ModelBlueprint[T]]

    Provides:
        blueprint_exists: bool
        no_blueprint_exists: bool

    Super Class:
        PrimeExtract
    """

    def __init__(
            self,
            carrier: ModelCarrier[T],
            blueprint: Optional[ModelBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: EntityCarrier[T]
            blueprint: Optional[Blueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> ModelCarrier[T]:
        return cast(ModelCarrier[T], super().carrier)
    
    @property
    def blueprint(self) -> Optional[ModelBlueprint[T]]:
        return cast(ModelBlueprint[T], super().blueprint)
    
