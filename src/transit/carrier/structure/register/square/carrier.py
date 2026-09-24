# src/transit/carrier/structure/register/sqaure/carrier.py

"""
Module: transit.carrier.structure.register.square.carrier
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
        1.  Transport a hydrated SquareRegister its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [SquareRegister | SquareRegisterBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[SquareRegisterBlueprint]

    Super Class:
        RegisterCarrier
    """
    
    _model: Optional[SquareRegister]
    _blueprint: Optional[SquareRegisterBlueprint]
    
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
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[SquareRegister | SquareRegisterBlueprint]:
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
                isinstance(self._model, SquareRegister)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, SquareRegisterBlueprint)
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
    
    def extract_blueprint(self) -> Optional[SquareRegisterBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        structure = cast(SquareRegister, self._model)
        return SquareRegisterBlueprint(
            origin=structure.origin,
            destination=structure.destination,
        )


    