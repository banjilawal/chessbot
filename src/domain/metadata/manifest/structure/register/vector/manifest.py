# src/domain/metadata/manifest/strcture/register/vector/manifest.py

"""
Module: domain.metadata.manifest.structure.register.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterManifest, VectorRegister, VectorRegisterNullGroup, VectorRegisterTypeUnion


class VectorRegisterManifest(RegisterManifest[VectorRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for a VectorRegister's 
            security lifecycle.

     Attributes:
        types: VectorRegisterTypeUnion
        nulls: VectorRegisterNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[VectorRegisterTypeUnion] | None = None,
            nulls: Optional[VectorRegisterNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[VectorRegisterTypeUnion]
            nulls: Optional[VectorRegisterNullGroup]
        """
        super().__init__(
            types=types or VectorRegisterTypeUnion(),
            nulls=nulls or VectorRegisterNullGroup(),
        )

        
    @property
    def types(self) -> VectorRegisterTypeUnion:
        return cast(VectorRegisterTypeUnion, super().types)
    
    @property
    def nulls(self) -> VectorRegisterNullGroup:
        return cast(VectorRegisterNullGroup, super().nulls)