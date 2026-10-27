# src/domain/metadata/null/context/vector/null.py

"""
Module: domain.metadata.null.context.vector.null
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullWarningSet
from err import (
    VectorContextBlueprintNullException, VectorContextCarrierNullException, VectorContextNullException
)


class VectorContextNullWarningSet(ContextNullWarningSet[VectorContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Vector's integrity cycle.

    Attributes:
        model: VectorContextNullException
        carrier: VectorContextCarrierNullException
        blueprint: VectorContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullWarningSet
    """
    
    def __init__(
            self,
            model: Optional[VectorContextNullException] | None = None,
            carrier: Optional[VectorContextCarrierNullException] | None = None,
            blueprint: Optional[VectorContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[VectorContextNullException]
            carrier: Optional[VectorContextCarrierNullException]
            blueprint: Optional[VectorContextBlueprintNullException]
        """
        super().__init__(
            model=model or VectorContextNullException(),
            carrier=carrier or VectorContextCarrierNullException(),
            blueprint=blueprint or VectorContextBlueprintNullException(),
        )
        
    @property
    def model(self) -> VectorContextNullException:
        return cast(VectorContextNullException, super().model)
    
    @property
    def carrier(self) -> VectorContextCarrierNullException:
        return cast(VectorContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> VectorContextBlueprintNullException:
        return cast(VectorContextBlueprintNullException, super().blueprint)