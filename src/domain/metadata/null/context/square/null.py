# src/domain/metadata/null/context/square/null.py

"""
Module: domain.metadata.null.context.square.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullWarningSet, Square
from err import (
    SquareContextBlueprintNullException, SquareContextCarrierNullException, SquareContextNullException
)


class SquareContextNullWarningSet(ContextNullWarningSet[SquareContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Square's integrity cycle.

    Attributes:
        model: SquareContextNullException
        carrier: SquareContextCarrierNullException
        blueprint: SquareContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[SquareContextNullException] | None = None,
            carrier: Optional[SquareContextCarrierNullException] | None = None,
            blueprint: Optional[SquareContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[SquareContextNullException]
            carrier: Optional[SquareContextCarrierNullException]
            blueprint: Optional[SquareContextBlueprintNullException]
        """
        super().__init__(
            model=model or SquareContextNullException(),
            carrier=carrier or SquareContextCarrierNullException(),
            blueprint=blueprint or SquareContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> SquareContextNullException:
        return cast(SquareContextNullException, super().model)
    
    @property
    def carrier(self) -> SquareContextCarrierNullException:
        return cast(SquareContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> SquareContextBlueprintNullException:
        return cast(SquareContextBlueprintNullException, super().blueprint)