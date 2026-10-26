# src/domain/metadata/nulls/context/rank/knight/group.py

"""
Module: domain.metadata.nulls.context.rank.knight.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Knight, RankContextNullGroup
from err import (
    KnightContextBlueprintNullException, KnightContextCarrierNullException, KnightContextNullException
)


class KnightContextNullGroup(RankContextNullGroup[KnightContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a Knight's integrity cycle.

    Attributes:
        context: KnightContextNullException
        carrier: KnightContextCarrierNullException
        blueprint: KnightContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[KnightContextNullException] | None = None,
            carrier: Optional[KnightContextCarrierNullException] | None = None,
            blueprint: Optional[KnightContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[KnightContextNullException]
            carrier: Optional[KnightContextCarrierNullException]
            blueprint: Optional[KnightContextBlueprintNullException]
        """
        super().__init__(
            context = context or KnightContextNullException(),
            carrier = carrier or KnightContextCarrierNullException(),
            blueprint = blueprint or KnightContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> KnightContextNullException:
        return cast(KnightContextNullException, super().context)
    
    @property
    def carrier(self) -> KnightContextCarrierNullException:
        return cast(KnightContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KnightContextBlueprintNullException:
        return cast(KnightContextBlueprintNullException, super().blueprint)