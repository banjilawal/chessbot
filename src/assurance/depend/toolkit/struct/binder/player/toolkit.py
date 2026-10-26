# src/assurance/depend/toolkit/struct/binder/player/toolkit.py

"""
Module: assurance.depend.toolkit.struct.binder.player.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import BinderValidatorToolkit, PlayerBinderDependency
from domain import (
    PlayerBinder, PlayerBinderManifest, PlayerBinderNullWarningSet,
    PlayerBinderLayer
)


class PlayerBinderValidatorToolkit(BinderValidatorToolkit[PlayerBinder]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for attribute validators and type metadata.

    Attributes:
            wrapper: PlayerBinderDependency
            metadata: PlayerBinderManifest

    Provides:

    Super Class:
       BinderValidatorToolkit
    """
    
    def __init__(
            self,
            wrapper: Optional[PlayerBinderDependency] | None = None,
            metadata: Optional[PlayerBinderManifest] | None = None,
    ):
        """
            wrapper: Optional[PlayerBinderDependency]
            metadata: Optional[PlayerBinderManifest]
        """
        super().__init__(
            wrapper=wrapper or PlayerBinderDependency(),
            metadata=metadata or PlayerBinderManifest(),
        )
    
    @property
    def wrapper(self) -> PlayerBinderDependency:
        return cast(PlayerBinderDependency, super().wrapper)
    
    @property
    def metadata(self) -> PlayerBinderManifest:
        return cast(PlayerBinderManifest, super().metadata)
    
    @property
    def nulls(self) -> PlayerBinderNullWarningSet:
        return self.metadata.nulls
    
    @property
    def types(self) -> PlayerBinderLayer:
        return self.metadata.types