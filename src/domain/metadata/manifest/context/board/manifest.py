# src/domain/metadata/context/manifest/context/board/manifest.py

"""
Module: domain.metadata.manifest.context.board.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, BoardContextNullGroup, BoardContextTypeUnion, ContextManifest


class BoardContextManifest(ContextManifest[Board]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and ContextTypeUnions for the Board security lifecycle.

     Attributes:
        types: BoardContextTypeUnion
        nulls: BoardContextNullGroup

     Provides:

     Super Class:
        ContextManifest
     """
    
    def __init__(
            self,
            types: Optional[BoardContextTypeUnion] | None = None,
            nulls: Optional[BoardContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[BoardContextTypeUnion]
            nulls: Optional[BoardContextNullGroup]
        """
        super().__init__(
            types=types or BoardContextTypeUnion(),
            nulls=nulls or BoardContextNullGroup(),
        )
        
    @property
    def types(self) -> BoardContextTypeUnion:
        return cast(BoardContextTypeUnion, super().types)
    
    @property
    def nulls(self) -> BoardContextNullGroup:
        return cast(BoardContextNullGroup, super().nulls)