# src/domain/metadata/unions/strcture/node/manifest.py

"""
Module: domain.metadata.unions.struct.node.manifest
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Type, TypeVar, cast

from domain import Node, NodeBlueprint, StructTypeUnion
from transit import NodeCarrier

T = TypeVar("T", bound="Node")


class NodeTypeUnion(StructTypeUnion[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of types associated with building and validating a Node.

    Attributes:
        model: Type[T]
        carrier: Type[EntityCarrier[T]]
        blueprint: Type[NodeBlueprint[T]]
        
    Provides:

    Super Class:
        StructTypeUnion
    """
    
    def __init__(
            self,
            model: Type[T],
            carrier: Type[NodeCarrier[T]],
            blueprint: Type[NodeBlueprint[T]],
    ):
        """
        Args:
            model: Type[T]
            carrier: Type[EntityCarrier[T]]
            blueprint: Type[NodeBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint, carrier=carrier)
        
    @property
    def model(self) -> Type[T]:
        return cast(Type[T], super().model)
    
    @property
    def carrier(self) -> Type[NodeCarrier[T]]:
        return cast(Type[NodeCarrier[T]], super().carrier)
    
    @property
    def blueprint(self) -> Type[NodeBlueprint[T]]:
        return cast(Type[NodeBlueprint[T]], super().blueprint)