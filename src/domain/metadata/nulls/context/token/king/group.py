# src/domain/metadata/nulls/context/token/king/group.py

"""
Module: domain.metadata.nulls.context.token.king.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KingToken, TokenContextNullGroup
from err import (
    KingTokenContextBlueprintNullException, KingTokenContextCarrierNullException, KingTokenContextNullException
)


class KingTokenContextNullGroup(TokenContextNullGroup[KingTokenContext]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of ContextNullExceptions associated with a KingToken's integrity cycle.

    Attributes:
        context: KingTokenContextNullException
        carrier: KingTokenContextCarrierNullException
        blueprint: KingTokenContextBlueprintNullException

    Provides:

    Super Class:
        ContextNullExceptionGroup
    """
    
    def __init__(
            self,
            context: Optional[KingTokenContextNullException] | None = None,
            carrier: Optional[KingTokenContextCarrierNullException] | None = None,
            blueprint: Optional[KingTokenContextBlueprintNullException] | None = None,
    ):
        """
        Args:
            context: Optional[KingTokenContextNullException]
            carrier: Optional[KingTokenContextCarrierNullException]
            blueprint: Optional[KingTokenContextBlueprintNullException]
        """
        super().__init__(
            context = context or KingTokenContextNullException(),
            carrier = carrier or KingTokenContextCarrierNullException(),
            blueprint = blueprint or KingTokenContextBlueprintNullException(),
        )
        
    @property
    def context(self) -> KingTokenContextNullException:
        return cast(KingTokenContextNullException, super().context)
    
    @property
    def carrier(self) -> KingTokenContextCarrierNullException:
        return cast(KingTokenContextCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KingTokenContextBlueprintNullException:
        return cast(KingTokenContextBlueprintNullException, super().blueprint)