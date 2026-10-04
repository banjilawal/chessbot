# src/domain/extract/struct/node/extract.py

"""
Module: domain.extract.struct.node.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar, cast

from domain import StructPrimeExtract, Node, NodeBlueprint
from transit import NodeCarrier

T = TypeVar("T", bound="Node")

class NodePrimeExtract(StructPrimeExtract[T], Generic[T]):
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Persist Blueprint and Carrier data for NodeValidator.

    Attributes:
        carrier: NodeCarrier[T]
        blueprint: Optional[NodeBlueprint]

    Provides:

    Super Class:
        StructPrimeExtract
    """

    def __init__(
            self,
            carrier: NodeCarrier[T],
            blueprint: Optional[NodeBlueprint[T]] | None = None,
    ):
        """
        Args:
            carrier: NodeCarrier[T]
            blueprint: Optional[NodeBlueprint[T]]
        """
        super().__init__(carrier=carrier, blueprint=blueprint)
        
    @property
    def carrier(self) -> NodeCarrier[T]:
        return cast(NodeCarrier[T], super().carrier)
    
    @property
    def blueprint(self) -> Optional[NodeBlueprint[T]]:
        return cast(NodeBlueprint[T], super().blueprint)