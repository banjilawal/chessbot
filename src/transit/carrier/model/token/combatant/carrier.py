# src/transit/carrier/model/token/combatant/carrier.py

"""
Module: transit.carrier.model.token.combatant.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import CombatantToken, CombatantTokenBlueprint
from transit import TokenCarrier


class CombatantTokenCarrier(TokenCarrier[CombatantToken]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated CombatantToken or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Token|CombatantBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[CombatantBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[CombatantToken] | None = None,
            blueprint: Optional[CombatantTokenBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[CombatantToken]
            blueprint: Optional[CombatantTokenBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint, )
    
    @property
    def entity(self) -> Optional[CombatantToken | CombatantTokenBlueprint]:
        entity = super().entity
        if (
                isinstance(entity, CombatantToken) or
                isinstance(entity, CombatantTokenBlueprint)
        ):
            return entity
        
        return None
    
    @property
    def has_model(self) -> bool:
        return isinstance(self.entity, CombatantToken)
    
    @property
    def has_blueprint(self) -> bool:
        return isinstance(self.entity, CombatantTokenBlueprint)
       
    def extract_blueprint(self) -> Optional[CombatantTokenBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return cast(CombatantTokenBlueprint, self.entity)
        
        model = cast(CombatantToken, self.entity)
        return CombatantTokenBlueprint(
            id=model.id,
            team=model.team,
            footstep=model.footstep,
            captor=model.captor,
            readiness=model.readiness,
            formation=model.formation,
            deployment=model.deployment,
            home_square=model.home_square,
        )


