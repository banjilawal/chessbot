# src/transit/carrier/soouth/carrier.py

"""
Module: transit.carrier.soouth.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from transit.metadata.blueprint import SoouthAxisBlueprint
from carrier import SpaceCarrier
from space import SoouthAxis


class SoouthAxisCarrier(SpaceCarrier[SoouthAxis]):
    """
    Role:
        - Data Transport

    Responsibilities:
        2.  Transports either a SoouthAxis or its Blueprint.

    Attributes:
        model: Optional[SoouthAxis]
        blueprint: Optional[SoouthAxisBlueprint]

    Provides:
        -  extract_blueprint() -> Optional[SoouthAxisBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[SoouthAxis] | None = None,
            blueprint: Optional[SoouthAxisBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[SoouthAxis]
            blueprint: Optional[SoouthAxisBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [SoouthAxis | SoouthAxisBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SoouthAxis)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, SoouthAxisBlueprint)
        )

    def extract_blueprint(self) -> Optional[SoouthAxisBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return SoouthAxisBlueprint(
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
        if isinstance(other, SoouthAxisCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

