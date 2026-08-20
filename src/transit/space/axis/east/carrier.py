# src/transit/east/carrier.py

"""
Module: transit.east.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication.blueprint import EastAxisBlueprint
from carrier import SpaceCarrier
from space import EastAxis


class EastAxisCarrier(SpaceCarrier[EastAxis]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        2.  Transports either a EastAxis or its Blueprint.

    Attributes:
        model: Optional[EastAxis]
        blueprint: Optional[EastAxisBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[EastAxisBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[EastAxis] | None = None,
            blueprint: Optional[EastAxisBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[EastAxis]
            blueprint: Optional[EastAxisBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [EastAxis | EastAxisBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, EastAxis)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, EastAxisBlueprint)
        )

    def extract_blueprint(self) -> Optional[EastAxisBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return EastAxisBlueprint(
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
        if isinstance(other, EastAxisCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

