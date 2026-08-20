# src/transit/node/carrier.py

"""
Module: transit.node.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication.blueprint import NodeBlueprint

from carrier import ModelCarrier
from node import SquareNode


class NodeCarrier(ModelCarrier[SquareNode]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Node or NodeBlueprint
    
    Attributes:
        model: Optional[Node]
        blueprint: Optional[NodeBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        ModelCarrier
    """
    _model: Optional[SquareNode]
    _blueprint: Optional[NodeBlueprint]
    
    def __init__(
            self,
            model: Optional[SquareNode] | None = None,
            blueprint: Optional[NodeBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Node]
            blueprint: Optional[NodeBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [SquareNode | NodeBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SquareNode)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, NodeBlueprint)
        )
        
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

