# src/assurance/loader/model/team/extract.py

"""
Module: assurance.loader.model.team.extract
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from assurance import ModelExtract
from domain import Blueprint, Team, TeamBlueprint
from transit import EntityCarrier, TeamCarrier


class TeamlExtract(ModelExtract[Team]):

    def __(
            self,
            carrier: EntityCarrier[Team],
            blueprint: Optional[Blueprint[Team]],
            model: Optional[Team],
    ):
        """
        Args:
            carrier: EntityCarrier[Team]
            blueprint: Optional[Blueprint[Team]]
            model: Optional[T]
        """
        super().__init__(
            carrier=carrier,
            blueprint=blueprint,
            model=model,
        )
        
    @property
    def carrier(self) -> TeamCarrier:
        return cast(TeamCarrier, super().carrier)
    
    @property
    def model(self) -> Optional[Team]:
        return cast(Team, super().model)
    
    @property
    def blueprint(self) -> Optional[TeamBlueprint]:
        return cast(TeamBlueprint,super().blueprint)
    
    @property
    def is_model_load(self) -> bool:
        if self._model is None:
            return False
        if (
                self.model is None or
                not isinstance(self.model, Team)
        ):
            return False
        return True
    
    @property
    def is_blueprint_load(self) -> bool:
        if self._blueprint is None:
            return False
        if (
                self.blueprint is None or
                not isinstance(self.blueprint, TeamBlueprint)
        ):
            return False
        return True