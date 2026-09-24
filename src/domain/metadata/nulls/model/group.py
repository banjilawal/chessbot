# src/domain/metadata/nulls/model/group.py

"""
Module: domain.metadata.nulls.model.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Model, NullExceptionGroup
from err import ModelCarrierNullException, ModelBlueprintNullException, ModelNullException

T = TypeVar("T", bound="Model")

class ModelNullGroup(NullExceptionGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Model's integrity cycle.

    Attributes:
        model: ModelNullException
        carrier: ModelCarrierNullException
        blueprint: ModelBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: ModelNullException,
            carrier: ModelCarrierNullException,
            blueprint: ModelBlueprintNullException,
    ):
        """
        Args:
            model: ModelNullException
            carrier: ModelCarrierNullException
            blueprint: ModelBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)

        
    @property
    def model(self) -> ModelNullException:
        return cast(ModelNullException, super().model)
    
    @property
    def carrier(self) -> ModelCarrierNullException:
        return cast(ModelCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ModelBlueprintNullException:
        return cast(ModelBlueprintNullException, super().blueprint)