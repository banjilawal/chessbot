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

from domain import Register, StructureNullGroup
from err import RegisterBlueprintNullException, StructureNullException

T = TypeVar("T", bound="Register")

class RegisterNullGroup(StructureNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Register's integrity cycle.

    Attributes:
        structure: T
        blueprint: RegisterBlueprintNullException

    Provides:

    Super Class:
        StructureNullGroup
    """

    
    def __init__(
            self,
            structure: StructureNullException,
            blueprint: RegisterBlueprintNullException,
    ):
        """
        Args:
            structure: StructureNullException
            blueprint: RegisterBlueprintNullException
        """
        super().__init__(structure=structure)
        self._blueprint = blueprint
        
    @property
    def structure(self) -> StructureNullException:
        return cast(StructureNullException, super().model)
    
    @property
    def model(self) -> StructureNullException:
        return self.structure
    
    @property
    def blueprint(self) -> RegisterBlueprintNullException:
        return self._blueprint