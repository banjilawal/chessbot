# src/domain/metadata/manifest/struct/register/square/manifest.py

"""
Module: domain.metadata.manifest.struct.register.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterManifest, SquareRegister, SquareRegisterNullWarningSet, SquareRegisterLayer


class SquareRegisterManifest(RegisterManifest[SquareRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the SquareRegister
            security lifecycle.

     Attributes:
        types: SquareRegisterTypeUnion
        nulls: SquareRegisterNullGroup

     Provides:

     Super Class:
        DomainManifest
     """
    
    def __init__(
            self,
            types: Optional[SquareRegisterLayer] | None = None,
            nulls: Optional[SquareRegisterNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[SquareRegisterTypeUnion]
            nulls: Optional[SquareRegisterNullGroup]
        """
        super().__init__(
            types=types or SquareRegisterLayer(),
            nulls=nulls or SquareRegisterNullWarningSet(),
        )

        
    @property
    def types(self) -> SquareRegisterLayer:
        return cast(SquareRegisterLayer, super().types)
    
    @property
    def nulls(self) -> SquareRegisterNullWarningSet:
        return cast(SquareRegisterNullWarningSet, super().nulls)