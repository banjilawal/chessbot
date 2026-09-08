# src/domain/metadata/nulls/model/token/king/group.py

"""
Module: domain.metadata.nulls.model.token.king.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KingToken, TokenNullGroup
from err import (
    KingTokenBlueprintNullException, KingTokenCarrierNullException, KingTokenNullException
)


class KingTokenNullGroup(TokenNullGroup[KingToken]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a KingToken's integrity cycle.

    Attributes:
        model: KingTokenNullException
        carrier: KingTokenCarrierNullException
        blueprint: KingTokenBlueprintNullException

    Provides:

    Super Class:
        NullExceptionGroup
    """
    
    def __init__(
            self,
            model: Optional[KingTokenNullException] | None = None,
            carrier: Optional[KingTokenCarrierNullException] | None = None,
            blueprint: Optional[KingTokenBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[KingTokenNullException]
            carrier: Optional[KingTokenCarrierNullException]
            blueprint: Optional[KingTokenBlueprintNullException]
        """
        super().__init__(
            model = model or KingTokenNullException(),
            carrier = carrier or KingTokenCarrierNullException(),
            blueprint = blueprint or KingTokenBlueprintNullException(),
        )
        
    @property
    def model(self) -> KingTokenNullException:
        return cast(KingTokenNullException, super().model)
    
    @property
    def carrier(self) -> KingTokenCarrierNullException:
        return cast(KingTokenCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> KingTokenBlueprintNullException:
        return cast(KingTokenBlueprintNullException, super().blueprint)