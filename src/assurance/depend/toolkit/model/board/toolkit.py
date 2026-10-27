# src/assurance/depend/toolkit/model/board/toolkit.py

"""
Module: assurance.depend.toolkit.model.board.toolkit
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelLayerToolkit, BoardServiceDependency
from domain import Board, BoardManifest, BoardNullWarningSet, BoardLayer


class BoardLayerToolkit(ModelLayerToolkit[Board]):
    """
    Role:
        - Toolkit

    Responsibilities:
        1.  Single source of truth for Board attribute validators and type manifest.

    Attributes:
        helper: BoardManifest
        manifest: BoardServiceDependency

    Provides:

    Super Class:
        ModelLayerToolkit
    """
    
    def __init__(
            self,
            manifest: Optional[BoardManifest] | None = None,
            dependency: Optional[BoardServiceDependency] | None = None,
    ):
        """
        Args:
            dependency: Optional[BoardManifest]
            manifest: Optional[BoardServiceDependency]
        """
        super().__init__(
            dependency=dependency or BoardServiceDependency(),
            manifest=manifest or BoardManifest(),
        )
    
    @property
    def dependency(self) -> BoardServiceDependency:
        return cast(BoardServiceDependency, super().dependency)
    
    @property
    def manifest(self) -> BoardManifest:
        return cast(BoardManifest, super().manifest)
    
    @property
    def nulls(self) -> BoardNullWarningSet:
        return self.manifest.nulls
    
    @property
    def types(self) -> BoardLayer:
        return self.manifest.types