# src/assurance/toolkit/model/toolkit.py

"""
Module: assurance.toolkit.model.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import BoardHelperTable, ModelValidationToolkit
from domain import Board, BoardManifest



class BoardValidationToolkit(ModelValidationToolkit[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Board attribute validators and type metadata.

    Attributes:
        helper: Optional[BoardManifest]
        metadata: Optional[BoardHelperTable]

    Provides:

    Super Class:
    """
    _metadata: BoardManifest
    _helper: BoardHelperTable
    
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
        self._helper = helper or BoardHelperTable()
        self._metadata = metadata or BoardManifest()
    
    @property
    def helper(self) -> BoardHelperTable:
        return cast(BoardHelperTable, super().helper)
    
    @property
    def metadata(self) -> BoardManifest:
        return cast(BoardManifest, super().metadata)
