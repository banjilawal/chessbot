# src/transit/carrier/struct/node/carrier.py

"""
Module: transit.carrier.struct.node.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar, cast

from domain import Node, NodeBlueprint
from transit import StructCarrier

T = TypeVar("T", bound="Node")


class NodeCarrier(StructCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Node its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[NodeBlueprint[T]]
        entity: [T | NodeBlueprint[T]]

    Provides:
        -   def extract_blueprint() -> Optional[NodeBlueprint[T]]

    Super Class:
        StructCarrier
    """
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[NodeBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[NodeBlueprint[T]]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | NodeBlueprint[T]]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(T, entity)
        return cast(NodeBlueprint[T], super().entity)
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[NodeBlueprint[T]]:
        pass


    