# src/transit/carrier/struct/register/coord/carrier.py

"""
Module: transit.carrier.struct.register.coord.carrier
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
        1.  Transport a hydrated CoordRegister its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [CoordRegister | CoordRegisterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CoordRegisterBlueprint]

    Super Class:
        RegisterCarrier
    """
    
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
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[CoordRegister | CoordRegisterBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(CoordRegister, entity)
        return cast(CoordRegister, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, CoordRegister)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, CoordRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[CoordRegisterBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(CoordRegisterBlueprint, self.entity)
            return blueprint
        
        model = cast(CoordRegister, self.entity)
        return CoordRegisterBlueprint(
            origin=model.origin,
            terminus=model.terminus,
        )


    