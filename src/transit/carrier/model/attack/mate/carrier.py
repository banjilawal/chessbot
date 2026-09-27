# src/transit/carrier/model/attack/mate/carrier.py

"""
Module: transit.carrier.model.attack.mate.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CheckmateAttack, CheckmateAttackBlueprint
from transit import AttackCarrier


class CheckmateAttackCarrier(AttackCarrier[CheckmateAttack]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CheckmateAttack or its Blueprint across
            processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [CheckmateAttack | CheckmateAttackBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CheckmateAttackBlueprint]

    Super Class:
        AttackCarrier
    """
    
    def __init__(
            self,
            model: Optional[CheckmateAttack] | None = None,
            blueprint: Optional[CheckmateAttackBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CheckmateAttack]
            blueprint: Optional[CheckmateAttackBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[CheckmateAttack|CheckmateAttackBlueprint]:
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
                isinstance(self._model, CheckmateAttack)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, CheckmateAttackBlueprint)
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
    
    def extract_blueprint(self) -> Optional[CheckmateAttackBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(CheckmateAttack, self._model)
        return CheckmateAttackBlueprint(
            id=model.id,
            team=model.team,
            position=model.position,
            readiness=model.readiness,
            formation=model.formation,
            checkmate=model.checkmate,
            deployment=model.deployment,
            home_square=model.home_square,
            check_warning=model.check_warning,
            previous_position=model.previous_position,
        )


