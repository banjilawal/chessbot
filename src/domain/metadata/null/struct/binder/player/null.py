# src/domain/metadata/nulls/struct/binder/player/group.py

"""
Module: domain.metadata.nulls.struct.binder.player.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import BinderNullWarningSet, PlayerBinder
from err import (
    PlayerBinderBlueprintNullException, PlayerBinderCarrierNullException,
    PlayerBinderNullException
)


class PlayerBinderNullWarningSet(BinderNullWarningSet[PlayerBinder]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a PlayerBinder's integrity cycle.

    Attributes:
        model: PlayerBinderNullException
        carrier: PlayerBinderCarrierNullException
        blueprint:PlayerBinderBlueprintNullException

    Provides:

    Super Class:
        BinderNullGroup
    """

    
    def __init__(
            self,
            model: Optional[PlayerBinderNullException] | None = None,
            carrier: Optional[PlayerBinderCarrierNullException] | None = None,
            blueprint: Optional[PlayerBinderBlueprintNullException] | None = None,
    ):
        """
        Args:
            model: Optional[PlayerBinderNullException]
            carrier: Optional[PlayerBinderCarrierNullException]
            blueprint: Optional[PlayerBinderBlueprintNullException]
        """
        super().__init__(
            model=model or PlayerBinderNullException(),
            carrier=carrier or PlayerBinderCarrierNullException(),
            blueprint=blueprint or PlayerBinderBlueprintNullException(),
        )
        
    @property
    def struct(self) -> PlayerBinderNullException:
        return cast(PlayerBinderNullException, super().model)
    
    @property
    def model(self) -> PlayerBinderNullException:
        return self.struct
    
    @property
    def carrier(self) -> PlayerBinderCarrierNullException:
        return cast(PlayerBinderCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> PlayerBinderBlueprintNullException:
        return cast(PlayerBinderBlueprintNullException, super().blueprint)