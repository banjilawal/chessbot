# src/carrier/north/carrier.py

"""
Module: carrier.north.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import NorthAxisBlueprint
from carrier import SpaceCarrier
from geometry.space import NorthAxis


class NorthAxisCarrier(SpaceCarrier[NorthAxis]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        2.  Transports either a NorthAxis or its Blueprint.

    Attributes:
        model: Optional[NorthAxis]
        blueprint: Optional[NorthAxisBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[NorthAxisBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[NorthAxis] | None = None,
            blueprint: Optional[NorthAxisBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[NorthAxis]
            blueprint: Optional[NorthAxisBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [NorthAxis | NorthAxisBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, NorthAxis)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, NorthAxisBlueprint)
        )

    def extract_blueprint(self) -> Optional[NorthAxisBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return NorthAxisBlueprint(
            origin=self._model.origin,
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
        if isinstance(other, NorthAxisCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

