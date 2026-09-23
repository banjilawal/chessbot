# src/domain/metadata/nulls/structure/register/square/group.py

"""
Module: domain.metadata.nulls.structure.register.square.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterNullGroup, SquareRegister
from err import SquareRegisterBlueprintNullException, SquareRegisterNullException


class SquareRegisterNullGroup(RegisterNullGroup[SquareRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a SquareRegister's integrity cycle.

    Attributes:
        structure: SquareRegisterNullException
        blueprint: SquareRegisterBlueprintNullException

    Provides:

    Super Class:
        RegisterNullGroup
    """

    
    def __init__(
            self,
            structure: Optional[SquareRegisterNullException] | None = None,
            blueprint: Optional[SquareRegisterBlueprintNullException] | None = None,
    ):
        """
        Args:
            structure: Optional[SquareRegisterNullException]
            blueprint: Optional[SquareRegisterBlueprintNullException]
        """
        super().__init__(
            structure=structure or SquareRegisterNullException(),
            blueprint=blueprint or SquareRegisterBlueprintNullException(),
        )
        
    @property
    def structure(self) -> SquareRegisterNullException:
        return cast(SquareRegisterNullException, super().model)
    
    @property
    def model(self) -> SquareRegisterNullException:
        return self.structure
    
    @property
    def blueprint(self) -> SquareRegisterBlueprintNullException:
        return cast(SquareRegisterBlueprintNullException, super().blueprint)