# src/assurance/toolkit/model/game/toolkit.py

"""
Module: assurance.toolkit.model.game.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, GameHelperTable
from domain import Game, GameManifest


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
            helper: Optional[GameHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[GameManifest]
            metadata: Optional[GameHelperTable]
        """
        super().__init__(
            helper=helper or GameHelperTable(),
            metadata=metadata or GameManifest(),
        )
    
    @property
    def attribute(self) -> GameHelperTable:
        return cast(GameHelperTable, super().attribute)
    
    @property
    def metadata(self) -> GameManifest:
        return cast(GameManifest, super().metadata)