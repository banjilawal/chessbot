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
from err import (
    CoordRegisterBlueprintNullException, CoordRegisterCarrierNullException,
    CoordRegisterNullException
)


class CoordRegisterNullGroup(RegisterNullGroup[CoordRegister]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a CoordRegister's integrity cycle.

    Attributes:
        model: CoordRegisterNullException
        carrier: CoordRegisterCarrierNullException
        blueprint:CoordRegisterBlueprintNullException

    Provides:

    Super Class:
        RegisterNullGroup
    """

    
    def __init__(
            self,
            model: Optional[CoordRegisterNullException] | None = None,
            carrier: Optional[CoordRegisterCarrierNullException] | None = None,
            blueprint: Optional[CoordRegisterBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[CoordRegisterNullException]
            carrier: Optional[CoordRegisterCarrierNullException]
            blueprint: Optional[CoordRegisterBlueprintNullException]
        """
        super().__init__(
            model=model or CoordRegisterNullException(),
            carrier=carrier or CoordRegisterCarrierNullException(),
            blueprint=blueprint or CoordRegisterBlueprintNullException(),
        )
        
    @property
    def structure(self) -> CoordRegisterNullException:
        return cast(CoordRegisterNullException, super().model)
    
    @property
    def model(self) -> CoordRegisterNullException:
        return self.structure
    
    @property
    def carrier(self) -> CoordRegisterCarrierNullException:
        return cast(CoordRegisterCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> CoordRegisterBlueprintNullException:
        return cast(CoordRegisterBlueprintNullException, super().blueprint)