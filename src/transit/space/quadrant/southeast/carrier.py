# src/transit/southeast/carrier.py

"""
Module: transit.southeast.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from fabrication.blueprint import SoutheastQuadrantBlueprint
from carrier import SpaceCarrier
from space import SoutheastQuadrant


class SoutheastQuadrantCarrier(SpaceCarrier[SoutheastQuadrant]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        2.  Transports either a SoutheastQuadrant or its Blueprint.

    Attributes:
        model: Optional[SoutheastQuadrant]
        blueprint: Optional[SoutheastQuadrantBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[SoutheastQuadrantBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[SoutheastQuadrant] | None = None,
            blueprint: Optional[SoutheastQuadrantBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[SoutheastQuadrant]
            blueprint: Optional[SoutheastQuadrantBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [SoutheastQuadrant | SoutheastQuadrantBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SoutheastQuadrant)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SoutheastQuadrantBlueprint)
        )

    def extract_blueprint(self) -> Optional[SoutheastQuadrantBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return SoutheastQuadrantBlueprint(
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
        if isinstance(other, SoutheastQuadrantCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

