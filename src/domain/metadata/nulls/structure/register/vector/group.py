# src/domain/metadata/nulls/structure/register/vector/group.py

"""
Module: domain.metadata.nulls.structure.register.vector.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterNullGroup, VectorRegister
from err import VectorRegisterBlueprintNullException, VectorRegisterNullException


class VectorRegisterNullGroup(RegisterNullGroup[VectorRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a VectorRegister's integrity cycle.

    Attributes:
        structure: VectorRegisterNullException
        blueprint: VectorRegisterBlueprintNullException

    Provides:

    Super Class:
        RegisterNullGroup
    """

    
    def __init__(
            self,
            structure: Optional[VectorRegisterNullException] | None = None,
            blueprint: Optional[VectorRegisterBlueprintNullException] | None = None,
    ):
        """
        Args:
            structure: Optional[VectorRegisterNullException]
            blueprint: Optional[VectorRegisterBlueprintNullException]
        """
        super().__init__(
            structure=structure or VectorRegisterNullException(),
            blueprint=blueprint or VectorRegisterBlueprintNullException(),
        )
        
    @property
    def structure(self) -> VectorRegisterNullException:
        return cast(VectorRegisterNullException, super().model)
    
    @property
    def model(self) -> VectorRegisterNullException:
        return self.structure
    
    @property
    def blueprint(self) -> VectorRegisterBlueprintNullException:
        return cast(VectorRegisterBlueprintNullException, super().blueprint)