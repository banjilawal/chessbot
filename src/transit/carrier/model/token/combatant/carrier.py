# src/transit/carrier/model/token/combatant/carrier.py

"""
Module: transit.carrier.model.token.combatant.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantToken, CombatantBlueprint
from transit import TokenCarrier


class CombatantCarrier(TokenCarrier):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CombatantToken or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Token|CombatantBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[CombatantBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[CombatantToken] | None = None,
            blueprint: Optional[CombatantBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CombatantToken]
            blueprint: Optional[CombatantBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[CombatantToken|CombatantBlueprint]:
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
                isinstance(self._model, CombatantToken)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, CombatantBlueprint)
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
    
    def extract_blueprint(self) -> Optional[CombatantBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(CombatantToken, self._model)
        return CombatantBlueprint(
            id=model.id,
            team=model.team,
            rank=model.rank,
            captor=model.captor,
            formation=model.formation,
            positions=model.positions,
            home_square=model.home_square,
        )


