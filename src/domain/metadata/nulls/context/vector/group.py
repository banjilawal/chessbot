# src/domain/metadata/nulls/context/vector/group.py

"""
Module: domain.metadata.nulls.context.vector.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullGroup, Vector
from err import (
    VectorContextBlueprintNullException, VectorContextCarrierNullException, VectorContextNullException
)


class VectorContextNullGroup(ContextNullGroup[VectorContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Vector's integrity cycle.

    Attributes:
        context: VectorContextNullException
        carrier: VectorContextCarrierNullException
        blueprint: VectorContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[VectorContextNullException] | None = None,
            carrier: Optional[VectorContextCarrierNullException] | None = None,
            blueprint: Optional[VectorContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[VectorContextNullException]
            carrier: Optional[VectorContextCarrierNullException]
            blueprint: Optional[VectorContextBlueprintNullException]
        """
        super().__init__(
            context = context or VectorContextNullException(),
            carrier = carrier or VectorContextCarrierNullException(),
            blueprint = blueprint or VectorContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> VectorContextNullException:
        return cast(VectorContextNullException, super().context)
    
    @property
    def carrier(self) -> VectorContextCarrierNullException:
        return cast(VectorContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> VectorContextBlueprintNullException:
        return cast(VectorContextBlueprintNullException, super().blueprint)