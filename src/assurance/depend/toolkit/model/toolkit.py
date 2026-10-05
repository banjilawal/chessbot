# src/assurance/depend/toolkit/model/toolkit.py

"""
Module: assurance.depend.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from assurance import ModelLoader, ModelWrapperDependency, ValidatorToolkit
from domain import Model, ModelManifest, ModelNullGroup, ModelTypeUnion

T = TypeVar("T", bound="Model")


class ModelValidatorToolkit(ValidatorToolkit[T], ABC, Generic[T]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
        helper: WrapperDependency[T]
        metadata: ModelManifest[T]

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    
    def __init__(
            self,
            wrapper: ModelWrapperDependency[T],
            metadata: ModelManifest[T],
    ):
        """
        Args:
            wrapper: WrapperDependency[T]
            metadata: ModelManifest[T]
        """
        super().__init__(wrapper=wrapper, metadata=metadata)
    
    @property
    def wrapper(self) -> ModelWrapperDependency[T]:
        return cast(ModelWrapperDependency[T], super().wrapper)
    
    @property
    def metadata(self) -> ModelManifest[T]:
        return cast(ModelManifest[T], super().metadata)
    
    @property
    def nulls(self) -> ModelNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> ModelTypeUnion[T]:
        return self.metadata.types
    
