# src/domain/metadata/manifest/scalar/manifest.py

"""
Module: domain.metadata.manifest.scalar.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Scalar, ScalarNullGroup, ScalarTypeUnion, ObjectManifest


class ScalarManifest(ObjectManifest[Scalar]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for an Scalar's security lifecycle.

     Attributes:
        type_union: ScalarTypeUnion
        null_group: ScalarNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            type_union: Optional[ScalarTypeUnion] | None = None,
            null_group: Optional[ScalarNullGroup] | None = None,
    ):
        """
        Args:
            type_union: Optional[ScalarTypeUnion]
            null_group: Optional[ScalarNullGroup]
        """
        super().__init__(
            type_union=type_union or ScalarTypeUnion(),
            null_group=null_group or ScalarNullGroup(),
        )
        
    @property
    def types(self) -> ScalarTypeUnion:
        return cast(ScalarTypeUnion, super().types)
    
    @property
    def nulls(self) -> ScalarNullGroup:
        return cast(ScalarNullGroup, super().nulls)