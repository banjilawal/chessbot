# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import GameHelperTable, ModelValidatorToolkit
from domain import Game, GameManifest



class GameValidatorToolkit(ModelValidatorToolkit[Game]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Game attribute validators and type metadata.

    Attributes:
        helper: Optional[GameManifest]
        metadata: Optional[GameHelperTable]

    Provides:

    Super Class:
    """
    _metadata: GameManifest
    _helper: GameHelperTable
    
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
        self._helper = helper or GameHelperTable()
        self._metadata = metadata or GameManifest()
    
    @property
    def helper(self) -> GameHelperTable:
        return cast(GameHelperTable, super().helper)
    
    @property
    def metadata(self) -> GameManifest:
        return cast(GameManifest, super().metadata)
