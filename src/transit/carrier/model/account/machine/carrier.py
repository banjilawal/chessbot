# src/transit/carrier/model/account/machine/carrier.py

"""
Module: transit.carrier.model.account.machine.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import MachineAccount, MachineAccountBlueprint
from transit import AccountCarrier


class MachineAccountCarrier(AccountCarrier[MachineAccount]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated MachineAccount or its Blueprint.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [MachineAccount|MachineAccountBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[MachineAccountBlueprint]

    Super Class:
        MachineAccountCarrier
    """
    
    _model: Optional[MachineAccount]
    _blueprint: Optional[MachineAccountBlueprint]
    
    def __init__(
            self,
            model: Optional[MachineAccount] | None = None,
            blueprint: Optional[MachineAccountBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[MachineAccount]
            blueprint: Optional[MachineAccountBlueprint]
        """
        super().__init__()
        self._model = model or Type[MachineAccount]
        self._blueprint = blueprint or Type[MachineAccountBlueprint]
    
    @property
    def entity(self) -> Optional[MachineAccount | MachineAccountBlueprint]:
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
                isinstance(self._model, MachineAccount)
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, MachineAccountBlueprint)
        )
    
    @property
    def size(self) -> int:
        return len([self._model, self._blueprint])
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_consistent(self) -> bool:
        return self.size == 1
    
    @property
    def not_consistent(self) -> bool:
        return not self.is_consistent
    
    def extract_blueprint(self) -> Optional[MachineAccountBlueprint]:
        if self.is_empty: return None
        if self.has_blueprint: return self._blueprint
        
        model = cast(MachineAccount, self._model)
        return MachineAccountBlueprint(
            id=model.id,
            name=model.name,
        )
    
    



