# src/carrier/northwest/carrier.py

"""
Module: carrier.northwest.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import NorthwestQuadrantBlueprint
from carrier import SpaceCarrier
from geometry.space import NorthwestQuadrant


class NorthwestQuadrantCarrier(SpaceCarrier[NorthwestQuadrant]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        2.  Transports either a NorthwestQuadrant or its Blueprint.

    Attributes:
        model: Optional[NorthwestQuadrant]
        blueprint: Optional[NorthwestQuadrantBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[NorthwestQuadrantBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[NorthwestQuadrant] | None = None,
            blueprint: Optional[NorthwestQuadrantBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[NorthwestQuadrant]
            blueprint: Optional[NorthwestQuadrantBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [NorthwestQuadrant | NorthwestQuadrantBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, NorthwestQuadrant)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, NorthwestQuadrantBlueprint)
        )

    def extract_blueprint(self) -> Optional[NorthwestQuadrantBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return NorthwestQuadrantBlueprint(
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
        if isinstance(other, NorthwestQuadrantCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

