# src/transit/team/carrier.py

"""
Module: transit.team.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from fabrication import TeamBlueprint
from domain.model import Team
from transit import ModelCarrier


class TeamCarrier(ModelCarrier):
    """
    Role:
        -   Boundary Carrier

    Responsibilities:
        1.  Transport either a hydrated Team or its Blueprint across validation and other
            processing boundaries

    Attributes:
        model: Optional[Team]
        blueprint: Optional[TeamBlueprint]

    Provides:
        -   extract_blueprint() -> Optional[TeamBlueprint]

    Super Class:
        ModelCarrier
    """
    
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
    def entity(self) -> Optional[Team | TeamBlueprint]:
        if self.is_not_carrying_anything:
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
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, TeamBlueprint)
        )

    def extract_blueprint(self) -> Optional[TeamBlueprint]:
        if self.is_not_carrying_anything: return None
        if self.is_carrying_blueprint: return self._blueprint
        return TeamBlueprint(
            id=self._model.id,
            board=self._model.board,
            owner=self._model.owner,
            archetype=self._model.archetype,
        )
        
    @property
    def is_not_carrying_anything(self) -> bool:
        return self._model is None and self._blueprint is None
    
    @property
    def is_carrying_too_much(self) -> bool:
        return not self.is_not_carrying_anything

    def __eq__(self, other):
        if other is self: return True
        if other is None: return False
        if isinstance(other, TeamCarrier):
            return self.entity == other.entity
        return False
    
    def __hash__(self):
        return hash(self.entity)

