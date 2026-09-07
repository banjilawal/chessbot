# src/transit/carrier/model/player/machine/carrier.py

"""
Module: transit.carrier.model.player.machine.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, cast

from domain import MachinePlayer, MachineBlueprint
from transit import PlayerCarrier


class MachineCarrier(PlayerCarrier):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated MachinePlayer or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [MachinePlayer|MachineBlueprint]

    Provides:
        - def extract_blueprint() -> Optional[MachineBlueprint]

    Super Class:
        MachinePlayerCarrier
    """
    
    _model: Optional[MachinePlayer]
    _blueprint: Optional[MachineBlueprint]
    
    def __init__(
            self,
            model: Optional[MachinePlayer] | None = None,
            blueprint: Optional[MachineBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[MachinePlayer]
            blueprint: Optional[MachineBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[MachinePlayer|MachineBlueprint]:
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
                isinstance(self._model, MachinePlayer)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.is_carrying_model and
                isinstance(self._blueprint, MachineBlueprint)
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
    
    def extract_blueprint(self) -> Optional[MachineBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(MachinePlayer, self._model)
        return MachineBlueprint(
            id=model.id,
            name=model.name,
            adviser=model.adviser,
        )
    
    



