# src/carrier/edge/operand.py

"""
Module: carrier.edge.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import EdgeBlueprint
from model import Edge
from chooser import EntityCarrier


class EdgeCarrier(EntityCarrier[Edge]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Edge or EdgeBlueprint
    
    Attributes:
        model: Optional[Edge]
        blueprint: Optional[EdgeBlueprint]
        is_model_operand: bool
        is_blueprint_operand: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        EntityOperand
    """
    _model: Optional[Edge]
    _blueprint: Optional[EdgeBlueprint]
    
    def __init__(
            self,
            model: Optional[Edge] | None = None,
            blueprint: Optional[EdgeBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Edge]
            blueprint: Optional[EdgeBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Edge | EdgeBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_operand(self) -> bool:
        return self._model is not None and self._blueprint is None
    
    @property
    def is_blueprint_operand(self) -> bool:
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
        if self.is_model_operand or self.is_blueprint_operand: return 1
        return 2
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, EdgeCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

