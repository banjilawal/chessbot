# src/domain/metadata/nulls/struct/binder/group.py

"""
Module: domain.metadata.nulls.struct.binder.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import ArchetypeBinder, StructNullGroup
from err import (
    BinderBlueprintNullException, ArchetypeBinderNullException, BinderCarrierNullException
)

T = TypeVar("T", bound="ArchetypeBinder")

class BinderNullGroup(StructNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Binder's integrity cycle.

    Attributes:
        model: ArchetypeBinderNullException
        carrier: BinderCarrierNullException
        blueprint: BinderBlueprintNullException

    Provides:

    Super Class:
        StructNullGroup
    """

    
    def __init__(
            self,
            model: ArchetypeBinderNullException,
            carrier: BinderCarrierNullException,
            blueprint: BinderBlueprintNullException,
    ):
        """
        Args:
            model: ArchetypeBinderNullException
            carrier: BinderCarrierNullException
            blueprint: BinderBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
        
    @property
    def struct(self) -> ArchetypeBinderNullException:
        return cast(ArchetypeBinderNullException, super().model)
    
    @property
    def model(self) -> ArchetypeBinderNullException:
        return self.struct
    
    @property
    def carrier(self) -> BinderCarrierNullException:
        return cast(BinderCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> BinderBlueprintNullException:
        return cast(BinderBlueprintNullException, super().blueprint)