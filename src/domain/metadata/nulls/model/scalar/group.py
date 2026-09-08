# src/domain/metadata/nulls/model/scalar/group.py

"""
Module: domain.metadata.nulls.model.scalar.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import (
    ScalarBlueprintNullException, ScalarCarrierNullException, ScalarNullException
)


class ScalarNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Scalar's integrity cycle.

    Attributes:
        model: ScalarNullException
        carrier: ScalarCarrierNullException
        blueprint: ScalarBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[ScalarNullException] | None = None,
            carrier: Optional[ScalarCarrierNullException] | None = None,
            blueprint: Optional[ScalarBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[ScalarNullException]
            carrier: Optional[ScalarCarrierNullException]
            blueprint: Optional[ScalarBlueprintNullException]
        """
        super().__init__(
            model = model or ScalarNullException(),
            carrier = carrier or ScalarCarrierNullException(),
            blueprint = blueprint or ScalarBlueprintNullException(),
        )
        
    @property
    def model(self) -> ScalarNullException:
        return cast(ScalarNullException, super().model)
    
    @property
    def carrier(self) -> ScalarCarrierNullException:
        return cast(ScalarCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ScalarBlueprintNullException:
        return cast(ScalarBlueprintNullException, super().blueprint)