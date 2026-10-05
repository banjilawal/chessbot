# src/domain/metadata/nulls/struct/node/group.py

"""
Module: domain.metadata.nulls.struct.node.group
Author: Banji Lawal
Created: 2026-03-30
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar, cast

from domain import Node, StructNullGroup
from err import (
    NodeBlueprintNullException, NodeCarrierNullException, NodeNullException
)

T = TypeVar("T", bound="Node")

class NodeNullGroup(StructNullGroup[T], ABC, Generic[T]):
    """
    Role:
        - Metadata

    Responsibilities:
        1. Catalog of NullExceptions associated with a Node's integrity cycle.

    Attributes:
        model: NodeNullException
        carrier: NodeCarrierNullException
        blueprint: NodeBlueprintNullException

    Provides:

    Super Class:
        StructNullGroup
    """

    
    def __init__(
            self,
            model: NodeNullException,
            carrier: NodeCarrierNullException,
            blueprint: NodeBlueprintNullException,
    ):
        """
        Args:
            model: NodeNullException
            carrier: NodeCarrierNullException
            blueprint: NodeBlueprintNullException
        """
        super().__init__(model=model, carrier=carrier, blueprint=blueprint)
        
    @property
    def struct(self) -> NodeNullException:
        return cast(NodeNullException, super().model)
    
    @property
    def model(self) -> NodeNullException:
        return self.struct
    
    @property
    def carrier(self) -> NodeCarrierNullException:
        return cast(NodeCarrierNullException, super().carrier)
    
    @property
    def blueprint(self) -> NodeBlueprintNullException:
        return cast(NodeBlueprintNullException, super().blueprint)