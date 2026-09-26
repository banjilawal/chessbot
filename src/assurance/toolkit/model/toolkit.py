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

from assurance import ModelHelperTable, ValidatorToolkit
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

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    
    def __init__(
            self,
            helper: ModelHelperTable[T],
            metadata: ModelManifest[T],
    ):
        """
        Args:
            helper: HelperTable[T]
            metadata: ModelManifest[T]
        """
        super().__init__(helper=helper, metadata=metadata)
    
    @property
    def helper(self) -> ModelHelperTable[T]:
        return cast(ModelHelperTable[T], super().helper)
    
    @property
    def nulls(self) -> ModelNullGroup[T]:
        return self.metadata.nulls
    
    @property
    def types(self) -> ModelTypeUnion[T]:
        return self.metadata.types
    
    @property
    def metadata(self) -> ModelManifest[T]:
        return cast(ModelManifest[T], super().metadata)