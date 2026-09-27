# src/assurance/depend/toolkit/model/board/toolkit.py

"""
Module: assurance.depend.toolkit.model.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelValidatorToolkit, BoardWrapperDependency
from domain import Board, BoardManifest, BoardNullGroup, BoardTypeUnion


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
            wrapper: Optional[BoardWrapperDependency] | None = None,
    ):
        """
        Args:
            wrapper: Optional[BoardManifest]
            metadata: Optional[BoardHelperTable]
        """
        super().__init__(
            wrapper=wrapper or BoardWrapperDependency(),
            metadata=metadata or BoardManifest(),
        )
    
    @property
    def wrapper(self) -> BoardWrapperDependency:
        return cast(BoardWrapperDependency, super().wrapper)
    
    @property
    def metadata(self) -> BoardManifest:
        return cast(BoardManifest, super().metadata)
    
    @property
    def nulls(self) -> BoardNullGroup:
        return self.metadata.nulls
    
    @property
    def types(self) -> BoardTypeUnion:
        return self.metadata.types