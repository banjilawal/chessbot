# src/domain/metadata/nulls/structure/register/coord/group.py

"""
Module: domain.metadata.nulls.structure.register.coord.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterNullGroup, CoordRegister
from err import CoordRegisterBlueprintNullException, CoordRegisterNullException


class CoordRegisterNullGroup(RegisterNullGroup[CoordRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CoordRegister's integrity cycle.

    Attributes:
        structure: CoordRegisterNullException
        blueprint: CoordRegisterBlueprintNullException

    Provides:

    Super Class:
        RegisterNullGroup
    """

    
    def __init__(
            self,
            structure: Optional[CoordRegisterNullException] | None = None,
            blueprint: Optional[CoordRegisterBlueprintNullException] | None = None,
    ):
        """
        Args:
            structure: Optional[CoordRegisterNullException]
            blueprint: Optional[CoordRegisterBlueprintNullException]
        """
        super().__init__(
            structure=structure or CoordRegisterNullException(),
            blueprint=blueprint or CoordRegisterBlueprintNullException(),
        )
        
    @property
    def structure(self) -> CoordRegisterNullException:
        return cast(CoordRegisterNullException, super().model)
    
    @property
    def model(self) -> CoordRegisterNullException:
        return self.structure
    
    @property
    def blueprint(self) -> CoordRegisterBlueprintNullException:
        return cast(CoordRegisterBlueprintNullException, super().blueprint)