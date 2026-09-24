# src/domain/metadata/manifest/model/scalar/manifest.py

"""
Module: domain.metadata.manifest.model.scalar.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Scalar, ScalarNullGroup, ScalarTypeUnion, ModelManifest


class ScalarManifest(ModelManifest[Scalar]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Scalar security lifecycle.

     Attributes:
        types: ScalarTypeUnion
        nulls: ScalarNullGroup

     Provides:

     Super Class:
        ModelManifest
     """
    
    def __init__(
            self,
            types: Optional[ScalarTypeUnion] | None = None,
            nulls: Optional[ScalarNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[ScalarTypeUnion]
            nulls: Optional[ScalarNullGroup]
        """
        super().__init__(
            types=types or ScalarTypeUnion(),
            nulls=nulls or ScalarNullGroup(),
        )
        
    @property
    def types(self) -> ScalarTypeUnion:
        return cast(ScalarTypeUnion, super().types)
    
    @property
    def nulls(self) -> ScalarNullGroup:
        return cast(ScalarNullGroup, super().nulls)