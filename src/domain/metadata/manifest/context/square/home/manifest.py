# src/domain/metadata/context/manifest/context/square/home/manifest.py

"""
Module: domain.metadata.manifest.context.square.home.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HomeSquareContextNullGroup, HomeSquareContextTypeUnion, SquareContextManifest


class HomeSquareContextManifest(SquareContextManifest):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and ContextTypeUnions for the HOmeSquare
            security lifecycle.

     Attributes:
        types: HomeSquareContextTypeUnion
        nulls: HomeSquareContextNullGroup

     Provides:

     Super Class:
        SquareContextManifest
     """
    
    def __init__(
            self,
            types: Optional[HomeSquareContextTypeUnion] | None = None,
            nulls: Optional[HomeSquareContextNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[HomeSquareContextTypeUnion]
            nulls: Optional[HomeSquareContextNullGroup]
        """
        super().__init__(
            types=types or HomeSquareContextTypeUnion(),
            nulls=nulls or HomeSquareContextNullGroup(),
        )
        
    @property
    def types(self) -> HomeSquareContextTypeUnion:
        return cast(HomeSquareContextTypeUnion, super().types)
    
    @property
    def nulls(self) -> HomeSquareContextNullGroup:
        return cast(HomeSquareContextNullGroup, super().nulls)