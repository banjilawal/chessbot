# src/transit/northeast/carrier.py

"""
Module: transit.northeast.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from fabrication.blueprint import NortheastQuadrantBlueprint
from carrier import SpaceCarrier
from space import NortheastQuadrant


class NortheastQuadrantCarrier(SpaceCarrier[NortheastQuadrant]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        2.  Transports either a NortheastQuadrant or its Blueprint.

    Attributes:
        model: Optional[NortheastQuadrant]
        blueprint: Optional[NortheastQuadrantBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[NortheastQuadrantBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[NortheastQuadrant] | None = None,
            blueprint: Optional[NortheastQuadrantBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[NortheastQuadrant]
            blueprint: Optional[NortheastQuadrantBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [NortheastQuadrant | NortheastQuadrantBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, NortheastQuadrant)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, NortheastQuadrantBlueprint)
        )

    def extract_blueprint(self) -> Optional[NortheastQuadrantBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return NortheastQuadrantBlueprint(
            origin=self._model.origin,
            terminus=self._model.terminus,
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
        if isinstance(other, NortheastQuadrantCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

