# src/domain/metadata/unions/strcture/node/vector/manifest.py

"""
Module: domain.metadata.unions.struct.node.vector.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, Type, cast

from domain import NodeTypeUnion, VectorNode, VectorNodeBlueprint
from transit import EntityCarrier

class VectorNodeTypeUnion(NodeTypeUnion[VectorNode]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a VectorNode.

    Attributes:
        model: Type[VectorNode]
        carrier: Type[EntityCarrier[VectorNode]]
        blueprint: Type[VectorNodeBlueprint]
        
    Provides:

    Super Class:
        VectorNodeTypeUnion
    """
    
    def __init__(
            self,
            carrier: Type[EntityCarrier[VectorNode]],
            model: Optional[Type[VectorNode]] | None = None,
            blueprint: Optional[Type[VectorNodeBlueprint]] | None = None,
    ):
        """
        Args:
            model: Type[VectorNode]
            carrier: Type[EntityCarrier[VectorNode]]
            blueprint: Type[VectorNodeBlueprint]
        """
        super().__init__(
            model=model or VectorNode,
            blueprint=blueprint or VectorNodeBlueprint,
            carrier=carrier,
        )
        
    @property
    def model(self) -> Type[VectorNode]:
        return cast(Type[VectorNode], super().model)
    
    @property
    def carrier(self) -> Type[EntityCarrier[VectorNode]]:
        return cast(Type[EntityCarrier[VectorNode]], super().carrier)
    
    @property
    def blueprint(self) -> Type[VectorNodeBlueprint]:
        return cast(Type[VectorNodeBlueprint], super().model)