# src/transit/carrier/struct/binder/team/carrier.py

"""
Module: transit.carrier.struct.binder.team.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import TeamBinder, TeamBinderBlueprint
from transit import BinderCarrier


class TeamBinderCarrier(BinderCarrier[TeamBinder]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated TeamBinder its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [TeamBinder | TeamBinderBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[TeamBinderBlueprint]

    Super Class:
        BinderCarrier
    """
    _model: Optional[TeamBinder]
    _blueprint: Optional[TeamBinderBlueprint]
    
    def __init__(
            self,
            model: Optional[TeamBinder] | None = None,
            blueprint: Optional[TeamBinderBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[TeamBinder]
            blueprint: Optional[TeamBinderBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[TeamBinder | TeamBinderBlueprint]:
        if self._model is not None:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._blueprint is None and
                self._model is not None and
                isinstance(self._model, TeamBinder)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._blueprint is not None and
                self._model is None and
                isinstance(self._blueprint, TeamBinderBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[TeamBinderBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            return self._blueprint
        model = cast(TeamBinder, self._model)
        return TeamBinderBlueprint(
            white_team=model.white_team,
            black_team=model.black_team,
        )


    