# src/domain/metadata/nulls/context/square/group.py

"""
Module: domain.metadata.nulls.context.square.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullGroup, Square
from err import (
    SquareContextBlueprintNullException, SquareContextCarrierNullException, SquareContextNullException
)


class SquareContextNullGroup(ContextNullGroup[SquareContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Square's integrity cycle.

    Attributes:
        context: SquareContextNullException
        carrier: SquareContextCarrierNullException
        blueprint: SquareContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[SquareContextNullException] | None = None,
            carrier: Optional[SquareContextCarrierNullException] | None = None,
            blueprint: Optional[SquareContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[SquareContextNullException]
            carrier: Optional[SquareContextCarrierNullException]
            blueprint: Optional[SquareContextBlueprintNullException]
        """
        super().__init__(
            context = context or SquareContextNullException(),
            carrier = carrier or SquareContextCarrierNullException(),
            blueprint = blueprint or SquareContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> SquareContextNullException:
        return cast(SquareContextNullException, super().context)
    
    @property
    def carrier(self) -> SquareContextCarrierNullException:
        return cast(SquareContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> SquareContextBlueprintNullException:
        return cast(SquareContextBlueprintNullException, super().blueprint)