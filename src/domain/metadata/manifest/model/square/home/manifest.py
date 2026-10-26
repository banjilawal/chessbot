# src/domain/metadata/manifest/model/square/home/manifest.py

"""
Module: domain.metadata.manifest.model.square.home.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import HomeSquareNullWarningSet, HomeSquareTypeUnion, SquareManifest


class HomeSquareManifest(SquareManifest):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1. Aggregates NullExceptions and TypeUnions for the HOmeSquare
            security lifecycle.

     Attributes:
        types: HomeSquareTypeUnion
        nulls: HomeSquareNullGroup

     Provides:

     Super Class:
        SquareManifest
     """
    
    def __init__(
            self,
            types: Optional[HomeSquareTypeUnion] | None = None,
            nulls: Optional[HomeSquareNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[HomeSquareTypeUnion]
            nulls: Optional[HomeSquareNullGroup]
        """
        super().__init__(
            types=types or HomeSquareTypeUnion(),
            nulls=nulls or HomeSquareNullWarningSet(),
        )
        
    @property
    def types(self) -> HomeSquareTypeUnion:
        return cast(HomeSquareTypeUnion, super().types)
    
    @property
    def nulls(self) -> HomeSquareNullWarningSet:
        return cast(HomeSquareNullWarningSet, super().nulls)