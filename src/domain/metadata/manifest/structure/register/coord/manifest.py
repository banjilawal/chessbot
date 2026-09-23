# src/domain/metadata/manifest/strcture/register/coord/manifest.py

"""
Module: domain.metadata.manifest.structure.register.coord.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import RegisterManifest, CoordRegister, CoordRegisterNullGroup, CoordRegisterTypeUnion


class CoordRegisterManifest(RegisterManifest[CoordRegister]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for a CoordRegister's 
            security lifecycle.

     Attributes:
        types: CoordRegisterTypeUnion
        nulls: CoordRegisterNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[CoordRegisterTypeUnion] | None = None,
            nulls: Optional[CoordRegisterNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[CoordRegisterTypeUnion]
            nulls: Optional[CoordRegisterNullGroup]
        """
        super().__init__(
            types=types or CoordRegisterTypeUnion(),
            nulls=nulls or CoordRegisterNullGroup(),
        )

        
    @property
    def types(self) -> CoordRegisterTypeUnion:
        return cast(CoordRegisterTypeUnion, super().types)
    
    @property
    def nulls(self) -> CoordRegisterNullGroup:
        return cast(CoordRegisterNullGroup, super().nulls)