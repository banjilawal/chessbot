# src/domain/metadata/nulls/struct/register/vector/group.py

"""
Module: domain.metadata.nulls.struct.register.vector.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterNullGroup, VectorRegister
from err import (
    VectorRegisterBlueprintNullException, VectorRegisterCarrierNullException,
    VectorRegisterNullException
)


class VectorRegisterNullGroup(RegisterNullGroup[VectorRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a VectorRegister's integrity cycle.

    Attributes:
        model: VectorRegisterNullException
        carrier: VectorRegisterCarrierNullException
        blueprint:VectorRegisterBlueprintNullException

    Provides:

    Super Class:
        RegisterNullGroup
    """

    
    def __init__(
            self,
            model: Optional[VectorRegisterNullException] | None = None,
            carrier: Optional[VectorRegisterCarrierNullException] | None = None,
            blueprint: Optional[VectorRegisterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[VectorRegisterNullException]
            carrier: Optional[VectorRegisterCarrierNullException]
            blueprint: Optional[VectorRegisterBlueprintNullException]
        """
        super().__init__(
            model=model or VectorRegisterNullException(),
            carrier=carrier or VectorRegisterCarrierNullException(),
            blueprint=blueprint or VectorRegisterBlueprintNullException(),
        )
        
    @property
    def struct(self) -> VectorRegisterNullException:
        return cast(VectorRegisterNullException, super().model)
    
    @property
    def model(self) -> VectorRegisterNullException:
        return self.struct
    
    @property
    def carrier(self) -> VectorRegisterCarrierNullException:
        return cast(VectorRegisterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> VectorRegisterBlueprintNullException:
        return cast(VectorRegisterBlueprintNullException, super().blueprint)