# src/domain/metadata/manifest/struct/register/vector/manifest.py

"""
Module: domain.metadata.manifest.struct.register.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterManifest, VectorRegister, VectorRegisterNullWarningSet, VectorRegisterLayer


class VectorRegisterManifest(RegisterManifest[VectorRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the VectorRegister
            security lifecycle.

     Attributes:
        types: VectorRegisterTypeUnion
        nulls: VectorRegisterNullGroup

     Provides:

     Super Class:
        DomainManifest
     """
    
    def __init__(
            self,
            types: Optional[VectorRegisterLayer] | None = None,
            nulls: Optional[VectorRegisterNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[VectorRegisterTypeUnion]
            nulls: Optional[VectorRegisterNullGroup]
        """
        super().__init__(
            types=types or VectorRegisterLayer(),
            nulls=nulls or VectorRegisterNullWarningSet(),
        )

        
    @property
    def types(self) -> VectorRegisterLayer:
        return cast(VectorRegisterLayer, super().types)
    
    @property
    def nulls(self) -> VectorRegisterNullWarningSet:
        return cast(VectorRegisterNullWarningSet, super().nulls)