# src/domain/metadata/manifest/struct/register/coord/manifest.py

"""
Module: domain.metadata.manifest.struct.register.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterManifest, CoordRegister, CoordRegisterNullWarningSet, CoordRegisterLayer


class CoordRegisterManifest(RegisterManifest[CoordRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the CoordRegister
            security lifecycle.

     Attributes:
        types: CoordRegisterTypeUnion
        nulls: CoordRegisterNullGroup

     Provides:

     Super Class:
        DomainManifest
     """
    
    def __init__(
            self,
            types: Optional[CoordRegisterLayer] | None = None,
            nulls: Optional[CoordRegisterNullWarningSet] | None = None,
    ):
        """
        Args:
            types: Optional[CoordRegisterTypeUnion]
            nulls: Optional[CoordRegisterNullGroup]
        """
        super().__init__(
            types=types or CoordRegisterLayer(),
            nulls=nulls or CoordRegisterNullWarningSet(),
        )

        
    @property
    def types(self) -> CoordRegisterLayer:
        return cast(CoordRegisterLayer, super().types)
    
    @property
    def nulls(self) -> CoordRegisterNullWarningSet:
        return cast(CoordRegisterNullWarningSet, super().nulls)