# src/domain/metadata/null/model/square/null.py

"""
Module: domain.metadata.null.model.square.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ModelNullWarningSet, Square
from err import (
    SquareBlueprintNullException, SquareCarrierNullException, SquareNullException
)


class SquareNullWarningSet(ModelNullWarningSet[Square]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Square's integrity cycle.

    Attributes:
        model: SquareNullException
        carrier: SquareCarrierNullException
        blueprint: SquareBlueprintNullException

    Provides:

    Super Class:
        NullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[SquareNullException] | None = None,
            carrier: Optional[SquareCarrierNullException] | None = None,
            blueprint: Optional[SquareBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[SquareNullException]
            carrier: Optional[SquareCarrierNullException]
            blueprint: Optional[SquareBlueprintNullException]
        """
        super().__init__(
            model = model or SquareNullException(),
            carrier = carrier or SquareCarrierNullException(),
            blueprint = blueprint or SquareBlueprintNullException(),
        )
        
    @property
    def model(self) -> SquareNullException:
        return cast(SquareNullException, super().model)
    
    @property
    def carrier(self) -> SquareCarrierNullException:
        return cast(SquareCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> SquareBlueprintNullException:
        return cast(SquareBlueprintNullException, super().blueprint)