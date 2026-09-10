# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import PlayerHelperTable, ModelValidatorToolkit
from domain import Player, PlayerManifest



class PlayerValidatorToolkit(ModelValidatorToolkit[Player]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Player attribute validators and type metadata.

    Attributes:
        helper: Optional[PlayerManifest]
        metadata: Optional[PlayerHelperTable]

    Provides:

    Super Class:
    """
    _metadata: PlayerManifest
    _helper: PlayerHelperTable
    
    def __init__(
            self,
            metadata: Optional[PlayerManifest] | None = None,
            helper: Optional[PlayerHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[PlayerManifest]
            metadata: Optional[PlayerHelperTable]
        """
        super().__init__(
            helper=helper or PlayerHelperTable(),
            metadata=metadata or PlayerManifest(),
        )
    
    @property
    def helper(self) -> PlayerHelperTable:
        return cast(PlayerHelperTable, super().helper)
    
    @property
    def metadata(self) -> PlayerManifest:
        return cast(PlayerManifest, super().metadata)
