# src/domain/metadata/nulls/model/arena/group.py

"""
Module: domain.metadata.nulls.model.arena.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NullExceptionGroup
from err import (
    ArenaBlueprintNullException, ArenaCarrierNullException, ArenaNullException
)


class ArenaNullGroup(NullExceptionGroup):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with an Arena's integrity cycle.

    Attributes:
        model: ArenaNullException
        carrier: ArenaCarrierNullException
        blueprint: ArenaBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[ArenaNullException] | None = None,
            carrier: Optional[ArenaCarrierNullException] | None = None,
            blueprint: Optional[ArenaBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[ArenaNullException]
            carrier: Optional[ArenaCarrierNullException]
            blueprint: Optional[ArenaBlueprintNullException]
        """
        super().__init__(
            model = model or ArenaNullException(),
            carrier = carrier or ArenaCarrierNullException(),
            blueprint = blueprint or ArenaBlueprintNullException(),
        )
        
    @property
    def model(self) -> ArenaNullException:
        return cast(ArenaNullException, super().model)
    
    @property
    def carrier(self) -> ArenaCarrierNullException:
        return cast(ArenaCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> ArenaBlueprintNullException:
        return cast(ArenaBlueprintNullException, super().blueprint)