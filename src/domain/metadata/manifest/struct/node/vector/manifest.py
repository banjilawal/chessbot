# src/domain/metadata/manifest/strcture/node/vector/manifest.py

"""
Module: domain.metadata.manifest.struct.node.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import NodeManifest, VectorNode, VectorNodeNullGroup, VectorNodeTypeUnion


class VectorNodeManifest(NodeManifest[VectorNode]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the VectorNode
            security lifecycle.

     Attributes:
        types: VectorNodeTypeUnion
        nulls: VectorNodeNullGroup

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: Optional[VectorNodeTypeUnion] | None = None,
            nulls: Optional[VectorNodeNullGroup] | None = None,
    ):
        """
        Args:
            types: Optional[VectorNodeTypeUnion]
            nulls: Optional[VectorNodeNullGroup]
        """
        super().__init__(
            types=types or VectorNodeTypeUnion(),
            nulls=nulls or VectorNodeNullGroup(),
        )

        
    @property
    def types(self) -> VectorNodeTypeUnion:
        return cast(VectorNodeTypeUnion, super().types)
    
    @property
    def nulls(self) -> VectorNodeNullGroup:
        return cast(VectorNodeNullGroup, super().nulls)