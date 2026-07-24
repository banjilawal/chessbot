# src/carrier/vector/carrier.py

"""
Module: carrier.vector.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import VectorBlueprint
from model import Vector
from carrier import ModelCarrier


class VectorCarrier(ModelCarrier[Vector]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Vector or VectorBlueprint
    
    Attributes:
        model: Optional[Vector]
        blueprint: Optional[VectorBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        ModelCarrier
    """
    _model: Optional[Vector]
    _blueprint: Optional[VectorBlueprint]
    
    def __init__(
            self,
            model: Optional[Vector] | None = None,
            blueprint: Optional[VectorBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Vector]
            blueprint: Optional[VectorBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Vector | VectorBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_carrying_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Vector)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, VectorBlueprint)
        )
    
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything
    
    def extract_blueprint(self) -> Optional[VectorBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return VectorBlueprint(
            x=self._model.x,
            y=self._model.y,
        )

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, VectorCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

    

    
    @property
    def is_carrying_too_much(self) -> bool:
        return self.active_toggles > 1
    
    @property
    def active_toggles(self) -> int:
        return len(self.to_dict)
    
    @property
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[Blueprint[T]]:
        pass
