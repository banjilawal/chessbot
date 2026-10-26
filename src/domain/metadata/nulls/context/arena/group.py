# src/domain/metadata/nulls/context/arena/group.py

"""
Module: domain.metadata.nulls.context.arena.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ContextNullGroup
from err import (
    ArenaContextBlueprintNullException, ArenaContextCarrierNullException, ArenaContextNullException
)


class ArenaContextNullGroup(ContextNullGroup[ArenaContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Arena's integrity cycle.

    Attributes:
        context: ArenaContextNullException
        carrier: ArenaContextCarrierNullException
        blueprint: ArenaContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[ArenaContextNullException] | None = None,
            carrier: Optional[ArenaContextCarrierNullException] | None = None,
            blueprint: Optional[ArenaContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[ArenaContextNullException]
            carrier: Optional[ArenaContextCarrierNullException]
            blueprint: Optional[ArenaContextBlueprintNullException]
        """
        super().__init__(
            context = context or ArenaContextNullException(),
            carrier = carrier or ArenaContextCarrierNullException(),
            blueprint = blueprint or ArenaContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> ArenaContextNullException:
        return cast(ArenaContextNullException, super().context)
    
    @property
    def carrier(self) -> ArenaContextCarrierNullException:
        return cast(ArenaContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ArenaContextBlueprintNullException:
        return cast(ArenaContextBlueprintNullException, super().blueprint)