# src/transit/carrier/struct/register/square/carrier.py

"""
Module: transit.carrier.struct.register.square.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import SquareRegister, SquareRegisterBlueprint
from transit import RegisterCarrier


class SquareRegisterCarrier(RegisterCarrier[SquareRegister]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated SquareRegister its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [SquareRegister | SquareRegisterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[SquareRegisterBlueprint]

    Super Class:
        RegisterCarrier
    """
    
    def __init__(
            self,
            model: Optional[SquareRegister] | None = None,
            blueprint: Optional[SquareRegisterBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[SquareRegister]
            blueprint: Optional[SquareRegisterBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint)
    
    @property
    def entity(self) -> Optional[SquareRegister | SquareRegisterBlueprint]:
        entity = super().entity
        if entity is None:
            return None
        if self.has_model:
            return cast(SquareRegister, entity)
        return cast(SquareRegister, entity)
    
    @property
    def has_model(self) -> bool:
        return (
                super().has_model is None and
                isinstance(self.entity, SquareRegister)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self.entity, SquareRegisterBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[SquareRegisterBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            blueprint = cast(SquareRegisterBlueprint, self.entity)
            return blueprint
        
        model = cast(SquareRegister, self.entity)
        return SquareRegisterBlueprint(
            origin=model.origin,
            destination=model.destination,
        )


    