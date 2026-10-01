# src/transit/carrier/model/account/carrier.py

"""
Module: transit.carrier.model.account.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC, abstractmethod


from typing import Generic, Optional, TypeVar

from domain import (
    HumanAccountBlueprint, MachineAccountBlueprint, Account, AccountBlueprint
)
from transit import ModelCarrier

T = TypeVar("T", bound="Account")

class AccountCarrier(ModelCarrier[T], ABC, Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Account or its Blueprint.

    Attributes:
        entity: [Account | AccountBlueprint]
        is_human_account_carrier: bool
        is_machine_account_carrier: bool

    Provides:
        -   def extract_blueprint() -> Optional[AccountBlueprint]

    Super Class:
        ModelCarrier
    """
    _model: Optional[T]
    _blueprint: Optional[AccountBlueprint[T]]
    
    def __init__(
            self,
            model: Optional[T] | None = None,
            blueprint: Optional[AccountBlueprint[T]] | None = None,
    ):
        """
        Args:
            model: Optional[T]
            blueprint: Optional[AccountBlueprint[T]]
        """
        super().__init__()
        self._model = model
        self._blueprint = blueprint
    
    @property
    def entity(self) -> Optional[T | AccountBlueprint[T]]:
        if self.is_empty:
            return None
        if self.has_model:
            return self._model
        return self._blueprint
    
    @property
    def has_model(self) -> bool:
        return (
                self._model is not None and
                self._blueprint is None
        )
    
    @property
    def has_blueprint(self) -> bool:
        return (
                self._model is None and
                self._blueprint is not None
        )
    
    @abstractmethod
    def extract_blueprint(self) -> Optional[AccountBlueprint[T]]:
        pass

    @property
    def is_human_account_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return  isinstance(blueprint, HumanAccountBlueprint)
    
    @property
    def is_machine_account_carrier(self) -> bool:
        blueprint = self.extract_blueprint()
        if blueprint is None:
            return False
        return isinstance(blueprint, MachineAccountBlueprint)