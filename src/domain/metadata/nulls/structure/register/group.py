# src/domain/metadata/nulls/structure/register/group.py

"""
Module: domain.metadata.nulls.structure.register.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import StructureNullGroup
from err import EntityCarrierNullException, StructureNullException

T = TypeVar("T", bound="Structure")

class RegisterNullGroup(StructureNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Register's integrity cycle.

    Attributes:
        structure: StructureNullException
        carrier: EntityCarrierNullException
        blueprint: BlueprintNullException

    Provides:

    Super Class:
    """

    
    def __init__(
            self,
            structure: StructureNullException,
            carrier: EntityCarrierNullException,
            blueprint: BlueprintNullException,
    ):
        """
        Args:
            structure: StructureNullException
            carrier: EntityCarrierNullException
            blueprint: BlueprintNullException
        """
        super().__init__(structure=structure)
        self._carrier = carrier
        self._blueprint = blueprint
        
    @property
    def structure(self) -> StructureNullException:
        return cast(StructureNullException, super().model)
    
    @property
    def model(self) -> StructureNullException:
        return self.structure
    
    @property
    def carrier(self) -> EntityCarrierNullException:
        return self._carrier
    
    @property
    def blueprint(self) -> BlueprintNullException:
        return self._blueprint