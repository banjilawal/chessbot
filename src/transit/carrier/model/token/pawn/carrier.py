# src/transit/carrier/model/token/pawn/carrier.py

"""
Module: transit.carrier.model.token.pawn.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import PawnToken, PawnTokenBlueprint
from transit import TokenCarrier


class PawnTokenCarrier(TokenCarrier[PawnToken]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated PawnToken or its Blueprint.

    Attributes:
        model: Optional[PawnToken]
        blueprint: Optional[PawnTokenBlueprint]
        entity: [PawnToken | PawnTokenBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[PawnTokenBlueprint]

    Super Class:
        ModelCarrier
    """
    
    def __init__(
            self,
            model: Optional[PawnToken] | None = None,
            blueprint: Optional[PawnTokenBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[PawnToken]
            blueprint: Optional[PawnTokenBlueprint]
        """
        super().__init__(model=model, blueprint=blueprint,)
    
    @property
    def entity(self) -> Optional[PawnToken | PawnTokenBlueprint]:
        entity = super().entity
        if (
                isinstance(entity, PawnToken) or
                isinstance(entity, PawnTokenBlueprint)
        ):
            return entity
        
        return None
    
    @property
    def has_model(self) -> bool:
        return isinstance(self.entity, PawnToken)
    
    @property
    def has_blueprint(self) -> bool:
        return isinstance(self.entity, PawnTokenBlueprint)
    
    def extract_blueprint(self) -> Optional[PawnTokenBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return cast(PawnTokenBlueprint, self.entity)
        
        model = cast(PawnToken, self.entity)
        return PawnTokenBlueprint(
            id=model.id,
            team=model.team,
            rank=model.rank,
            captor=model.captor,
            position=model.position,
            readiness=model.readiness,
            formation=model.formation,
            deployment=model.deployment,
            home_square=model.home_square,
            promotion_state=model.promotion_state,
            previous_position=model.previous_position,
        )


