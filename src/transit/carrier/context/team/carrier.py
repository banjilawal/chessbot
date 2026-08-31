# src/transit/carrier/context/team/carrier.py

"""
Module: transit.carrier.context.team.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Team, TeamBlueprint
from transit import ContextCarrier


class TeamContextCarrier(ContextCarrier[TeamContext]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated TeamContext or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Team|TeamContextBlueprint]

    Provides:
        - def extract_ContextBlueprint() -> Optional[TeamContextBlueprint]

    Super Class:
        ContextCarrier
    """
    
    _model: Optional[TeamContext]
    _blueprint: Optional[TeamContextBlueprint]
    
    def __init__(
            self,
            model: Optional[TeamContext] | None = None,
            blueprint: Optional[TeamContextBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[TeamContext]
            blueprint: Optional[TeamContextBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Team|TeamContextBlueprint]:
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
                isinstance(self._model, Team)
        )
    
    @property
    def is_carrying_ContextBlueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, TeamBlueprint)
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
    
    def extract_ContextBlueprint(self) -> Optional[TeamContextBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        context = cast(TeamContext, self._model)
        return TeamContextBlueprint(
            id=context.id,
            board=context.board,
            owner=context.owner,
            roster=context.roster,
            archetype=context.archetype,
        )

