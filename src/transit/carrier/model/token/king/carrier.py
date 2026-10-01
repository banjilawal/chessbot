# src/transit/carrier/model/token/king/carrier.py

"""
Module: transit.carrier.model.token.king.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import KingToken, KingTokenBlueprint
from transit import TokenCarrier


class KingTokenCarrier(TokenCarrier[KingToken]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated KingToken or its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [KingToken | KingTokenBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[KingTokenBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[KingToken] | None = None,
            blueprint: Optional[KingTokenBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[KingToken]
            blueprint: Optional[KingTokenBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint, )
    
    @property
    def entity(self) -> Optional[KingToken | KingTokenBlueprint]:
        entity = super().entity
        if (
                isinstance(entity, KingToken) or
                isinstance(entity, KingTokenBlueprint)
        ):
            return entity
        
        return None
    
    @property
    def has_model(self) -> bool:
        return isinstance(self.entity, KingToken)
    
    @property
    def has_blueprint(self) -> bool:
        return isinstance(self.entity, KingTokenBlueprint)
    
    def extract_blueprint(self) -> Optional[KingTokenBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(KingToken, self._model)
        return KingTokenBlueprint(
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


