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
        1.  Transport a hydrated TeamContext or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_not_consistent: bool
        has_model: bool
        has_blueprint: bool
        entity: [Team|TeamContextBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[TeamContextBlueprint]

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
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None and
                isinstance(self._model, Team)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, TeamContextBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_consistent(self) -> bool:
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[TeamContextBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(TeamContext, self._model)
        return TeamContextBlueprint(
            id=model.id,
            board=model.board,
            owner=model.owner,
            roster=model.roster,
            archetype=model.archetype,
        )

