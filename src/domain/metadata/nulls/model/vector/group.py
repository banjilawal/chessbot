# src/domain/metadata/nulls/model/vector/group.py

"""
Module: domain.metadata.nulls.model.vector.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import (
    VectorBlueprintNullException, VectorCarrierNullException, VectorNullException
)


class VectorNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Vector's integrity cycle.

    Attributes:
        model: VectorNullException
        carrier: VectorCarrierNullException
        blueprint: VectorBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[VectorNullException] | None = None,
            carrier: Optional[VectorCarrierNullException] | None = None,
            blueprint: Optional[VectorBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[VectorNullException]
            carrier: Optional[VectorCarrierNullException]
            blueprint: Optional[VectorBlueprintNullException]
        """
        super().__init__(
            model = model or VectorNullException(),
            carrier = carrier or VectorCarrierNullException(),
            blueprint = blueprint or VectorBlueprintNullException(),
        )
        
    @property
    def model(self) -> VectorNullException:
        return cast(VectorNullException, super().model)
    
    @property
    def carrier(self) -> VectorCarrierNullException:
        return cast(VectorCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> VectorBlueprintNullException:
        return cast(VectorBlueprintNullException, super().blueprint)