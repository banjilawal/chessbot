# src/assurance/depend/toolkit/model/game/toolkit.py

"""
Module: assurance.depend.toolkit.model.game.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, GameWrapperDependency
from domain import Game, GameManifest, GameNullGroup, GameTypeUnion


class GameValidatorToolkit(ModelValidatorToolkit[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Game attribute validators and type metadata.

    Attributes:
        helper: GameManifest
        metadata: GameWrapperDependency

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[GameManifest] | None = None,
            wrapper: Optional[GameWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[GameManifest]
            metadata: Optional[GameWrapperDependency]
        """
        super().__init__(
            wrapper=wrapper or GameWrapperDependency(),
            metadata=metadata or GameManifest(),
        )
    
    @property
    def wrapper(self) -> GameWrapperDependency:
        return cast(GameWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> GameManifest:
        return cast(GameManifest, super().metadata)
    
    @property
    def nulls(self) -> GameNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> GameTypeUnion:
        return self.metadata.types