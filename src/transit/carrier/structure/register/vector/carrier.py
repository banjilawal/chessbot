# src/transit/carrier/structure/register/vector/carrier.py

"""
Module: transit.carrier.structure.register.vector.carrier
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
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [VectorRegister | VectorRegisterBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[VectorRegisterBlueprint]

    Super Class:
        RegisterCarrier
    """
    
    _model: Optional[VectorRegister]
    _blueprint: Optional[VectorRegisterBlueprint]
    
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
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[VectorRegister | VectorRegisterBlueprint]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, VectorRegister)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, VectorRegisterBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def not_consistent(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[VectorRegisterBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        structure = cast(VectorRegister, self._model)
        return VectorRegisterBlueprint(
            u=structure.u,
            v=structure.v,
        )


    