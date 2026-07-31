# src/carrier/space/reservoir/axis/carrier.py

"""
Module: carrier.space.reservoir.axis.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import AxisReservoirBlueprint
from carrier import SpaceReservoirCarrier
from geometry.space import AxisReservoir


class AxisReservoirCarrier(SpaceReservoirCarrier[AxisReservoir]):
    """
    Role:
        -   Data Transport

    Responsibilities:
        1.  Transport either:
            -   a AxisReservoir
            -   a AxisReservoirReservoirBlueprint

    Attributes:
        is_carrying_model: bool
        is_carrying_blueprint: bool
        is_not_carrying_anything: bool
        is_carrying_too_much: bool
        
        entity: [AxisReservoir| AxisReservoirReservoirBlueprint | None]

    Provides:
        -   def extract_blueprint() -> Optional[AxisReservoirBlueprint]

    Super Class:
        SpaceReservoirCarrier
    """
    _model: Optional[AxisReservoir]
    _blueprint: Optional[AxisReservoirBlueprint]
    
    def __init__(
            self,
            model: Optional[AxisReservoir] | None = None,
            blueprint: Optional[AxisReservoirBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[AxisReservoir]
            blueprint: Optional[AxisReservoirBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [AxisReservoir | AxisReservoirBlueprint] | None:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, AxisReservoir)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, AxisReservoirBlueprint)
        )
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything
    
    def extract_blueprint(self) -> Optional[AxisReservoirBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return AxisReservoirBlueprint(origin=self._model.origin,)
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, AxisReservoirCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)
            
    
            
    


    