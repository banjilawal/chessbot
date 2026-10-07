# src/transit/carrier/model/footstep/carrier.py

"""
Module: transit.carrier.model.footstep.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import Footstep, FootstepBlueprint
from transit import ModelCarrier


class FootstepCarrier(ModelCarrier[Footstep]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Footstep its Blueprint.

    Attributes:
        has_model: bool
        has_blueprint: bool
        entity: [Footstep | FootstepBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[FootstepBlueprint]

    Super Class:
        ModelCarrier
    """
    _model: Optional[Footstep]
    _blueprint: Optional[FootstepBlueprint]
    
    def __init__(
            self,
            model: Optional[Footstep] | None = None,
            blueprint: Optional[FootstepBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Footstep]
            blueprint: Optional[FootstepBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Footstep | FootstepBlueprint]:
        if self._model is not None:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._blueprint is None and
                self._model is not None and
                isinstance(self._model, Footstep)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None and
                isinstance(self._blueprint, FootstepBlueprint)
        )
    
    def extract_blueprint(self) -> Optional[FootstepBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint:
            return self._blueprint
        model = cast(Footstep, self.entity)
        return FootstepBlueprint(
            position=model.position,
            previous_position=model.previous_position,
        )


    