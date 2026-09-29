# src/transit/carrier/model/account/carrier.py

"""
Module: transit.carrier.model.account.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod

from _testcapi import Generic
from typing import Optional, TypeVar

from domain import (
    HumanAccountBlueprint, MachineAccountBlueprint, Account, AccountBlueprint
)
from transit import ModelCarrier

T = TypeVar("T", bound="Account")

class AccountCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Account or its Blueprint.

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
    
    @property
    @abstractmethod
    def entity(self) -> Optional[T | AccountBlueprint[T]]:
        pass
    
    @property
    @abstractmethod
    def has_model(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def has_blueprint(self) -> bool:
        pass
    
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
        return self.size > 1
    
    def extract_blueprint(self) -> Optional[AccountBlueprint[T]]:
        pass
    
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