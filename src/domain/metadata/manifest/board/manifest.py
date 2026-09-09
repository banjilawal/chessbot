# src/domain/metadata/manifest/board/manifest.py

"""
Module: domain.metadata.manifest.board.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Board, BoardNullGroup, BoardTypeUnion, ObjectManifest


class BoardManifest(ObjectManifest[Board]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Board's security lifecycle.

     Attributes:
        type_union: BoardTypeUnion
        null_group: BoardNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[BoardTypeUnion] | None = None,
            null_group: Optional[BoardNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[BoardTypeUnion]
            null_group: Optional[BoardNullGroup]
        """
        super().__init__(
            type_union=type_union or BoardTypeUnion(),
            null_group=null_group or BoardNullGroup(),
        )
        
    @property
    def type_union(self) -> BoardTypeUnion:
        return cast(BoardTypeUnion, super().type_union)
    
    @property
    def null_group(self) -> BoardNullGroup:
        return cast(BoardNullGroup, super().null_group)