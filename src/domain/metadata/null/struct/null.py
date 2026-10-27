# src/domain/metadata/null/struct/null.py

"""
Module: domain.metadata.null.struct.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Struct, NullWarningSet
from err import (
    StructCarrierNullException, StructBlueprintNullException, StructNullException
)

T = TypeVar("T", bound="Struct")


class StructNullWarningSet(NullWarningSet[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Struct's integrity cycle.

    Attributes:
        model: StructNullException
        carrier: StructCarrierNullException
        blueprint: StructBlueprintNullException

    Provides:

    Super Class:
        NullWarningSet
    """
    
    def __init__(
            self,
            model: StructNullException,
            carrier: StructCarrierNullException,
            blueprint: StructBlueprintNullException,
    ):
        """
        Args:
            model: StructNullException
            carrier: StructCarrierNullException
            blueprint: StructBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
    
    @property
    def struct(self) -> StructNullException:
        return cast(StructNullException, super().model)
    
    @property
    def model(self) -> StructNullException:
        return self.struct
    
    @property
    def carrier(self) -> StructCarrierNullException:
        return cast(StructCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> StructBlueprintNullException:
        return cast(StructBlueprintNullException, super().blueprint)