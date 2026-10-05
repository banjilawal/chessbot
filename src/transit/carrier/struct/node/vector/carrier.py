# src/transit/carrier/struct/node/vector/carrier.py

"""
Module: transit.carrier.struct.node.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorNode, VectorNodeBlueprint
from transit import NodeCarrier


class VectorNodeCarrier(NodeCarrier[VectorNode]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated VectorNode its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [VectorNode | VectorNodeBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[VectorNodeBlueprint]

    Super Class:
        NodeCarrier
    """
    
    def __init__(
            self,
            model: Optional[VectorNode] | None = None,
            blueprint: Optional[VectorNodeBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[VectorNode]
            blueprint: Optional[VectorNodeBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[VectorNode | VectorNodeBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(VectorNode, entity)
        return cast(VectorNodeBlueprint, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, VectorNode)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, VectorNodeBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[VectorNodeBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(VectorNodeBlueprint, self.entity)
            return blueprint
        
        model = cast(VectorNode, self.entity)
        next_node = VectorNode()
        previous = VectorNode()
        
        if model.next is not None:
            next_node = model.next
        if model.previous is not None:
            previous = model.previous
        return VectorNodeBlueprint(
            payload=model.payload
        )


    