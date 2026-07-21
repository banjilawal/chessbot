# src/carrier/node/operand.py

"""
Module: carrier.node.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import NodeBlueprint
from model import Node
from carrier import EntityCarrierToggle


class NodeCarrier(EntityCarrierToggle[Node]):
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
        EntityCarrierToggle
    """
    _model: Optional[Node]
    _blueprint: Optional[NodeBlueprint]
    
    def __init__(
            self,
            model: Optional[Node] | None = None,
            blueprint: Optional[NodeBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Node]
            blueprint: Optional[NodeBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Node | NodeBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_carrier(self) -> bool:
        return self._model is not None and self._blueprint is None
    
    @property
    def is_blueprint_carrier(self) -> bool:
        return self._model is None and self._blueprint is not None
    
    @property
    def is_empty(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def has_overflow(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def size(self) -> int:
        if self.no_active_toggles: return 0
        if self.is_model_carrier or self.is_blueprint_carrier: return 1
        return 2
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, NodeCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

