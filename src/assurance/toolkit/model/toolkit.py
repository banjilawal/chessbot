# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import ModelBlueprintLoader, ModelValidationWrapperDict, ValidatorToolkit
from domain import Model, ModelManifest, ModelNullGroup, ModelTypeUnion

T = TypeVar("T", bound="Model")


class ModelValidatorToolkit(ValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
        helper: HelperTable[T]
        metadata: ModelManifest[T]
        blueprint_loader: ModelBlueprintLoader[T]

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    
    def __init__(
            self,
            wrapper: ModelValidationWrapperDict[T],
            metadata: ModelManifest[T],
            blueprint_loader: ModelBlueprintLoader[T]
    ):
        """
        Args:
            wrapper: HelperTable[T]
            metadata: ModelManifest[T]
            blueprint_loader: ModelBlueprintLoader[T]
        """
        super().__init__(
            wrapper=wrapper,
            metadata=metadata,
            blueprint_loader=blueprint_loader,
        )
    
    @property
    def wrapper(self) -> ModelValidationWrapperDict[T]:
        return cast(ModelValidationWrapperDict[T], super().wrapper)
    
    @property
    def metadata(self) -> ModelManifest[T]:
        return cast(ModelManifest[T], super().metadata)
    
    @property
    def loader(self) -> ModelBlueprintLoader[T]:
        return cast(ModelBlueprintLoader[T], super().loader)
    
    @property
    def nulls(self) -> ModelNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> ModelTypeUnion[T]:
        return self.metadata.types
    
