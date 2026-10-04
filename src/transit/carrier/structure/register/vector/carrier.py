# src/transit/carrier/struct/register/vector/carrier.py

"""
Module: transit.carrier.struct.register.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import VectorRegister, VectorRegisterBlueprint
from transit import RegisterCarrier


class VectorRegisterCarrier(RegisterCarrier[VectorRegister]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated VectorRegister its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [VectorRegister | VectorRegisterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[VectorRegisterBlueprint]

    Super Class:
        RegisterCarrier
    """
    
    def __init__(
            self,
            model: Optional[VectorRegister] | None = None,
            blueprint: Optional[VectorRegisterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[VectorRegister]
            blueprint: Optional[VectorRegisterBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[VectorRegister | VectorRegisterBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(VectorRegister, entity)
        return cast(VectorRegister, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, VectorRegister)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, VectorRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[VectorRegisterBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(VectorRegisterBlueprint, self.entity)
            return blueprint
        
        model = cast(VectorRegister, self.entity)
        return VectorRegisterBlueprint(
            u=model.u,
            v=model.v,
        )


    