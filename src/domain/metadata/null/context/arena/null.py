# src/domain/metadata/null/context/arena/null.py

"""
Module: domain.metadata.null.context.arena.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Arena, ContextNullWarningSet
from err import (
    ArenaContextBlueprintNullException, ArenaContextCarrierNullException, ArenaContextNullException
)


class ArenaContextNullWarningSet(ContextNullWarningSet[ArenaContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Arena's integrity cycle.

    Attributes:
        model: ArenaContextNullException
        carrier: ArenaContextCarrierNullException
        blueprint: ArenaContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[ArenaContextNullException] | None = None,
            carrier: Optional[ArenaContextCarrierNullException] | None = None,
            blueprint: Optional[ArenaContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[ArenaContextNullException]
            carrier: Optional[ArenaContextCarrierNullException]
            blueprint: Optional[ArenaContextBlueprintNullException]
        """
        super().__init__(
            model=model or ArenaContextNullException(),
            carrier=carrier or ArenaContextCarrierNullException(),
            blueprint=blueprint or ArenaContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> ArenaContextNullException:
        return cast(ArenaContextNullException, super().model)
    
    @property
    def carrier(self) -> ArenaContextCarrierNullException:
        return cast(ArenaContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ArenaContextBlueprintNullException:
        return cast(ArenaContextBlueprintNullException, super().blueprint)