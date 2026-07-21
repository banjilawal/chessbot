# src/carrier/arena/operand.py

"""
Module: carrier.arena.operand
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Optional

from blueprint import ArenaBlueprint
from model import Arena
from carrier import EntityCarrierToggle


class ArenaCarrier(EntityCarrierToggle[Arena]):
    """
    Role:
        -   Addressing
        -   Data-Holder
    
    Responsibilities:
        1.  Entity for transporting either a Arena or ArenaBlueprint
    
    Attributes:
        model: Optional[Arena]
        blueprint: Optional[ArenaBlueprint]
        is_model_carrier: bool
        is_blueprint_carrier: bool
        has_overflow: bool
        is_empty: bool
    
    Provides:
    
    Super Class:
        EntityCarrierToggle
    """
    _model: Optional[Arena]
    _blueprint: Optional[ArenaBlueprint]
    
    def __init__(
            self,
            model: Optional[Arena] | None = None,
            blueprint: Optional[ArenaBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Arena]
            blueprint: Optional[ArenaBlueprint]
        """
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> [Arena | ArenaBlueprint]:
        return self._model or self._blueprint
    
    @property
    def is_model_carrier(self) -> bool:
        return self._model is not None and self._blueprint is None
    
    @property
    def is_blueprint_carrier(self) -> bool:
        return self._model is None and self._blueprint is not None
    
    @property
    def is_empty(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def has_overflow(self) -> bool:
        return self._model is not None and self._blueprint is not None
    
    @property
    def size(self) -> int:
        if self.no_active_toggles: return 0
        if self.is_model_carrier or self.is_blueprint_carrier: return 1
        return 2
    
    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, ArenaCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

