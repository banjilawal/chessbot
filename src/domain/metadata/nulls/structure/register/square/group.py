# src/domain/metadata/nulls/struct/register/square/group.py

"""
Module: domain.metadata.nulls.struct.register.square.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterNullGroup, SquareRegister
from err import (
    SquareRegisterBlueprintNullException, SquareRegisterCarrierNullException,
    SquareRegisterNullException
)


class SquareRegisterNullGroup(RegisterNullGroup[SquareRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a SquareRegister's integrity cycle.

    Attributes:
        model: SquareRegisterNullException
        carrier: SquareRegisterCarrierNullException
        blueprint:SquareRegisterBlueprintNullException

    Provides:

    Super Class:
        RegisterNullGroup
    """

    
    def __init__(
            self,
            model: Optional[SquareRegisterNullException] | None = None,
            carrier: Optional[SquareRegisterCarrierNullException] | None = None,
            blueprint: Optional[SquareRegisterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[SquareRegisterNullException]
            carrier: Optional[SquareRegisterCarrierNullException]
            blueprint: Optional[SquareRegisterBlueprintNullException]
        """
        super().__init__(
            model=model or SquareRegisterNullException(),
            carrier=carrier or SquareRegisterCarrierNullException(),
            blueprint=blueprint or SquareRegisterBlueprintNullException(),
        )
        
    @property
    def struct(self) -> SquareRegisterNullException:
        return cast(SquareRegisterNullException, super().model)
    
    @property
    def model(self) -> SquareRegisterNullException:
        return self.struct
    
    @property
    def carrier(self) -> SquareRegisterCarrierNullException:
        return cast(SquareRegisterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> SquareRegisterBlueprintNullException:
        return cast(SquareRegisterBlueprintNullException, super().blueprint)