# src/domain/metadata/nulls/context/footstep/group.py

"""
Module: domain.metadata.nulls.context.footstep.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullGroup, Footstep
from err import (
    FootstepContextBlueprintNullException, FootstepContextCarrierNullException,
    FootstepContextNullException
)


class FootstepContextNullGroup(ContextNullGroup[FootstepContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Footstep's integrity cycle.

    Attributes:
        context: FootstepContextNullException
        carrier: FootstepContextCarrierNullException
        blueprint:FootstepContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullGroup
    """

    
    def __init__(
            self,
            context: Optional[FootstepContextNullException] | None = None,
            carrier: Optional[FootstepContextCarrierNullException] | None = None,
            blueprint: Optional[FootstepContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[FootstepContextNullException]
            carrier: Optional[FootstepContextCarrierNullException]
            blueprint: Optional[FootstepContextBlueprintNullException]
        """
        super().__init__(
            context=context or FootstepContextNullException(),
            carrier=carrier or FootstepContextCarrierNullException(),
            blueprint=blueprint or FootstepContextBlueprintNullException(),
        )
        
    @property
    def struct(self) -> FootstepContextNullException:
        return cast(FootstepContextNullException, super().context)
    
    @property
    def context(self) -> FootstepContextNullException:
        return self.struct
    
    @property
    def carrier(self) -> FootstepContextCarrierNullException:
        return cast(FootstepContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> FootstepContextBlueprintNullException:
        return cast(FootstepContextBlueprintNullException, super().blueprint)