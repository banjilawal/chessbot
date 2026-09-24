# src/domain/metadata/manifest/strcture/register/square/manifest.py

"""
Module: domain.metadata.manifest.structure.register.square.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterManifest, SquareRegister, SquareRegisterNullGroup, SquareRegisterTypeUnion


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
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[SquareRegisterTypeUnion] | None = None,
            nulls: Optional[SquareRegisterNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[SquareRegisterTypeUnion]
            nulls: Optional[SquareRegisterNullGroup]
        """
        super().__init__(
            types=types or SquareRegisterTypeUnion(),
            nulls=nulls or SquareRegisterNullGroup(),
        )

        
    @property
    def types(self) -> SquareRegisterTypeUnion:
        return cast(SquareRegisterTypeUnion, super().types)
    
    @property
    def nulls(self) -> SquareRegisterNullGroup:
        return cast(SquareRegisterNullGroup, super().nulls)