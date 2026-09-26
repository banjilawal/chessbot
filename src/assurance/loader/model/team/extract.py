# src/assurance/loader/model/team/extract.py

"""
Module: assurance.loader.model.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from domain import Blueprint
from transit import EntityCarrier

T = TypeVar("T")

class LoaderExtract(ABC, Generic[T]):
    _carrier: EntityCarrier[T]
    _blueprint: Optional[Blueprint[T]]
    _model: Optional[T]

    
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
        self._model = model
        self._carrier = carrier
        self._blueprint = blueprint
        
    @property
    def carrier(self) -> EntityCarrier[T]:
        return self._carrier
    
    @property
    def model(self) -> Optional[T]:
        return self._model
    
    @property
    def blueprint(self) -> Optional[Blueprint[T]]:
        return self._blueprint
    
    @property
    def is_model_load(self) -> bool:
        if self._model is None:
            return False
        if (
                self.model is None or
                not isinstance(self.model, T)
        ):
            return False
        return self.model
    
    @property
    def is_blueprint_load(self) -> bool:
        if self._blueprint is None:
            return False
        if (
                self.blueprint is None or
                not isinstance(self.blueprint, Blueprint[T])
        ):
            return False
        return self.blueprint