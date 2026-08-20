# src/transit/edge/carrier.py

"""
Module: transit.edge.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication.blueprint import EdgeBlueprint
from carrier import ModelCarrier
from graph.component.edge import Edge


class EdgeCarrier(ModelCarrier[Edge]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Edge or EdgeBlueprint
    
    Attributes:
        model: Optional[Edge]
        blueprint: Optional[EdgeBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        ModelCarrier
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
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Edge | EdgeBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Edge)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, EdgeBlueprint)
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
        if isinstance(other, EdgeCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

