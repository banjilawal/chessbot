# src/domain/metadata/nulls/context/scalar/group.py

"""
Module: domain.metadata.nulls.context.scalar.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import ContextNullGroup
from err import (
    ScalarContextBlueprintNullException, ScalarContextCarrierNullException, ScalarContextNullException
)


class ScalarContextNullGroup(ContextNullGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with an Scalar's integrity cycle.

    Attributes:
        context: ScalarContextNullException
        carrier: ScalarContextCarrierNullException
        blueprint: ScalarContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[ScalarContextNullException] | None = None,
            carrier: Optional[ScalarContextCarrierNullException] | None = None,
            blueprint: Optional[ScalarContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[ScalarContextNullException]
            carrier: Optional[ScalarContextCarrierNullException]
            blueprint: Optional[ScalarContextBlueprintNullException]
        """
        super().__init__(
            context = context or ScalarContextNullException(),
            carrier = carrier or ScalarContextCarrierNullException(),
            blueprint = blueprint or ScalarContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> ScalarContextNullException:
        return cast(ScalarContextNullException, super().context)
    
    @property
    def carrier(self) -> ScalarContextCarrierNullException:
        return cast(ScalarContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ScalarContextBlueprintNullException:
        return cast(ScalarContextBlueprintNullException, super().blueprint)