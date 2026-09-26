# src/assurance/loader/model/extract.py

"""
Module: assurance.loader.model.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar, cast

from assurance import Extract
from domain import Blueprint, Model, ModelBlueprint
from transit import EntityCarrier, ModelCarrier

T = TypeVar("T", bound="Model")

class ModelExtract(Extract[T], ABC, Generic[T]):

    def __(
            self,
            carrier: EntityCarrier[T],
            blueprint: Optional[Blueprint[T]],
            model: Optional[T],
    ):
        """
        Args:
            carrier: EntityCarrier[T]
            blueprint: Optional[Blueprint[T]]
            model: Optional[T]
        """
        super().__init__(
            carrier=carrier,
            blueprint=blueprint,
            model=model,
        )
        
    @property
    def carrier(self) -> ModelCarrier[T]:
        return cast(ModelCarrier[T], super().carrier)
    
    @property
    def model(self) -> Optional[T]:
        return cast(T, super().model)
    
    @property
    def blueprint(self) -> Optional[ModelBlueprint[T]]:
        return cast(ModelBlueprint[T], super().blueprint)
    
    @property
    def is_model_load(self) -> bool:
        if self._model is None:
            return False
        if (
                self.model is None or
                not isinstance(self.model, T)
        ):
            return False
        return True
    
    @property
    def is_blueprint_load(self) -> bool:
        if self._blueprint is None:
            return False
        if (
                self.blueprint is None or
                not isinstance(self.blueprint, Blueprint[T])
        ):
            return False
        return True