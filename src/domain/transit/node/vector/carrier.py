# src/domain/transit/node/vector/carrier.py

"""
Module: domain.transit.node.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication import VectorNodeBlueprint
from domain.structures.node import VectorNode
from domain.transit import NodeCarrier


class VectorNodeCarrier(NodeCarrier):
    """
    Role:
        -   Boundary Carrier

    Responsibilities:
        1.  Transport either a hydrated VectorNode or its Blueprint across validation and other processing
            boundaries.
    
    Attributes:
        model: Optional[VectorNode]
        blueprint: Optional[VectorNodeBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        NodeCarrier
    """
    _model: Optional[VectorNode]
    _blueprint: Optional[VectorNodeBlueprint]
    
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
        super().__init__()
        self._model = model
        self._blueprint = blueprint
        
    @property
    def entity(self) -> Optional[VectorNode | VectorNodeBlueprint]:
        if self.is_not_carrying_anything:
            return None
        if self.is_carrying_model:
            return self._model
        return self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, VectorNode)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, VectorNodeBlueprint)
        )
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything
    
    def extract_blueprint(self) -> Optional[VectorNodeBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return VectorNodeBlueprint(vector=self._model.payload)

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorNodeCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

