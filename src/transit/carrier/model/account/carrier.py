# src/transit/carrier/model/account/carrier.py

"""
Module: transit.carrier.model.account.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from _testcapi import Generic
from typing import Optional, TypeVar, cast

from domain import HumanAccountBlueprint, MachineAccountBlueprint, Account, AccountBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Account")

class AccountCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Account or its Blueprint across processing boundaries.

    Attributes:
        size: int
        is_empty: bool
        is_over_capacity: bool
        is_model_carrier: bool
        is_blueprint_carrier: bool
        entity: [Account|AccountBlueprint]

    Provides:
        -   def extract_blueprint() -> Optional[AccountBlueprint]

    Super Class:
        ModelCarrier
    """
    _model: Optional[T]
    _blueprint: Optional[AccountBlueprint]
    
    def __init__(
            self,
            model: Optional[Account] | None = None,
            blueprint: Optional[AccountBlueprint] | None = None,
    ):
        """
        Args:
            model: Optional[Account]
            blueprint: Optional[AccountBlueprint]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[Account | AccountBlueprint]:
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
                isinstance(self._model, Account)
        )
    
    @property
    def is_carrying_blueprint(self) -> bool:
        return (
                not self.has_model and
                isinstance(self._blueprint, AccountBlueprint)
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
    
    def extract_blueprint(self) -> Optional[AccountBlueprint]:
        if self.is_empty: return None
        if self.is_carrying_blueprint: return self._blueprint
        
        model = cast(Account, self._model)
        return AccountBlueprint(
            id=model.id,
            name=model.name,
            adviser=model.adviser,
        )
    
    @property
    def is_carrying_human(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, HumanAccountBlueprint)
    
    @property
    def is_carrying_machine(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, MachineAccountBlueprint)