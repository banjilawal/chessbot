# src/domain/metadata/nulls/nulls.py

"""
Module: domain.metadata.nulls.nulls
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from domain import Model
from err import BlueprintNullException, EntityCarrierNullException, ModelNullException

T = TypeVar("T", bound="Model")

class NullExceptionGroup(ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Model's integrity cycle.

    Attributes:
        model: ModelNullException
        carrier: EntityCarrierNullException
        blueprint: BlueprintNullException

    Provides:

    Super Class:
    """
    _model: ModelNullException
    _carrier: EntityCarrierNullException
    _blueprint: BlueprintNullException
    
    def __init__(
            self,
            model: ModelNullException,
            carrier: EntityCarrierNullException,
            blueprint: BlueprintNullException,
    ):
        """
        Args:
            model: ModelNullException
            carrier: EntityCarrierNullException
            blueprint: BlueprintNullException
        """
        self._model = model
        self._carrier = carrier
        self._blueprint = blueprint
        
    @property
    def model(self) -> ModelNullException:
        return self._model
    
    @property
    def carrier(self) -> EntityCarrierNullException:
        return self._carrier
    
    @property
    def blueprint(self) -> BlueprintNullException:
        return self._blueprint