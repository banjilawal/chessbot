# src/domain/metadata/unions/structure/searchable/node/vector/manifest.py

"""
Module: domain.metadata.unions.structure.searchable.node.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from dataclasses import dataclass
from typing import Optional, Type

from domain import NodeTypeUnions, Context, VectorNode, VectorNodeBlueprint


@dataclass
class VectorNodeTypeUnions(NodeTypeUnions[VectorNode]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of data unions a Node uses in the domain.

    Attributes:
        model: Type[VectorNode] = VectorNode
        carrier: Type[VectorNodeCarrier] = VectorNodeCarrier
        blueprint: Type[VectorNodeBlueprint] = VectorNodeBlueprint
        search_context: Optional[SearchContext] = None
        
    Provides:

    Super Class:
        NodeUnionss
    """
    model: Type[VectorNode] = VectorNode
    carrier: Type[VectorNodeCarrier] = VectorNodeCarrier
    blueprint: Type[VectorNodeBlueprint] = VectorNodeBlueprint
    search_context: Optional[Context] = None
