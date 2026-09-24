# src/transit/carrier/structure/register/coord/carrier.py

"""
Module: transit.carrier.structure.register.coord.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CoordRegister, CoordRegisterBlueprint
from transit import RegisterCarrier


class CoordRegisterCarrier(RegisterCarrier[CoordRegister]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CoordRegister its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [CoordRegister | CoordRegisterBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[CoordRegisterBlueprint]

    Super Class:
        RegisterCarrier
    """
    
    _model: Optional[CoordRegister]
    _blueprint: Optional[CoordRegisterBlueprint]
    
    def __init__(
            self,
            model: Optional[CoordRegister] | None = None,
            blueprint: Optional[CoordRegisterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CoordRegister]
            blueprint: Optional[CoordRegisterBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[CoordRegister | CoordRegisterBlueprint]:
        if self.is_empty:
            return None
        if self.is_carrying_model:
            return self._model
        return self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, CoordRegister)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, CoordRegisterBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_over_capacity(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[CoordRegisterBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        structure = cast(CoordRegister, self._model)
        return CoordRegisterBlueprint(
            origin=structure.origin,
            destination=structure.destination,
        )


    