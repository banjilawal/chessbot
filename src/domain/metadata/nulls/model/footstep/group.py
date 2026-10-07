# src/domain/metadata/nulls/model/footstep/group.py

"""
Module: domain.metadata.nulls.model.footstep.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelNullGroup, Footstep
from err import (
    FootstepBlueprintNullException, FootstepCarrierNullException,
    FootstepNullException
)


class FootstepNullGroup(ModelNullGroup[Footstep]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Footstep's integrity cycle.

    Attributes:
        model: FootstepNullException
        carrier: FootstepCarrierNullException
        blueprint:FootstepBlueprintNullException

    Provides:

    Super Class:
        ModelNullGroup
    """

    
    def __init__(
            self,
            model: Optional[FootstepNullException] | None = None,
            carrier: Optional[FootstepCarrierNullException] | None = None,
            blueprint: Optional[FootstepBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[FootstepNullException]
            carrier: Optional[FootstepCarrierNullException]
            blueprint: Optional[FootstepBlueprintNullException]
        """
        super().__init__(
            model=model or FootstepNullException(),
            carrier=carrier or FootstepCarrierNullException(),
            blueprint=blueprint or FootstepBlueprintNullException(),
        )
        
    @property
    def struct(self) -> FootstepNullException:
        return cast(FootstepNullException, super().model)
    
    @property
    def model(self) -> FootstepNullException:
        return self.struct
    
    @property
    def carrier(self) -> FootstepCarrierNullException:
        return cast(FootstepCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> FootstepBlueprintNullException:
        return cast(FootstepBlueprintNullException, super().blueprint)