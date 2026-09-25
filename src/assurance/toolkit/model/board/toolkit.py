# src/assurance/toolkit/model/board/toolkit.py

"""
Module: assurance.toolkit.model.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, BoardHelperTable
from domain import Board, BoardManifest


class BoardValidatorToolkit(ModelValidatorToolkit[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Board attribute validators and type metadata.

    Attributes:
        helper: BoardManifest
        metadata: BoardHelperTable

    Provides:

    Super Class:
        ModelValidatorToolkit
    """
    
    def __init__(
            self,
            metadata: Optional[BoardManifest] | None = None,
            helper: Optional[BoardHelperTable] | None = None,
    ):
        """
        Args:
            helper: Optional[BoardManifest]
            metadata: Optional[BoardHelperTable]
        """
        super().__init__(
            helper=helper or BoardHelperTable(),
            metadata=metadata or BoardManifest(),
        )
    
    @property
    def attribute(self) -> BoardHelperTable:
        return cast(BoardHelperTable, super().attribute)
    
    @property
    def metadata(self) -> BoardManifest:
        return cast(BoardManifest, super().metadata)