# src/domain/metadata/manifest/model/board/manifest.py

"""
Module: domain.metadata.manifest.model.board.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, BoardNullGroup, BoardTypeUnion, ModelManifest


class BoardManifest(ModelManifest[Board]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Board's security lifecycle.

     Attributes:
        types: BoardTypeUnion
        nulls: BoardNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[BoardTypeUnion] | None = None,
            nulls: Optional[BoardNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[BoardTypeUnion]
            nulls: Optional[BoardNullGroup]
        """
        super().__init__(
            types=types or BoardTypeUnion(),
            nulls=nulls or BoardNullGroup(),
        )
        
    @property
    def types(self) -> BoardTypeUnion:
        return cast(BoardTypeUnion, super().types)
    
    @property
    def nulls(self) -> BoardNullGroup:
        return cast(BoardNullGroup, super().nulls)