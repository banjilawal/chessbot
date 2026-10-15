# src/transit/carrier/model/Account/carrier.py

"""
Module: transit.carrier.model.Account.carrier
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from domain import Account, AccountBlueprint
from transit import ModelCarrier

T = TypeVar("T", bound="Account")


class AccountCarrier(ModelCarrier[T], Generic[T]):
    """
    Role:
        - Boundary Carrier Interface

    Responsibilities:
        1.  Transport a hydrated Account or its Blueprint.

    Attributes:
        model: Optional[T]
        blueprint: Optional[AccountBlueprint[T]]

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
    
    def extract_blueprint(self) -> Optional[AccountBlueprint[T]]:
        if self.is_empty or self.has_model:
            return None
        return self._blueprint