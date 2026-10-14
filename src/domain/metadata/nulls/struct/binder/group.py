# src/domain/metadata/nulls/struct/register/group.py

"""
Module: domain.metadata.nulls.struct.register.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Register, StructNullGroup
from err import (
    RegisterBlueprintNullException, RegisterCarrierNullException, RegisterNullException
)

T = TypeVar("T", bound="Register")

class RegisterNullGroup(StructNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Register's integrity cycle.

    Attributes:
        model: RegisterNullException
        carrier: RegisterCarrierNullException
        blueprint: RegisterBlueprintNullException

    Provides:

    Super Class:
        StructNullGroup
    """

    
    def __init__(
            self,
            model: RegisterNullException,
            carrier: RegisterCarrierNullException,
            blueprint: RegisterBlueprintNullException,
    ):
        """
        Args:
            model: RegisterNullException
            carrier: RegisterCarrierNullException
            blueprint: RegisterBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
        
    @property
    def struct(self) -> RegisterNullException:
        return cast(RegisterNullException, super().model)
    
    @property
    def model(self) -> RegisterNullException:
        return self.struct
    
    @property
    def carrier(self) -> RegisterCarrierNullException:
        return cast(RegisterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> RegisterBlueprintNullException:
        return cast(RegisterBlueprintNullException, super().blueprint)