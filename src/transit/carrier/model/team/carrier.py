# src/transit/carrier/model/team/carrier.py

"""
Module: transit.carrier.model.team.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Team, TeamBlueprint
from transit import ModelCarrier


class TeamCarrier(ModelCarrier[Team]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Team or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Team|TeamBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[TeamBlueprint]

    Super Class:
        ModelCarrier
    """
    
    _model: Optional[Team]
    _blueprint: Optional[TeamBlueprint]
    
    def __init__(
            self,
            model: Optional[Team] | None = None,
            blueprint: Optional[TeamBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Team]
            blueprint: Optional[TeamBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Team|TeamBlueprint]:
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
    def is_carrying_blueprint(self) -> bool:
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
    
    def extract_blueprint(self) -> Optional[TeamBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(Team, self._model)
        return TeamBlueprint(
            id=model.id,
            board=model.board,
            owner=model.owner,
            roster=model.roster,
            archetype=model.archetype,
        )

