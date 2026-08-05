# src/transit/southwest/carrier.py

"""
Module: transit.southwest.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from fabrication.blueprint import SouthwestQuadrantBlueprint
from carrier import SpaceCarrier
from space import SouthwestQuadrant


class SouthwestQuadrantCarrier(SpaceCarrier[SouthwestQuadrant]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        2.  Transports either a SouthwestQuadrant or its Blueprint.

    Attributes:
        model: Optional[SouthwestQuadrant]
        blueprint: Optional[SouthwestQuadrantBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[SouthwestQuadrantBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[SouthwestQuadrant] | None = None,
            blueprint: Optional[SouthwestQuadrantBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[SouthwestQuadrant]
            blueprint: Optional[SouthwestQuadrantBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [SouthwestQuadrant | SouthwestQuadrantBlueprint]:
        return self.model or self.blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self.model is not None and
                self.blueprint is None and
                isinstance(self._model, SouthwestQuadrant)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SouthwestQuadrantBlueprint)
        )

    def extract_blueprint(self) -> Optional[SouthwestQuadrantBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return SouthwestQuadrantBlueprint(
            origin=self.model.origin,
            terminus=self.model.terminus,
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
        if isinstance(other, SouthwestQuadrantCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

