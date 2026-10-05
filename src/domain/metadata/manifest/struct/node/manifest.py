# src/domain/metadata/manifest/strcture/node/manifest.py

"""
Module: domain.metadata.manifest.struct.node.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Node, StructManifest, NodeNullGroup, NodeTypeUnion

T = TypeVar("T", bound="Node")

class NodeManifest(StructManifest[T], ABC, Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Aggregates NullExceptions and TypeUnions for the Node security lifecycle.

     Attributes:
        types: NodeTypeUnion[T]
        nulls: NodeNullGroup[T]

     Provides:

     Super Class:
        ObjectManifest
     """
    
    def __init__(
            self,
            types: NodeTypeUnion[T],
            nulls: NodeNullGroup[T],
    ):
        """
        Args:
            types: NodeTypeUnion[T]
            nulls: NodeNullGroup[T]
        """
        super().__init__(types=types, nulls=nulls,)

        
    @property
    def types(self) -> NodeTypeUnion[T]:
        return cast(NodeTypeUnion[T], super().types)
    
    @property
    def nulls(self) -> NodeNullGroup:
        return cast(NodeNullGroup, super().nulls)