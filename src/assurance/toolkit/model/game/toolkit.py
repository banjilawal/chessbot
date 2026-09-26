# src/assurance/toolkit/model/game/toolkit.py

"""
Module: assurance.toolkit.model.game.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, GameValidationWrapperDict
from domain import Game, GameManifest, GameNullGroup, GameTypeUnion


class GameValidatorToolkit(ModelValidatorToolkit[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Game attribute validators and type metadata.

    Attributes:
        helper: GameManifest
        metadata: GameHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[GameManifest] | None = None,
            wrapper: Optional[GameValidationWrapperDict] | None = None,
    ):
        """
        Args:
            wrapper: Optional[GameManifest]
            metadata: Optional[GameHelperTable]
        """
        super().__init__(
            wrapper=wrapper or GameValidationWrapperDict(),
            metadata=metadata or GameManifest(),
        )
    
    @property
    def wrapper(self) -> GameValidationWrapperDict:
        return cast(GameValidationWrapperDict, super().wrapper)
    
    @property
    def metadata(self) -> GameManifest:
        return cast(GameManifest, super().metadata)
    
    @property
    def nulls(self) -> GameNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> GameTypeUnion:
        return self.metadata.types