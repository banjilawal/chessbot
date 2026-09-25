# src/transit/carrier/model/attack/carrier.py

"""
Module: transit.carrier.model.attack.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from domain import Attack, AttackBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Attack")

class AttackCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Attack or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Attack|AttackBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[AttackBlueprint]

    Super Class:
        ModelCarrier
    """
    _model: Optional[T]
    _blueprint: Optional[AttackBlueprint]

    def __init__(
            self,
            model: Optional[Attack] | None = None,
            blueprint: Optional[AttackBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Attack]
            blueprint: Optional[AttackBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint

    @property
    def entity(self) -> Optional[Attack | AttackBlueprint]:
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
                isinstance(self._model, Attack)
        )

    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, AttackBlueprint)
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

    @abstractmethod
    def extract_blueprint(self) -> Optional[AttackBlueprint]:
        pass
    
    @property
    def is_king_attack_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return blueprint.is_king_attack_blueprint
    
    @property
    def is_pawn_attack_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return blueprint.is_pawn_attack_blueprint
    
    @property
    def is_combatant_attack_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return (
                not self.is_king_attack_carrier and
                not self.is_pawn_attack_carrier
        )


